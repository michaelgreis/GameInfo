import psycopg2 #needed for the connection to the postgresql database
import json #needed to read scraper data

class datapush():
    def __init__(
        self
        ):
        self.file_read = ''


#establish the connection to the database instance
    def connect_to_db(
        self
        ):
        try:
            conn = psycopg2.connect("dbname='landingzone' user='dataingestionpush' host='lz-scraper.czn1pljrayu4.us-east-2.rds.amazonaws.com' password='alexmichael'")
            print('Connection successful you skillful coder you.')
            return(conn)
        except:
            print('unable to connect')

#purpose of this function is to read json data in a file that is passed into it.
    def read_data(
        self, file_to_read
    ):
        #self.json_data=json.load(open(file_to_read))
        #return(self.json_data)
        return(json.load(open(file_to_read)))

#This is used to default values before inserting to the database so that we don't have complete junk data. Can be used later to default different values.
    def default_value(
        self,variable
    ):
        if variable is not None:
            return variable
        else:
            return 'Unknown'

#this pushes the sony data into the right table. Going to need to be re-written for each source that we have. Or re-written to use a config file.
    def push_data(
        self,data_to_load,data_source
    ):
        conn = self.connect_to_db()
        cur = conn.cursor()
        cur.execute("SET search_path TO scraperdata")
        print('Cursor created successfully')
        for entry in data_to_load:
            try: #this contains the different insert script needed to move the data into the database from the different sources.
                if data_source=='sonymarketplace':
                    cur.execute("INSERT INTO sonywebsite(image,badge_sale,game_name,plus_sale,console_type,item_type) VALUES(%s,%s,%s,%s,%s,%s) ON CONFLICT ON CONSTRAINT unique_row DO NOTHING;",(self.default_value(entry['image']),self.default_value(entry['badge_sale']),self.default_value(entry['game_name']),self.default_value(entry['plus_sale']),self.default_value(entry['console_type']),self.default_value(entry['item_type']))) #this is what actually inserts to the database.
                elif data_source=='steammarketplace':
                    try:
                        cur.execute("INSERT INTO steammarketplace(id, full_data) VALUES(%s,%s);",(self.default_value(entry['id']),self.default_value(json.dumps(entry))))
                        break
                    except:
                        cur.execute("INSERT INTO steammarketplace(id,full_data) VALUES(%s,%s);",(self.default__value(None),self.default_value(json.dumps(entry))))
                else:
                    return 'Error. No insert script for data source.'
            except:
                print('Failed to write '+str(entry))
                raise
        conn.commit()
        cur.close()
        conn.close()

#This is used to select which object the data will be inserted to.
#    def insert_execute_script(
#        self, source
#        ):
#        if source='sonymarketplace':
#            return sony_network_load()
#        else if source='steammarketplace'
#            return steam_load()
#        else:
#            return 'Error. No insert script for data source.'

#this is the insert statement into the sony network's landing zone.
#    def sony_network_load(
#        self
#        ):
#        return ()

#This is the insert statement into the steam data source's landing zone.
#    def steam_load(
#        self
#        ):
#        return("INSERT INTO steammarketplace(id, title, release_date, app_name, early_access, full_data) VALUES(%s,%s,%s,%s,%s,%s) ON CONFLICT ON CONSTRAINT unique_row_steam DO NOTHING;",(self.default_value(entry['id']),self.default_value(entry['title']),self.default_value(entry['release_date']),self.default_value(entry['app_name']),self.default_value(entry['early_access']),self.default_value(entry)))





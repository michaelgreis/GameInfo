import psycopg2 #needed for the connection to the postgresql database
import json #needed to read scraper data

class datapush():
    def __init__(
        self
        ):
        self.file_read = ''
        self.json_data = []


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
        if variable is None:
            return 'Unknown'
        else:
            return variable

#this pushes the sony data into the right table. Going to need to be re-written for each source that we have. Or re-written to use a config file.
    def push_data(
        self,data_to_load
    ):
        conn = self.connect_to_db()
        cur = conn.cursor()
        cur.execute("SET search_path TO scraperdata")
        print('Cursor created successfully')
        for entry in data_to_load:
            try:
                cur.execute("INSERT INTO sonywebsite(image,badge_sale,game_name) VALUES(%s,%s,%s) ON CONFLICT ON CONSTRAINT unique_row DO NOTHING;",(self.default_value(entry['image']),self.default_value(entry['badge_sale']),self.default_value(entry['game_name'])))
                #print('Successful insert.')
            except:
                print('Failed to write '+str(entry))
        conn.commit()
        cur.close()
        conn.close()





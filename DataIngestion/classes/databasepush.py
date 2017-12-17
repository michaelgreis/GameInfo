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
        self.json_data=json.load(open(file_to_read))
        return(self.json_data)

#this pushes the sony data into the right table. Going to need to be re-written for each source that we have. Or re-written to use a config file.
    def push_data(
        self
    ):
        cur = self.connect_to_db()
        #cur = conn.cursor()
        for entry in self.json_data:
            print(entry['game_name'])
            try:
                cur.execute("INSERT INTO scraperdata.sonywebsite(image,badge_sale,game_name) VALUES(%s,%s,%s)",(entry['image'],entry['badge_sale'],entry['game_name'],))
            except:
                print('Failed to write '+str(entry))





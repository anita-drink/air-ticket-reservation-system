# database connector; reusable doorway from flask into sql database
import pymysql
from config import Config

def get_connection():
    return pymysql.connect( #creates a live connection to the mysql db
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        cursorclass=pymysql.cursors.DictCursor, #query results come back as dictionaries
        autocommit=True #auto saves changes to the db after insert/delete/update
    )
#the returned object from get_connection is what flask routes will use to run sql queries
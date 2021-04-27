# Define your item pipelines here
import sqlite3
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# for mysql=
#import mysql.connector

# cnx = mysql.connector.connect(user='scott', password='password',
#                               host='127.0.0.1',
#                               database='employees')
# cnx.close()

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TutorialPipeline:
    def __init__(self):
        self.connection()
        
        self.create()
    def connection(self):
        self.conn=sqlite3.connect("new.db") 
#       for mysql
#       self.cnx = mysql.connector.connect(user='scott', password='password',
#                               host='127.0.0.1',
#                               database='employees')
        self.curs=self.conn.cursor()
    def create(self):
        self.curs.execute(""" DROP TABLE IF EXISTS quotes_table """)
        self.curs.execute(""" create table quotes_table(
 
        title text,
        author text,
        tag text
                ) """)
    def process_item(self, item, spider):
        self.store(item)
        return item
    def store(self,item):
        self.curs.execute( """insert into quotes_table values(?,?,?)""",(# """insert into quotes_table values(%s,%s,%s)"""
            item["author"][0],
            item["text"][0],
            item["tag"][0]

        ) )
        self.conn.commit()



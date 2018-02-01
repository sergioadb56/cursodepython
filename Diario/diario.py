import datetime
from peewee import *
from collections import OrderedDict

pg_db = PostgresqlDatabase(database='BDSistema',user='analisis', password='adminadmin', host='localhost', port=5432)
menu_items = OrderedDict([
       ('a','add entry'),
       ('v','view entry'),
       ('d','delete entry') 
    ])


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default= datetime.datetime.now) 
        
    class Meta:
        database= pg_db
        
def create_and_connect():
    """Connects to the database and creates the tables"""
    pg_db.connect(reuse_if_open=True)
    pg_db.create_tables([Entry])
    
    
        
def menu_loop():
    """Show menu"""
    
    
def add_entry():
    """Add Entry"""
    
def view_entries():
    """View all entries"""

def delete_entry(entry):
    """Delete and Entry"""
    
    
if __name__ == '__main__': 
    create_and_connect()   
    menu_loop()

    
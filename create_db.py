'''
'   Cost Distribution API
'
'   Pavlos Sakoglou, M.Sc.
'
'   Demo database creation methods in native Python with SQLite3 API
'
'''

# Import the native SQLite3 database API
import sqlite3

# Function that creates a new database (if it doesn't exists already)
# and instantiates N separate tables with specified attributes
# In this example we only instantiate a general Roivant table, and a 
# table for one subsidiary. By induction, we can create more tables
def create_database():
    conn = sqlite3.connect('RoivantDB.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Roivant (datestamp TEXT, service TEXT, price REAL, date TEXT, score REAL)')
    c.execute('CREATE TABLE IF NOT EXISTS Datavant (datestamp TEXT, service TEXT, price REAL, date TEXT, score REAL)')
    c.close()
    conn.close()
    
# Create 
create_database()  

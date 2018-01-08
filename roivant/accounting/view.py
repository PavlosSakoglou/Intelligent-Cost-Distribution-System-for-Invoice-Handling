'''
'   Cost Distribution API
'
'   Pavlos Sakoglou, M.Sc.
'
'   View component
'
'''

# Import a Python database API called SQLite3
import sqlite3

# Main MIS class to querry information from database
class View:
    
    # Constructor
    # The retrieved data are being incapsulated
    def __init__(self):
        self.data = []
            
    # Plot the data once you have retrieve them
    def plotCostDistribution(self):
        '''TBD'''
        pass
    
    # Display the general cost table of Roivant
    def plotCostTable(self):
        conn = sqlite3.connect("C:\\Users\\Pavlos\\Desktop\\Roivant\\RoivantDB.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Roivant")
        self.data = c.fetchall()
        c.close()
        conn.close()
        print(self.data)
    
    # Retrieve (get) the data from the general cost table of Roivant
    def getCostTable(self):
        conn = sqlite3.connect("C:\\Users\\Pavlos\\Desktop\\Roivant\\RoivantDB.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Roivant")
        self.data = c.fetchall()
        c.close()
        conn.close()
        return self.data
    

# Specialized MIS class for Datavant
# Follows similar logic as above
class Datavant:
    
    # Constructor
    def __init__(self):
        self.data = []
        
    # Plot the data once you have retrieve them
    def plotCostDistribution(self):
        '''TBD'''
        pass
    
    # Display the general cost table of Roivant
    def plotCostTable(self):
        conn = sqlite3.connect("RoivantDB.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Roivant")
        self.data = c.fetchall()
        print(self.data)
    
     # Retrieve (get) the data from the general cost table of Roivant
    def getCostTable(self):
        conn = sqlite3.connect("RoivantDB.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Roivant")
        self.data = c.fetchall()
        return self.data
    
    
# Functions encapsulated in "buttons" to plot or display 
# cost-related information    
        
def view_all_costs():
    print("\nView Roivant Cost Distribution:\n")
    view_all = View()
    view_all.plotCostTable()
    
def view_datavant_costs():
    print("\nView Datavant Cost Distribution:\n")
    view_datavant = Datavant()
    datavant_cost_table = view_datavant.getCostTable()
    print(datavant_cost_table)
    
'''
'   Cost Distribution API
'
'   Pavlos Sakoglou, M.Sc.
'
'   Cost component
'
'''

# Invoke the code to be used from the other files
from roivant.accounting import invoice 
import sqlite3
import datetime
import time

# General Cost class
class Cost:
    
    # Constructor
    # Encapsulates the invoice extracted data
    def __init__(self):
        self.invoice_info = []

    # Loads and processes the input invoice
    # Look at the Invoice class for the methods below
    def loadInvoice(self, invoice_path):
        inv = invoice.Invoice()
        inv.processInvoice(invoice_path)
        self.invoice_info = inv.getInfo()
        print("Invoice loaded")
            
    # Displays the extracted information and asks user 
    # to review and press "OK"
    def review(self):
        print("Please review the following:")
        for i in self.invoice_info:
            print(i)
        print("Press 1 when ready, 0 to cancel.")
        return int(input())
        
    # Confirmation screen
    # Displays the information again and asks user
    # to confirm and press "OK"
    def confirm(self):
        print("Please confirm the following:")
        for i in self.invoice_info:
            print(i)
        print("Press 1 to submit, 0 to cancel")
        return int(input())
        
    # Method that distributes the cost and writes in the 
    # database appropriately. The following code writes in 
    # the table of the database that the cost belongs to.
    # If some invoice refers only to one subsidiary, 
    # the code below will allocate that cost only there.
    def submit(self):
        addresses = self.invoice_info[-1]
        t = time.time()
        datestamp = str(datetime.datetime.fromtimestamp(t).strftime('%m-%d-%Y %H:%M:%S'))
        price = self.invoice_info[0][1]
        service = self.invoice_info[1][1]
        date = self.invoice_info[2][1]
        score = self.invoice_info[3][1]
        conn = sqlite3.connect('RoivantDB.db')
        c = conn.cursor()
        for i in addresses[1]:
            if i == 'Roivant':   
                c.execute("INSERT INTO Roivant (datestamp, service, price, date, score) VALUES(?,?,?,?,?)",
                          (datestamp, service, price, date, score))
                conn.commit()
            if i == 'Datavant':
                c.execute("INSERT INTO Datavant (datestamp, service, price, date, score) VALUES(?,?,?,?,?)",
                          (datestamp, service, price, date, score))
                conn.commit()
        c.close()
        conn.close()
        print("Success!")
        
    # Naive error message function, to warn the user
    # that something went wrong upon submission
    def throw(self):
        print("Something went wrong!")
        return False
    
    # Function that resets all invoice info
    # This function is used when the user doesn't
    # confirm or review the invoice information
    def reset(self):
        print("Reseting...")
        self.invoice_info = []
        
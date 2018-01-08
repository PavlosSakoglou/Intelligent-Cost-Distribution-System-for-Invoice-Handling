'''
'   Cost Distribution API
'
'   Pavlos Sakoglou, M.Sc.
'
'   Invoice component
'
'''

# Invoke the code to be used from the other files
from roivant.accounting import invoiceAI as ai
from roivant.accounting import invoiceProcessor as ip

# Invoice class to objectify a new invoice
class Invoice:
    
    # Constructor
    # Encapsulates all the invoice data of interest
    # that are meant to be copied in the database
    # We can add more attributes here without
    # harming performance
    # The rationale is that there is a limited number
    # of attributes are interested in an invoice
    def __init__(self):
        self.price = 0.0
        self.service = ""
        self.date = ""
        self.score = 0.0
        self.addresses = []        
        
    # Function to process the invoice and assign 
    # the extracted information to each invoice attribute
    def processInvoice(self, pdf_path):
        text = ip.pdfToString(pdf_path)
        self.date = ip.processDate(text)
        self.price = ip.processPrice(text)
        self.service = ip.processService(text)
        analysis = ai.InvoiceAI()
        analysis.determineScore(text)
        self.score = analysis.getScore()
        self.addresses = ip.getAddresses(text)
        
        
    # Function to return a list of the initialized
    # invoice attributes
    def getInfo(self):
        return [ ["price", self.price],
                 ["service", self.service],
                 ["date", self.date],
                 ["score", self.score],
                 ["addresses", self.addresses] ]
    
    
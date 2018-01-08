'''
'   Cost Distribution API
'
'   Pavlos Sakoglou, M.Sc.
'
'   Invoice Processor component
'
'''

# Import a PDF reader Python library
# This might need further installation, but its open source
import PyPDF2

# Notice! 
# The implementation below is sloppy and unsafe
# This implementation is for demonstration only
# To achieve high performance and accurate results
# a good method to work around this is regular expressions

# Free function that reads a pdf and converts its contents 
# to a string of characters
def pdfToString(pdf_path):
    pdfFileObj = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    return pageObj.extractText()
    
# Free function that reads the string version of the invoice
# and extracts the date from its location in the string
def processDate(text):
    start = text.find("Start Date") + 10
    end = text.find("End Date")
    date = text[start:end]
    temp = ""
    for i in date:
       if i == ',':
            temp += ', '
            break
               
       if not i.isspace():
           if i.isalpha():
               temp += i
           else:
               temp += ' '
               temp += i
        
    temp += date[len(date) -7: len(date) - 3]
    return temp
    
# Free function that reads the string version of the invoice
# and extracts the service from its location in the string
def processService(text):
    start = text.find("Service(s)") + 13
    end = text.find("Point(s)") - 3
    return text[start:end]

# Free function that reads the string version of the invoice
# and extracts the price from its location in the string
def processPrice(text):
    start = text.find("Cost Allocation") + 19
    end = text.find("per user") - 3
    return float(text[start:end])

# Free function that reads the string version of the invoice
# and extracts the subsidiary companies that the invoice refers to
def getAddresses(text):
    ''' Extract Subsidiaries' names '''
    var1 = 'Roivant'
    var2 = 'Datavant'
    addresses = [var1, var2]
    return addresses

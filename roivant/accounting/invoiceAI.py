'''
'   Cost Distribution API
'
'   Pavlos Sakoglou, M.Sc.
'
'   Invoice AI component
'
'''

# Invoke the random library of Python
# This holds only for this demo
# Expected more advanced code below
import random

# InvoiceAI is a class that reads parts of the invoice,
# infers its importance, and assigns an importance score
# which indicates whether the represented expense should
# be reconsidered or not
class InvoiceAI:
    
    # Constructor
    # Encapsulates an abstract importance score
    # To be redefined later
    def __init__(self):
        self.score = 0.0
        
    # Function that returns the score, once calculated
    def getScore(self):
        return self.score
    
    # Function responsible for analysis and invoice content processing
    # that derives and assigns a score to the underlying invoice
    def determineScore(self, text):
        # Do something
        self.score = random.uniform(0,1)
        return self.score
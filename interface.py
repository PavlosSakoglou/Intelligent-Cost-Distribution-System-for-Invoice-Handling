'''
'   Cost Distribution API
'
'   Pavlos Sakoglou, M.Sc.
'
'   Interface component
'
'''

# Invoke the code to be used from the other files
from roivant.accounting import cost
from roivant.accounting import view

# Back-end code for submitting a new invoice
def submit_new_invoice(invoice_path):
        
    # Instantiate a Cost object
    new_cost = cost.Cost()
    
    # Load the invoice for processing
    new_cost.loadInvoice(invoice_path)
    
    # Review the invoice information
    reviewed = new_cost.review()
    
    # When you review it, confirm and submit
    # Otherwise cancel the process
    if reviewed != 0:
        success = new_cost.confirm()
        
        if success != 0:
            return new_cost.submit()
        else:
            new_cost.throw()
            new_cost.reset()
            return 0
    else:
        new_cost.throw()
        new_cost.reset()
        return 0


''' 
new_invoice = GET_FROM_LEDGER()
new_invoice = toPDF(new_invoice)  #  Now the invoice is in pdf format
'''

# Submit a new invoice
new_invoice = 'virus_software_invoice.pdf'
submit_new_invoice(new_invoice)

# Print/Visualize cost distributions
view.view_all_costs()
view.view_datavant_costs()



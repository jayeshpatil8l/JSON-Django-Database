from firebase_admin import db
import json
from fetchdata.settings import database

def push_data(form):
    json_file = form.cleaned_data['json_file']

    json_data = json.load(json_file)

    head = json_data['receipt']

    receipt_details = head['receipt_details']
    items = head['items']
    customers = head['bill_to']

    db = database

    receipt_ref = db.child('receipts')

    receipt_no = receipt_details['receipt_number']
    date = receipt_details['receipt_date']

    receipt_data = {
        'Receipt_no': receipt_no,
        'Date': date
    }

    receipt_ref.push(receipt_data)

    
    items_ref = db.child('items')

    item_key = receipt_no

    for item_data in items:
        qty = item_data['qty'],
        description = item_data['description'],
        unit_price = item_data['unit_price'],
        amount = item_data['amount']

        item_data = {
            'Qty': qty,
            'Description': description,
            'Unit Price': unit_price,
            'Amount': amount
        }

        items_ref.child(item_key).push(item_data)


    customer_ref = db.child('customers')

    customer_key = receipt_no

    fullname = customers['name'].split(' ')
    fname = fullname[0]
    lname = fullname[1]
    address = customers['address']

    customer_data = {
        'First Name': fname,
        'Last Name': lname,
        'Address': address
    }

    customer_ref.child(customer_key).set(customer_data)






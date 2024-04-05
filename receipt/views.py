from django.shortcuts import render
from django.http import JsonResponse
from .data import push_data
from .forms import uploadJSONFile
from .models import *


# Create your views here.
def upload_JSON(request):
    form = uploadJSONFile(request.POST, request.FILES)
    if request.method == 'POST':
        
        if  form.is_valid():

            # json_file = form.cleaned_data['json_file']

            # json_data = json.load(json_file)

            # head = json_data['receipt']

            # receipt_details = head['receipt_details']
            # items = head['items']
            # customers = head['bill_to']

            # receipt = Receipt.objects.create(
            #     receipt_no = receipt_details['receipt_number'],
            #     date = receipt_details['receipt_date']
            # )
            # receipt.save()

            # for item_data in items:
            #     item = Item.objects.create(
            #         receipt_no = receipt,
            #         qty = item_data['qty'],
            #         description = item_data['description'],
            #         unit_price = item_data['unit_price'],
            #         amount = item_data['amount']
            #     )
            #     item.save()

            # fullname = customers['name'].split(' ')
            # customer = Customer.objects.create(
            #     receipt_no = receipt,
            #     fname = fullname[0],
            #     lname = fullname[1],
            #     address = customers['address']
            # )
            # customer.save()

            push_data(form)

            return JsonResponse({'message':'JSON file uploaded and data saved successfully'})
    else:
        return render(request, 'upload.html', {'form': form})

            



           
            

from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings
from django.http import HttpResponse
from employee_information.models import Department, Position, Employees, Vehicle_Category,Vehicle,Expense_Category,Expense,Freight_Category,Commodity,Carrier,Vessel,Vendor,Customer,Contract_owner,Agent,Booking,Currency_exchange,Settlement,Container_sale,Container_purchase,lease_rental,Container_slot,Special_rate,Booking_invoice, BookingUpdate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json
from django.http import HttpResponse, JsonResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import string
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
from django.templatetags.static import static
import os
from django.contrib import messages
from django.http import FileResponse
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail

from django.template.loader import render_to_string

from django.contrib.auth import login, authenticate,logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Sum
from django.core.serializers import serialize


import csv
import datetime
import xlwt
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from urllib import response
from django import template
from django.template.loader import render_to_string
# from  .forms import attendForm
import weasyprint
from weasyprint import HTML
import tempfile
from django.db.models import Sum
from io import BytesIO
import os
from string import Template
from django.contrib import messages

import weasyprint
from weasyprint import HTML
import tempfile
from django.db.models import Sum

from io import BytesIO
import os
from string import Template
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
from employee_information.forms import CreateUserForm


############################                 Register Code        #########################################
def registerpage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' +user)
            return redirect('/loginpage')
    context={'form': form}
    return render(request,'employee_information/register.html',context)


#######################################     Login Code                     ###########################   

def loginpage(request):
  if request.method=='POST':
    username=  request.POST.get('username')
    password= request.POST.get('password')
    user=authenticate(request, username=username,password=password)
    if user is not None:
        login(request,user)
        messages.info(request, f"You are now logged in as {username}.")
        return redirect('/home')
    else:
        messages.error(request, "Unsuccessful registration. Invalid information.")
     
  context={}
  return render (request,'employee_information/loginn.html',context)

###################################   logout   ############################

def logoutuser(request):
    logout(request)
    return redirect('/loginpage')


#######################################     Customer                    ###########################   

@login_required
def customer(request):
    cust= Customer.objects.all()
   
   
    context = {
        'page_title':'Customer',
        'Cust': cust}
    return render(request, 'employee_information/customer.html',context)



########################################   Home #########################################

@login_required
def home(request):
    context = {
        'page_title':'Home',
        'employees':employees,
     
        'total_employee':len(Vendor.objects.all()),
         'total_veh':len(Commodity.objects.all()),
         'total_cat':len(Customer.objects.all()),
            'total_exp':len(Booking.objects.all()),
                'total_ag':len(Agent.objects.all()),
                    'total_emp':len(Employees.objects.all()),
    }
    return render(request, 'employee_information/home.html',context)

##########################################   departments ###############################
# Departments
@login_required
def departments(request):
    department_list = Department.objects.all()
    context = {
        'page_title':'Departments',
        'departments':department_list,
    }
    return render(request, 'employee_information/departments.html',context)



@login_required
def manage_departments(request):
    department = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            department = Department.objects.filter(id=id).first()
    
    context = {
        'department' : department
    }
    return render(request, 'employee_information/manage_department.html',context)




@login_required
def save_department(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_department = Department.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],status = data['status'])
        else:
            save_department = Department(name=data['name'], description = data['description'],status = data['status'])
            save_department.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_department(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Department.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


    ##############################################################################################################

def save_customer(request):
    if request.method == 'POST':
        data = request.POST
        resp = {'status': 'failed'}

        try:
            if 'id' in data and data['id'].isnumeric() and int(data['id']) > 0:
                # Retrieve and update existing customer data
                cust = Customer.objects.get(pk=data['id'])
                cust.name = data['name']
                cust.email = data['email']
                cust.con = data['con']
                cust.address = data['address']
                cust.company_name = data['company_name']
                if 'stamp' in request.FILES:
                    cust.stamp = request.FILES['stamp']
                cust.status = data['status']
                cust.save()
            else:
                # Create a new customer
                new_cust = Customer(
                    name=data['name'],
                    email=data['email'],
                    con=data['con'],
                    address=data['address'],
                    company_name=data['company_name'],
                    status=data['status']
                )
                if 'stamp' in request.FILES:
                    new_cust.stamp = request.FILES['stamp']
                new_cust.save()
            
            resp['status'] = 'success'
        except Exception as e:
            print(e)  # Print exception for debugging purposes
            resp['status'] = 'failed'
        
        return JsonResponse(resp)  # Return JSON response
    else:
        return HttpResponse('Invalid request method')



# def save_customerrrr(request):
#     data =  request.POST
#     resp = {'status':'failed'}
#     try:
#         if (data['id']).isnumeric() and int(data['id']) > 0 :
#             save_cust = customer.objects.filter(id = data['id']).update(name=data['name'], email = data['email'], con=data['con'], address=data['address'], comapny_name=data['company_name'], stamp=data['stamp'],status = data['status'])
#         else:
#             save_cust = customer(name=data['name'],  email = data['email'], con=data['con'], address=data['address'], comapny_name=data['company_name'], stamp=data['stamp'],status = data['status'])
#             save_cust.save()
#         resp['status'] = 'success'
#     except:
#         resp['status'] = 'failed'
#     return HttpResponse(json.dumps(resp), content_type="application/json")

# from django.http import JsonResponse

def save_customer(request):
    resp = {'status': 'failed'}
    
    try:
        # Extract data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        con = request.POST.get('con')
        address = request.POST.get('address')
        company_name = request.POST.get('company_name')
        status = request.POST.get('status')
        stamp = request.FILES.get('stamp') if 'stamp' in request.FILES else None
        
        # Check if the ID exists and is valid
        if 'id' in request.POST and request.POST['id'].isnumeric() and int(request.POST['id']) > 0:
            cust = Customer.objects.get(id=request.POST['id'])
            cust.name = name
            cust.email = email
            cust.con = con
            cust.address = address
            cust.company_name = company_name
            if stamp:
                cust.stamp = stamp
            cust.status = status
            cust.save()
        else:
            # Create a new customer
            new_cust = Customer(
                name=name,
                email=email,
                con=con,
                address=address,
                company_name=company_name,
                status=status
            )
            if stamp:
                new_cust.stamp = stamp
            new_cust.save()
        
        resp['status'] = 'success'
    except Exception as e:
        print(e)  # Print exception for debugging purposes
        resp['status'] = 'failed'
    
    return JsonResponse(resp)

# def save_customerrrrrr(request):
#     data = request.POST
#     resp = {'status': 'failed'}
    
#     try:
#         if (data['id']).isnumeric() and int(data['id']) > 0 :

#             cust = Customer.objects.get(id=data['id'])
#             cust.name = data['name']
#             cust.email = data['email']
#             cust.con = data['con']
#             cust.address = data['address']
#             cust.company_name = data['company_name']
#             if 'stamp' in request.FILES:
#                 cust.stamp = request.FILES['stamp']
#             cust.status = data['status']
#             cust.save()
#         else:
           
#             new_cust = Customer(
#                 name=data['name'],
#                 email=data['email'],
#                 con=data['con'],
#                 address=data['address'],
#                 company_name=data['company_name'],
#                 status=data['status']
#             )
#             if 'stamp' in request.FILES:
#                 new_cust.stamp = request.FILES['stamp']
#             new_cust.save()   
#         resp['status'] = 'success'
#     except:
#         resp['status'] = 'failed'
#     return HttpResponse(json.dumps(resp), content_type="application/json")



#################################   Positions  ######################################

# Positions
@login_required
def positions(request):
    position_list = Position.objects.all()
    context = {
        'page_title':'Positions',
        'positions':position_list,
    }
    return render(request, 'employee_information/positions.html',context)


@login_required
def manage_positions(request):
    position = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            position = Position.objects.filter(id=id).first()
    
    context = {
        'position' : position
    }
    return render(request, 'employee_information/manage_position.html',context)


@login_required
def save_position(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_position = Position.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],status = data['status'])
        else:
            save_position = Position(name=data['name'], description = data['description'],status = data['status'])
            save_position.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")





@login_required
def delete_position(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Position.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


###############################################################################################

#                                           Vehicle Category
###############################################################################################

@login_required
def vehicle_Category(request):
    cat= Vehicle_Category.objects.all()
    cat_count=cat.count()
    # cat = Vehicle_Category.objects.all()
    context = {
        'page_title':'Vehicle Category',
        'Veh': cat,
        'cat_count': cat_count
    }
    return render(request, 'employee_information/vehicle_category.html',context)
##############################################    Expense Category #############################
@login_required
def expense_Category(request):
    expe= Expense_Category.objects.all()
   
    # cat = Vehicle_Category.objects.all()
    context = {
        'page_title':'Expense Category',
        'Expe': expe}
    return render(request, 'employee_information/expense_category.html',context)

##############################################    freight Category #############################

@login_required
def freight_Category(request):
    fr= Freight_Category.objects.all()
   
    # cat = Vehicle_Category.objects.all()
    context = {
        'page_title':'Freight Category',
        'freight': fr}
    return render(request, 'employee_information/freight_category.html',context)

##############################################    Commodity #############################
@login_required
def commodity(request):
    com= Commodity.objects.all()
   
    # cat = Vehicle_Category.objects.all()
    context = {
        'page_title':'Commodity',
        'Com': com}
    return render(request, 'employee_information/commodity.html',context)

##############################################    Carrier#############################
@login_required
def carrier(request):
    car= Carrier.objects.all()
   
    # cat = Vehicle_Category.objects.all()
    context = {
        'page_title':'Carrier',
        'Car': car}
    return render(request, 'employee_information/carrier.html',context)
##############################################   Vessel#############################
@login_required
def vessel(request):
    ves= Vessel.objects.all()
   
    # cat = Vehicle_Category.objects.all()
    context = {
        'page_title':'Vessel',
        'Ves': ves}
    return render(request, 'employee_information/vessel.html',context)
##############################################    Contract owner #############################
@login_required
def contract(request):
    con= Contract_owner.objects.all()
   
    # cat = Vehicle_Category.objects.all()
    context = {
        'page_title':'Contract',
        'Con': con}
    return render(request, 'employee_information/contract.html',context)
####################################################### vehicle ################################
@login_required
def vehicle(request):
    veh= Vehicle.objects.all()
    record_count = Vehicle.objects.count()
    cat = Vehicle_Category.objects.all()
    vehicles=veh.count()
    context = {
        'page_title':'Vehicle',
        'Vehi': veh,
        'vehicles': vehicles,
        'record_count': record_count
    }
    return render(request, 'employee_information/vehicle.html',context)

####################################################  Expense   ####################################



@login_required
def expense(request):
    exps= Expense.objects.all()
    veh = Vehicle.objects.count()
    expe = Expense_Category.objects.count()
    context = {
        'page_title':'Expense',
        'Vehi': veh,
        'Exp': exps,
         'Expe': expe,
    }
    return render(request, 'employee_information/expense.html',context)

#################################################    EMPLOYEEE ###########################################

@login_required
# Employees
def employees(request):
    employee_list = Employees.objects.all()
    context = {
        'page_title':'Employees',
        'employees':employee_list,
    }
    return render(request, 'employee_information/employees.html',context)
######################################################    AGENT ####################
@login_required

def agent(request):
    ag = Agent.objects.all()
    context = {
        'page_title':'Agent',
        'Ag':ag,
    }
    return render(request, 'employee_information/agent.html',context)

##########################################
@login_required
def curex(request):
    cur = Currency_exchange.objects.all()
    context = {
        'page_title':'Currency Exchange',
        'Cur':cur,
    }
    return render(request, 'employee_information/cur_ex.html',context)


###############################################################



@login_required
def set(request):
    set = Settlement.objects.all()
    context = {
        'page_title':'Settlement ',
        'Set':set,
    }
    return render(request, 'employee_information/set.html',context)
####################################################### VENDOR   ####################################
@login_required
def vendor(request):
    ven = Vendor.objects.all()
    context = {
        'page_title':'Vendor',
        'Ven':ven,
    }
    return render(request, 'employee_information/vendor.html',context)
@login_required
def booking(request):
    bok = Booking.objects.all()
    Com= Commodity.objects.all() 
    Ves= Vessel.objects.all() 
    Ag= Agent.objects.all() 
    Con= Contract_owner.objects.all() 
    freight= Freight_Category.objects.all() 
    Car= Carrier.objects.all() 
    Cust=Customer.objects.all()  
    context = {
        'page_title':'Booking',
        'Bok':bok,
           "Com" : Com ,
        "Ves" : Ves ,
        "Ag" : Ag ,
        "Con" : Con ,
        "freight" : freight ,
        "Car" : Car ,
        "Cust" : Cust
    }
    return render(request, 'employee_information/booking.html',context)

@login_required
def upd(request):
    Bok = Booking.objects.all()    
    upd = BookingUpdate.objects.all()
    Com= Commodity.objects.all() 
    Ves= Vessel.objects.all() 
    Ag= Agent.objects.all() 
    Con= Contract_owner.objects.all() 
    freight= Freight_Category.objects.all() 
    Car= Carrier.objects.all() 
    Cust=Customer.objects.all()  
    context = {
        'page_title':'Booking Update',
        'Bok':Bok,
           "Com" : Com ,
        "Ves" : Ves ,
        "Ag" : Ag ,
        "Con" : Con ,
        "freight" : freight ,
        "Car" : Car ,
        "Cust" : Cust,
        "Upd": upd
    }
    return render(request, 'employee_information/upd.html',context)
@login_required
def update(request):
     Bok = Booking.objects.all()
     ups = BookingUpdate.objects.all()
   
     context = {
        'page_title':'Tracker',
        'Ups':ups,
       " Bok":Bok
    }
     return render(request, 'employee_information/search_upd.html',context)



def get_booking_invoice(request):
    if request.method == 'POST':
        order_no = request.POST.get('order_no')
        booking_updates = Booking.objects.filter(order_no=order_no).values(
            'order_no', 'customer__name', 'Commodity__type', 'com', 'Pol', 'Pofd','amount',
            'Booking_date', 'Sailing_date', 'stamp'
        )

        booking_updates = list(booking_updates)
        for booking in booking_updates:
            booking['Booking_date'] = booking['Booking_date']
            booking['Sailing_date'] = booking['Sailing_date']
            booking['stamp'] = f"{settings.MEDIA_URL}{booking['stamp']}" 

        # print(booking_updates)  # Add this line to check the data
        
        request.session['booking_updates'] = json.dumps(booking_updates, cls=DjangoJSONEncoder)
        # print(request.session['booking_updates'])
        data = list(booking_updates)
        # print(data)
        return JsonResponse(data, safe=False)
    context = {
        'page_title': 'Booking invoice',
        'Bok': Booking.objects.all(),
        'Upd': BookingUpdate.objects.all()
    }
    return render(request, 'employee_information/bok_search.html', context)








from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from PIL import Image
from django.http import HttpResponse

def generate_booking_invoice(request):
    if request.method == 'POST':
        # Retrieve the JSON data from the session
        booking_updates_json = request.session.get('booking_updates')
        if not booking_updates_json:
            return HttpResponse("No record found.")
        
        # Convert the JSON back to a list of dictionaries
        booking_updates = json.loads(booking_updates_json)

        if not booking_updates:
            return HttpResponse("No record found.")

        # Retrieve the first record (assuming only one record will be retrieved from the search)
        booking_record = booking_updates[0]

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="booking_invoice.pdf"'

        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.setFont("Helvetica-Bold", 16)
        p.drawCentredString(300, 750, "LTV Tracking System")

# Add contact information
        p.setFont("Helvetica", 12)
        p.drawCentredString(300, 730, "Address: Karachi")  # Adjusted Y-coordinate
        p.drawCentredString(300, 710, "Email: ltv@gmail.com")  # Adjusted Y-coordinate
        p.drawCentredString(300, 690, "Phone: +92134567890")  # Adjusted Y-coordinate


        # Add heading for Booking Details
        p.setFillColorRGB(128, 0, 128)  # Purple color
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, 660, "Booking Details")

        # Table headers
        headers = ['Order No', 'Customer', 'Commodity', 'Company', 'POL', 'POFD','Amount', 'Booking Date', 'Delivery Date']
        col_widths = [60, 60, 65, 60, 60, 50,50, 95, 95]  # Widths for each column

        # Table data
        data = [
            [
                booking_record['order_no'],
                booking_record['customer__name'],
                booking_record['Commodity__type'],
                booking_record['com'],
                booking_record['Pol'],
                booking_record['Pofd'],
                booking_record['amount'],
                booking_record['Booking_date'],
                booking_record['Sailing_date'],
            ]
            # You can add more rows similarly based on your data structure
        ]

        # Creating a table from the data
        table = Table([headers] + data, colWidths=col_widths)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.purple),  # Purple header background
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),   # White header text
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),          # Center alignment for all cells
            ('BACKGROUND', (0, 1), (-1, -1), colors.white), # White background for data cells
            ('GRID', (0, 0), (-1, -1), 1, colors.purple)     # Table grid
        ]))

        # Drawing table on canvas
        table.wrapOn(p, 0, 0)
        table.drawOn(p, 50, 610)  # Adjust coordinates for table placement

        # Save the PDF content
        p.drawString(50, 30, f"Page 1")  # Change this accordingly based on the page number
        p.showPage()
        p.save()

        # Get the PDF content from the buffer
        pdf = buffer.getvalue()
        buffer.close()

        response.write(pdf)
        return response

    return HttpResponse("No method found.")






def generate_booking_invoicesss(request):
    if request.method == 'POST':
        # Retrieve the JSON data from the session
        booking_updates_json = request.session.get('booking_updates')
        if not booking_updates_json:
            return HttpResponse("No record found.")
        
        # Convert the JSON back to a list of dictionaries
        booking_updates = json.loads(booking_updates_json)

        if not booking_updates:
            return HttpResponse("No record found.")

        # Retrieve the first record (assuming only one record will be retrieved from the search)
        booking_record = booking_updates[0]

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="booking_invoice.pdf"'

        # Create a canvas
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.setFont("Helvetica-Bold", 16)
        p.drawCentredString(300, 750, "LTV Tracking System")

        # Add contact information
        p.setFont("Helvetica", 12)
        p.drawString(50, 730, "Address: Karachi")
        p.drawString(50, 710, "Email: ltv@gmail.com")
        p.drawString(50, 690, "Phone: +92134567890")

        # Add heading for Booking Details
        p.setFillColorRGB(128, 0, 128)  # Purple color
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, 660, "Booking Details")
        # Create the content for the PDF
        p.drawString(100, 750, f"Order No: {booking_record['order_no']}")
        p.drawString(100, 730, f"Customer: {booking_record['customer__name']}")
        p.drawString(100, 710, f"Commodity: {booking_record['Commodity__type']}")
        p.drawString(100, 690, f"Company: {booking_record['com']}")
        p.drawString(100, 670, f"POL: {booking_record['Pol']}")
        p.drawString(100, 650, f"POFD: {booking_record['Pofd']}")
        p.drawString(100, 630, f"Booking Date: {booking_record['Booking_date']}")
        p.drawString(100, 610, f"Delivery Date: {booking_record['Sailing_date']}")

        # Add the company stamp as an image
        stamp_url = booking_record['stamp']
        try:
            img = Image.open(stamp_url)
            x = 100  # Replace with the desired X-coordinate
            y = 590  # Replace with the desired Y-coordinate
            width = 200  # Replace with the desired width of the image
            height = 200 
            p.drawImage(img, x, y, width, height)  # Set x, y, width, height as needed
        except Exception as e:
            print(f"Error loading image: {e}")
            # Handle the case where the image couldn't be loaded

        p.setFont("Helvetica", 10)
        p.drawString(50, 30, f"Page 1")  # Change this accordingly based on the page number
        # Save the PDF content
        p.showPage()
        p.save()

        # Get the PDF content from the buffer
        pdf = buffer.getvalue()
        buffer.close()

        response.write(pdf)
        return response

    return HttpResponse("No method found.")



def get_booking_updates(request):
    Bok = Booking.objects.all()
   
    upd = BookingUpdate.objects.all()
    
    if request.method == 'POST':
        order_no = request.POST.get('order_no')
        booking_updates = BookingUpdate.objects.filter(booking__order_no=order_no).values('id', 'booking__order_no', 'des', 'updated_at')

        data = list(booking_updates)
        return JsonResponse(data, safe=False)

    # return JsonResponse([], safe=False)


    context = {
        'page_title': 'Booking Update',
        'Bok': Bok,
        
        'Upd': upd
    }
    return render(request, 'employee_information/search_upd.html', context)



# def get_booking_invoices(request):
#     bok = Booking.objects.all()
#     Upd = BookingUpdate.objects.all()
    
#     if request.method == 'POST':
#         order_no = request.POST.get('order_no')
#         booking_updates = Booking.objects.filter(order_no=order_no).values(
#             'order_no', 'customer__name', 'Commodity__type', 'com', 'Pol', 'Pofd',
#             'Booking_date', 'Sailing_date', 'stamp'
#         )

#         # Modify the stamp field value to contain the image URL path
#         for booking in booking_updates:
#             booking['stamp'] = f"{settings.MEDIA_URL}{booking['stamp']}"  # Assuming stamp contains the path
#         # request.session['booking_updates'] = list(booking_updates)
#         # data = list(booking_updates)
#         print(booking_updates)  
#         request.session['booking_updates'] = json.dumps(list(booking_updates))
#         data = list(booking_updates)
#         return JsonResponse(data, safe=False)

#     context = {
#         'page_title': 'Booking invoice',
#         'Bok': bok,
#         'Upd': Upd
#     }
#     return render(request, 'employee_information/bok_search.html', context)


# def generate_booking_invoice(request):
#          if request.method == 'POST':
#           order_no = request.POST.get('order_no')
#           booking_updates = Booking.objects.filter(order_no=order_no).values(
#             'order_no', 'customer__name', 'Commodity__type', 'com', 'Pol', 'Pofd',
#             'Booking_date', 'Sailing_date', 'stamp'
#         )

#         # Modify the stamp field value to contain the image URL path
#          for booking in booking_updates:
#             booking['stamp'] = f"{settings.MEDIA_URL}{booking['stamp']}"  # Assuming stamp contains the path

#          data = list(booking_updates)
#          booking_record = Booking.objects.filter(order_no=data).first()
#          if booking_record:
#           response = HttpResponse(content_type='application/pdf')
#           response['Content-Disposition'] = f'attachment; filename="booking_invoice.pdf"'

#         # Create a canvas
#          p = canvas.Canvas(response, pagesize=letter)

#         # Create the content for the PDF
#          p.drawString(100, 750, f"Booking Invoice for Order No: {booking_record.order_no}")
#          p.drawString(100, 730, f"Customer: {booking_record.customer.name}")
#          p.drawString(100, 710, f"Commodity: {booking_record.Commodity.type}")
#          p.drawString(100, 710, f"Company: {booking_record.com}")
#          p.drawString(100, 710, f"POL: {booking_record.Pol}")
#          p.drawString(100, 710, f"POFD: {booking_record.Pofd}")
#          p.drawString(100, 710, f"Booking Date: {booking_record.Booking_date}")
#          p.drawString(100, 710, f"Delivery Date: {booking_record.Sailing_date}")
#          # Add other details based on your Booking model fields

#         # Save the PDF content
#          p.showPage()
#          p.save()
#          return response

#         return HttpResponse("No record found.")



def search_booking(request):
    if request.method == 'POST' and request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        order_no = request.POST.get('order_no')
        # Filter Booking records based on order_no
        bookings = Booking.objects.filter(order_no=order_no).values(
            'order_no', 'customer__name', 'Commodity__type', 'com', 'Pol', 'Pofd',
            'Booking_date', 'Sailing_date', 'stamp', 'status'
        )
        # Convert QuerySet to list for JSON serialization
        booking_list = list(bookings)
        return JsonResponse(booking_list, safe=False)
    else:
        return render(request, 'employee_information/bok_search.html')



# def get_booking_updates(request):
#     Bok = Booking.objects.all()
#     Ups = BookingUpdate.objects.all()
#     if request.method == 'POST':
#         order_no = request.POST.get('order_no')
#         booking_updates = BookingUpdate.objects.filter(booking__order_no=order_no).values('id', 'booking__order_no', 'des', 'updated_at')

#         data = list(booking_updates)
#         return JsonResponse(data, safe=False)

#     return JsonResponse([], safe=False)









@login_required
def spe(request):
    Bok = Booking.objects.all()
    spe=Special_rate.objects.all()
    Com= Commodity.objects.all() 
    Ves= Vessel.objects.all() 
    Ag= Agent.objects.all() 
    Con= Contract_owner.objects.all() 
    freight= Freight_Category.objects.all() 
    Car= Carrier.objects.all() 
    Cust=Customer.objects.all()  
    context = {
        'page_title':'Special Rate',
         "Spe" : spe,
        'Bok':Bok,
           "Com" : Com ,
        "Ves" : Ves ,
        "Ag" : Ag ,
        "Con" : Con ,
        "freight" : freight ,
        "Car" : Car ,
        "Cust" : Cust
          
    }
    return render(request, 'employee_information/special.html',context)
@login_required
def bin(request):
    bin = Booking_invoice.objects.all()
    Bok = Booking.objects.all()
    Spe=Special_rate.objects.all()
    Com= Commodity.objects.all() 
    Set= Settlement.objects.filter(status = 1).all() 
    Ves= Vessel.objects.all() 
    Ag= Agent.objects.all() 
    Con= Contract_owner.objects.all() 
    freight= Freight_Category.objects.all() 
    Car= Carrier.objects.all() 
    Cust=Customer.objects.all()  
    context = {
        'page_title':'Booking Invoice',
        'Bok':Bok,
           "Com" : Com ,
        "Ves" : Ves ,
        "Ag" : Ag ,
        "Con" : Con ,
        "freight" : freight ,
        "Car" : Car ,
        "Cust" : Cust,
           "Spe" : Spe,
              "Bin" : bin,
              "Set":Set
    }
    return render(request, 'employee_information/bok_invoice.html',context)

@login_required
def consale(request):
    cns = Container_sale.objects.all()
    
    Vehi= Vehicle.objects.all() 
   
    Cust=Customer.objects.all()  
    context = {
        'page_title':'Container Sale',
        'Cns':cns,
        "Vehi" : Vehi,
      
        "Cust" : Cust
    }
    return render(request, 'employee_information/consale.html',context)


@login_required
def conpur(request):
    cnp = Container_purchase.objects.all()
    
    Vehi= Vehicle.objects.all() 
   
    Ven=Vendor.objects.all()  
    context = {
        'page_title':'Container Purchase',
        'Cnp':cnp,
        "Vehi" : Vehi,
      
        "Ven" : Ven
    }
    return render(request, 'employee_information/conpur.html',context)
@login_required
def rent(request):
    ren = lease_rental.objects.all()
    
    Vehi= Vehicle.objects.all() 
   
    Cust=Customer.objects.all()  
    context = {
        'page_title':'Rent',
        'Ren':ren,
        "Vehi" : Vehi,
      
        "Cust" : Cust
    }
    return render(request, 'employee_information/rent.html',context)




@login_required
def pursol(request):
    purs = Container_slot.objects.all()
    
    Set= Settlement.objects.all() 
   
    Vehi=Vehicle.objects.all()  
    context = {
        'page_title':' Purchase Slot',
        'Vehi':Vehi,
        "Set" : Set,
      
        "Purs" : purs
    }
    return render(request, 'employee_information/purslot.html',context)
########################################################   manage code       #####################################
@login_required
def manage_category(request):
    cat = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            cat = Vehicle_Category.objects.filter(id=id).first()
    
    context = {
        'cat' : cat
    }
    return render(request, 'employee_information/manage_category.html',context)
@login_required
def manage_consale(request):
    cns = {}
    Vehi= Vehicle.objects.filter(status = 1).all() 
    Cust=Customer.objects.filter(status = 1).all()  
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            cns = Container_sale.objects.filter(id=id).first()
    
    context = {
        'cns' : cns,   "Cust" : Cust,   "Vehi" : Vehi

    }
    return render(request, 'employee_information/manage_consale.html',context)
def manage_conpur(request):
    cnp = {}
    Vehi= Vehicle.objects.filter(status = 1).all() 
    Ven=Vendor.objects.filter(status = 1).all()  
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            cnp = Container_purchase.objects.filter(id=id).first()
    
    context = {
        'cnp' : cnp, 
            "Ven" : Ven,
                  "Vehi" : Vehi

    }
    return render(request, 'employee_information/manage_conpur.html',context)
def manage_rent(request):
    ren = {}
    Vehi= Vehicle.objects.filter(status = 1).all() 
    Cust=Customer.objects.filter(status = 1).all()  
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            ren = lease_rental.objects.filter(id=id).first()
    
    context = {
        'ren' : ren, 
            "Cust" : Cust,
                  "Vehi" : Vehi

    }
    return render(request, 'employee_information/manage_rent.html',context)
@login_required
def manage_pursol(request):
    purs = {}
    Set= Settlement.objects.filter(status = 1).all() 
    Vehi= Vehicle.objects.filter(status = 1).all()  
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            purs =Container_slot.objects.filter(id=id).first()
    
    context = {
        'Vehi' : Vehi,   "purs" : purs,   "Set" :Set

    }
    return render(request, 'employee_information/manage_purslot.html',context)
@login_required
def manage_curex(request):
    cur = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            cur = Currency_exchange.objects.filter(id=id).first()
    
    context = {
        'cur' : cur
    }
    return render(request, 'employee_information/manage_curex.html',context)
 

@login_required
def manage_expcategory(request):
    expe = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            expe = Expense_Category.objects.filter(id=id).first()
    
    context = {
        'expe' : expe
    }
    return render(request, 'employee_information/manage_expcategory.html',context)

@login_required
def manage_freightcategory(request):
    fr = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            fr = Freight_Category.objects.filter(id=id).first()
    
    context = {
        'fr' : fr
    }
    return render(request, 'employee_information/manage_freightcategory.html',context)

@login_required
def manage_comcategory(request):
    com = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            com = Commodity.objects.filter(id=id).first()
    
    context = {
        'com' : com
    }
    return render(request, 'employee_information/manage_commodity.html',context)

@login_required
def manage_concategory(request):
    con = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            con = Contract_owner.objects.filter(id=id).first()
    
    context = {
        'con' : con
    }
    return render(request, 'employee_information/manage_contract.html',context)




@login_required
def manage_carcategory(request):
    car = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            car= Carrier.objects.filter(id=id).first()
    
    context = {
        'car' : car
    }
    return render(request, 'employee_information/manage_carrier.html',context)

@login_required
def manage_vescategory(request):
    ves = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            ves = Vessel.objects.filter(id=id).first()
    
    context = {
        'ves' : ves
    }
    return render(request, 'employee_information/manage_vessel.html',context)




@login_required
def manage_vehicle(request):
    veh = {}
    Veh = Vehicle_Category.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            veh = Vehicle.objects.filter(id=id).first()
    
    context = {
        'veh' : veh,
        'Veh' : Veh
    }
    return render(request, 'employee_information/manage_vehicle.html',context)



@login_required
def manage_expense(request):
    exps = {}
    Expe = Expense_Category.objects.filter(status = 1).all() 
    Vehi =Vehicle.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            exps = Expense.objects.filter(id=id).first()
    
    context = {
        'exps' : exps,
        'Expe' : Expe,
        'Vehi': Vehi
    }
    return render(request, 'employee_information/manage_expense.html',context)


@login_required
def manage_employees(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
    return render(request, 'employee_information/manage_employee.html',context)
@login_required
def manage_customer(request):
    cust = {}
   
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            cust = Customer.objects.filter(id=id).first()
    context = {
      
        'cust' : cust
    }
    return render(request, 'employee_information/manage_customer.html',context)
@login_required
def manage_agent(request):
    ag = {}
   
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            ag = Agent.objects.filter(id=id).first()
    context = {
      
        'ag' : ag
    }
    return render(request, 'employee_information/manage_agent.html',context)

@login_required
def manage_booking(request):
    bok = {}
    Com= Commodity.objects.filter(status = 1).all() 
    Ves= Vessel.objects.filter(status = 1).all() 
    Ag= Agent.objects.filter(status = 1).all() 
    Con= Contract_owner.objects.filter(status = 1).all() 
    freight= Freight_Category.objects.filter(status = 1).all() 
    Car= Carrier.objects.filter(status = 1).all() 
    Cust=Customer.objects.filter(status = 1).all()  
        
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            bok = Booking.objects.filter(id=id).first()
    context = {
      
      
        "bok":bok,
        "Com" : Com ,
        "Ves" : Ves ,
        "Ag" : Ag ,
        "Con" : Con ,
        "freight" : freight ,
        "Car" : Car ,
        "Cust" : Cust
    }
    return render(request, 'employee_information/manage_booking.html',context)
@login_required
def manage_upd(request):
    upd = {}
    Com= Commodity.objects.filter(status = 1).all() 
    Bok= Booking.objects.filter(status = 1).all() 
    Ves= Vessel.objects.filter(status = 1).all() 
    Ag= Agent.objects.filter(status = 1).all() 
    Con= Contract_owner.objects.filter(status = 1).all() 
    freight= Freight_Category.objects.filter(status = 1).all() 
    Car= Carrier.objects.filter(status = 1).all() 
    Cust=Customer.objects.filter(status = 1).all()  
        
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            upd = BookingUpdate.objects.filter(id=id).first()
    context = {
      
      
        "Bok":Bok,
        "Com" : Com ,
        "Ves" : Ves ,
        "Ag" : Ag ,
        "Con" : Con ,
        "freight" : freight ,
        "Car" : Car ,
        "Cust" : Cust,
        "upd":upd
    }
    return render(request, 'employee_information/manage_upd.html',context)



@login_required
def manage_spe(request):
    spe = {}
    Bok= Booking.objects.filter(status = 1).all() 
    Set= Settlement.objects.filter(status = 1).all() 
    Com= Commodity.objects.filter(status = 1).all() 
    Ves= Vessel.objects.filter(status = 1).all() 
    Ag= Agent.objects.filter(status = 1).all() 
    Con= Contract_owner.objects.filter(status = 1).all() 
    freight= Freight_Category.objects.filter(status = 1).all() 
    Car= Carrier.objects.filter(status = 1).all() 
    Cust=Customer.objects.filter(status = 1).all()  
        
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            spe = Special_rate.objects.filter(id=id).first()
    context = {
      
      
        "Bok":Bok,
        "Com" : Com ,
        "Ves" : Ves ,
        "Ag" : Ag ,
        "Con" : Con ,
        "freight" : freight ,
        "Car" : Car ,
        "Cust" : Cust,
        " Set": Set,
               "spe" : spe
    }
    return render(request, 'employee_information/manage_special.html',context)



@login_required
def manage_bin(request):
    bin = {}
    Set= Settlement.objects.filter(status = 1).all() 
    Com= Commodity.objects.filter(status = 1).all() 
    Bok= Booking.objects.filter(status = 1).all() 
    Ves= Vessel.objects.filter(status = 1).all() 
    Ag= Agent.objects.filter(status = 1).all() 
    Con= Contract_owner.objects.filter(status = 1).all() 
    freight= Freight_Category.objects.filter(status = 1).all() 
    Car= Carrier.objects.filter(status = 1).all() 
    Cust=Customer.objects.filter(status = 1).all()  
        
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            bin = Booking_invoice.objects.filter(id=id).first()
    context = {
      
      
        "Bok":Bok,
        "Com" : Com ,
        "Ves" : Ves ,
        "Ag" : Ag ,
        "Con" : Con ,
        "freight" : freight ,
        "Car" : Car ,
        "Cust" : Cust,
        "bin" : bin,
         " Set": Set,

    }
    return render(request, 'employee_information/manage_bok_invoice.html',context)
@login_required
def manage_vendor(request):
    ven= {}
   
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            ven = Vendor.objects.filter(id=id).first()
    context = {
      
        'ven' : ven
    }
    return render(request, 'employee_information/manage_vendor.html',context)
@login_required
def manage_set(request):
    set= {}
   
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            set = Settlement.objects.filter(id=id).first()
    context = {
      
        'set' : set
    }
    return render(request, 'employee_information/manage_set.html',context)

##################################################### save code #############################
@login_required
def save_category(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_category = Vehicle_Category.objects.filter(id = data['id']).update(type=data['type'],status = data['status'])
        else:
            save_category = Vehicle_Category(type=data['type'], status = data['status'])
            save_category.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def save_expcategory(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_expcategory = Expense_Category.objects.filter(id = data['id']).update(type=data['type'],status = data['status'])
        else:
            save_expcategory = Expense_Category(type=data['type'], status = data['status'])
            save_expcategory.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
@login_required
# def save_curex(request):
#     data =  request.POST
#     resp = {'status':'failed'}
#     try:
#         if (data['id']).isnumeric() and int(data['id']) > 0 :
#             save_curex = Currency_exchange.objects.filter(id = data['id']).update(fom=data['fom'],to=data['to'], rate=data['rate'],  amount=data['amount'],  total=data['total'],status = data['status'])
#         else:
#             save_curex= Currency_exchange(fom=data['fom'],  to=data['to'], rate=data['rate'],  amount=data['amount'],   total=data['total'], status = data['status'])
#             save_curex.save()
#         resp['status'] = 'success'
#     except:
#         resp['status'] = 'failed'
#     return HttpResponse(json.dumps(resp), content_type="application/json")

def save_curex(request):
    data = request.POST
    resp = {'status': 'failed'}
    
    try:
        # if 'rate' in data and 'amount' in data:
        #     rate = float(data['rate']) if data['rate'] else 0
        #     amount = float(data['amount']) if data['amount'] else 0
        #     total = rate * amount
        #     data['total'] = total  # Assign the calculated total to the 'total' field

        if 'id' in data and data['id'].isnumeric() and int(data['id']) > 0:
            Currency_exchange.objects.filter(id=data['id']).update(
                fom=data['fom'],
                to=data['to'],
                rate=data['rate'],
                amount=data['amount'],
                total=data['total'],
                status=data['status']
            )
        else:
            curex = Currency_exchange(
                fom=data['fom'],
                to=data['to'],
                rate=data['rate'],
                amount=data['amount'],
                total=data['total'],
                status=data['status']
            )
            curex.save()
        resp['status'] = 'success'
    except ValidationError as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)
    except Exception as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)

    return JsonResponse(resp)
@login_required
def save_set(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_set = Settlement.objects.filter(id = data['id']).update(type=data['type'], status = data['status'])
        else:
            save_set= Settlement(type=data['type'],    status = data['status'])
            save_set.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
@login_required
def save_freightcategory(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_freight_categorycategory = Freight_Category.objects.filter(id = data['id']).update(type=data['type'],status = data['status'])
        else:
            save_freight_categorycategory = Freight_Category(type=data['type'], status = data['status'])
            save_freight_categorycategory.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def save_comcategory(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_com_category = Commodity.objects.filter(id = data['id']).update(type=data['type'],status = data['status'])
        else:
            save_com_category = Commodity(type=data['type'], status = data['status'])
            save_com_category.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def save_concategory(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_con_category = Contract_owner.objects.filter(id = data['id']).update(type=data['type'],status = data['status'])
        else:
            save_con_category = Contract_owner(type=data['type'], status = data['status'])
            save_con_category.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")




@login_required
def save_carcategory(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_car_category = Carrier.objects.filter(id = data['id']).update(type=data['type'],status = data['status'])
        else:
            save_car_category = Carrier(type=data['type'], status = data['status'])
            save_car_category.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def save_vescategory(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_ves_category = Vessel.objects.filter(id = data['id']).update(type=data['type'],status = data['status'])
        else:
            save_ves_category = Vessel(type=data['type'], status = data['status'])
            save_ves_category.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required

def save_vehicle(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Vehicle.objects.exclude(id = data['id']).filter(vehicle_number = data['vehicle_number'])
    else:
        check  = Vehicle.objects.filter(vehicle_number = data['vehicle_number'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Vehicle Number Already Exists'
    else:
        try:
            categ = Vehicle_Category.objects.filter(id=data['vehicle_id']).first()
         
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_vehicle = Vehicle.objects.filter(id = data['id']).update(vehicle_number=data['vehicle_number'], vehicle_id = categ,capacity=data['capacity'], size=data['size'],status = data['status'])
            else:
                save_vehicle = Vehicle(vehicle_number=data['vehicle_number'],vehicle_id = categ,capacity=data['capacity'],   size=data['size'],status = data['status'])
                save_vehicle.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({ "vehicle_number" : data['vehicle_number'], "vehicle_id" : data['vehicle_id'],"capacity" : data['capacity'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def save_expense(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Expense.objects.exclude(id = data['id']).filter(expense = data['expense'])
    else:
        check  = Expense.objects.filter(expense = data['expense'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Expense ID Already Exists'
    else:
        try:
            vehic = Vehicle.objects.filter(id=data['veh_id']).first()
            expo = Expense_Category.objects.filter(id=data['expense_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_expense = Expense.objects.filter(id = data['id']).update( expense=data['expense'],veh_id = vehic,expense_id = expo, amount=data['amount'],Description=data['Description'], date_added=data['date_added'], status = data['status'])                                                                
            else:
                save_expense = Expense(expense=data['expense'],veh_id = vehic,expense_id = expo, amount=data['amount'],Description=data['Description'], date_added=data['date_added'], status = data['status'])
                save_expense.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({ "expense" : data['expense'],  "expense_id " : data['expense_id '],  "veh_id" : data['veh_id']," amount" : data['amount'],  " Description" : data['Description'], " date_added" : data['date_added'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def save_employee(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Employees.objects.exclude(id = data['id']).filter(code = data['code'])
    else:
        check  = Employees.objects.filter(code = data['code'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            dept = Department.objects.filter(id=data['department_id']).first()
            pos = Position.objects.filter(id=data['position_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_employee = Employees.objects.filter(id = data['id']).update(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department_id = dept,position_id = pos,date_hired = data['date_hired'],salary = data['salary'],status = data['status'])
            else:
                save_employee = Employees(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department_id = dept,position_id = pos,date_hired = data['date_hired'],salary = data['salary'],status = data['status'])
                save_employee.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"code":data['code'], "firstname" : data['firstname'],"middlename" : data['middlename'],"lastname" : data['lastname'],"dob" : data['dob'],"gender" : data['gender'],"contact" : data['contact'],"email" : data['email'],"address" : data['address'],"department_id" : data['department_id'],"position_id" : data['position_id'],"date_hired" : data['date_hired'],"salary" : data['salary'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")
from django.core.exceptions import ValidationError


@login_required
def save_booking(request):
    resp = {'status': 'failed'}
    
    if request.method == 'POST':
        data = request.POST
        stamp_file = request.FILES.get('stamp')  # Retrieve the image file
        
        try:
            cust = Customer.objects.filter(id=data['customer']).first()
            comm = Commodity.objects.filter(id=data['Commodity']).first()
            car = Carrier.objects.filter(id=data['Carrier']).first()
            ves = Vessel.objects.filter(id=data['vessel']).first()
            con = Contract_owner.objects.filter(id=data['cntr_owner']).first()
            ag = Agent.objects.filter(id=data['agent']).first()
            fr = Freight_Category.objects.filter(id=data['freight']).first()
            order_no = data['order_no'] if data.get('order_no') else get_random_string(length=5, allowed_chars=string.ascii_letters + string.digits)

            
            if data.get('id').isnumeric() and int(data.get('id')) > 0:
                save_bok = Booking.objects.filter(id=data['id']).update(
                    ship=data['ship'],
                    Pol = data['Pol'],
                    Pofd = data['Pofd'],
                    Pot1 = data['Pot1'],
                    Pot2 = data['Pot2'],
                    amount = data['amount'],
                    pay = data['pay'],
                    # order_no = data['order_no'] if data.get('order_no') else get_random_string(length=5),  # Generating random string if order_no is not provided
                    
                    order_no = order_no,
                    Booking_date = data['Booking_date'],
                    Sailing_date = data['Sailing_date'],
                    com = data['com'],
                    # Other fields here...
                    stamp=stamp_file,  # Update the stamp field with the image file
                    customer=cust,  # Assign fetched customer object
                    Commodity=comm,  # Assign fetched commodity object
                    Carrier=car,  # Assign fetched carrier object
                    vessel=ves,  # Assign fetched vessel object
                    cntr_owner=con,  # Assign fetched contract owner object
                    agent=ag,  # Assign fetched agent object
                    freight=fr  # Assign fetched freight category object
                )  
            else:
                save_bok = Booking(
                    ship=data['ship'],
                    # Other fields here...
                  
                    Pol = data['Pol'],
                    Pofd = data['Pofd'],
                    Pot1 = data['Pot1'],
                    Pot2 = data['Pot2'],
                    order_no = order_no,
                    amount = data['amount'],
                    pay = data['pay'],
                    Booking_date = data['Booking_date'],
                    Sailing_date = data['Sailing_date'],
                    com = data['com'],
                   
                    stamp=stamp_file,  # Assign the image file to the stamp field
                    customer=cust,  # Assign fetched customer object
                    Commodity=comm,  # Assign fetched commodity object
                    Carrier=car,  # Assign fetched carrier object
                    vessel=ves,  # Assign fetched vessel object
                    cntr_owner=con,  # Assign fetched contract owner object
                    agent=ag,  # Assign fetched agent object
                    freight=fr  # Assign fetched freight category object
                )
             
                save_bok.save()   

            resp['status'] = 'success'
        except ValidationError as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)
        except Exception as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)

    return JsonResponse(resp)



@login_required
def save_upd(request):
      resp = {'status': 'failed'}
    
      if request.method == 'POST':
        data = request.POST
        
        # stamp_file = request.FILES.get('stamp')  # Retrieve the image file
        
        try:
            bok = Booking.objects.filter(id=data['booking']).first()
         
            if data.get('id').isnumeric() and int(data.get('id')) > 0:
                save_upd = BookingUpdate.objects.filter(id=data['id']).update(
                  
                    des= data['des'],
                   updated_at= data['updated_at'],
                   booking=bok,
                   
                )
            else:
                save_upd = BookingUpdate(
                  
                  
                    des= data['des'],
                   updated_at= data['updated_at'],
                   booking=bok,
                   
                )
                save_upd.save()

            resp['status'] = 'success'
        except ValidationError as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)
        except Exception as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)

      return JsonResponse(resp)












@login_required
def save_bookingg(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        bok  = Booking.objects.exclude(id = data['id']).filter(order_no = data['order_no'])
    else:
        bok  = Booking.objects.filter(order_no = data['order_no'])

    if len(bok) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Booking Already Exists'
    else:
        try:
            cust = Customer.objects.filter(id=data['cust_id']).first()
            comm = Commodity.objects.filter(id=data['com_id']).first()
            car = Carrier.objects.filter(id=data['car_id']).first()
            ves = Vessel.objects.filter(id=data['ves_id']).first()
            con = Contract_owner.objects.filter(id=data['con_id']).first()
            ag = Agent.objects.filter(id=data['ag_id']).first()
            fr = Freight_Category.objects.filter(id=data['fr_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_bok= Booking.objects.filter(id = data['id']).update(Shipper=data['Shipper'], Pol = data['Pol'],Pofd = data['Pofd'],Pot1 = data['Pot1'],Pot2 = data['Pot2'],order_no = data['order_no'],Booking_date = data['Booking_date'],Sailing_date = data['Sailing_date'],com = data['com'],customer = cust,Commodity= comm,    Carrier = car,    freight = fr,  vessel = ves, cntr_owner = con, agent = ag, stamp = data['stamp'],status = data['status'])
            else:
                save_bok = Booking(Shipper=data['Shipper'], Pol = data['Pol'],Pofd = data['Pofd'],Pot1 = data['Pot1'],Pot2 = data['Pot2'],order_no= data['order_no'],Booking_date = data['Booking_date'],Sailing_date = data['Sailing_date'],com= data['com'],customer = cust,Commodity = comm,     Carrier = car,     freight = fr,     vessel = ves,  cntr_owner = con,    agent = ag,  stamp = data['stamp'],status = data['status'])
                save_bok.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
           
    return HttpResponse(json.dumps(resp), content_type="application/json")






def save_agent(request):
    data = request.POST
    resp = {'status': 'failed'}
    
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :

            ag = Agent.objects.get(id=data['id'])
            ag.name = data['name']
            ag.email = data['email']
            ag.con = data['con']
            ag.address = data['address']
           
            ag.status = data['status']
            ag.save()
        else:
           
            new_ag = Agent(
                name=data['name'],
                email=data['email'],
                con=data['con'],
                address=data['address'],
              
                status=data['status']
            )
           
            new_ag.save()   
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
def save_vendor(request):
    data = request.POST
    resp = {'status': 'failed'}
    
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :

            ven = Vendor.objects.get(id=data['id'])
            ven.name = data['name']
            ven.email = data['email']
            ven.con = data['con']
            ven.address = data['address']
           
            ven.status = data['status']
            ven.save()
        else:
           
            new_ven = Vendor(
                name=data['name'],
                email=data['email'],
                con=data['con'],
                address=data['address'],
              
                status=data['status']
            )
           
            new_ven.save()   
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")




@login_required
def save_spe(request):
    resp = {'status': 'failed'}
    
    if request.method == 'POST':
        data = request.POST

        
        try:
            cust = Customer.objects.filter(id=data['customer']).first()
            comm = Commodity.objects.filter(id=data['Commodity']).first()
           
           
            ag = Agent.objects.filter(id=data['agent']).first()
            fr = Freight_Category.objects.filter(id=data['freight']).first()
            # bok = Booking.objects.filter(id=data['']).first()
            
            
            if data.get('id').isnumeric() and int(data.get('id')) > 0:
                save_spe = Special_rate.objects.filter(id=data['id']).update(
                    ship=data['ship'],
                    Pol = data['Pol'],
                    Pofd = data['Pofd'],
                   Pol2 = data['Pol2'],
                    Pofd2 = data['Pofd2'],
                    rate = data['rate'],
                    tra_date = data['tra_date'],
                    tan_exp = data['tan_exp'],
                    det = data['det'],
                    # Other fields here...
                  
                    customer=cust,  # Assign fetched customer object
                    Commodity=comm,  # Assign fetched commodity object
                  
                    agent=ag,  # Assign fetched agent object
                    freight=fr  # Assign fetched freight category object
                )
            else:
                save_spe = Special_rate(
                       ship=data['ship'],
                    Pol = data['Pol'],
                    Pofd = data['Pofd'],
                   Pol2 = data['Pol2'],
                    Pofd2 = data['Pofd2'],
                    rate = data['rate'],
                    tra_date = data['tra_date'],
                    tan_exp = data['tan_exp'],
                    det = data['det'],
                    # Other fields here...
                  
                    customer=cust,  # Assign fetched customer object
                    Commodity=comm,  # Assign fetched commodity object
                  
                    agent=ag,  # Assign fetched agent object
                    freight=fr  # Assign fetched freight category object
                )
                save_spe.save()

            resp['status'] = 'success'
        except ValidationError as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)
        except Exception as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)

    return JsonResponse(resp)




@login_required
def save_bin(request):
    resp = {'status': 'failed'}
    
    if request.method == 'POST':
        data = request.POST
        stamp_file = request.FILES.get('stamp')  # Retrieve the image file
        
        try:
            bok = Booking.objects.filter(id=data['sale_id']).first()
            cust = Customer.objects.filter(id=data['customer']).first()
         
            
            if data.get('id').isnumeric() and int(data.get('id')) > 0:
                save_bin = Booking_invoice.objects.filter(id=data['id']).update(
                    com=data['com'],
                    port = data['port'],
                    amount = data['amount'],
                    payment_center = data['payment_center'],
                    invoice_date= data['invoice_date'],
                    trans_date = data['trans_date'],
                   
                    # Other fields here...
                    stamp=stamp_file,  # Update the stamp field with the image file
                    customer=cust,  # Assign fetched customer object
                    sale_id=bok,  # Assign fetched customer object
                  
                )
            else:
                  save_bin = Booking_invoice.objects.filter(id=data['id']).update(
                    com=data['com'],
                    port = data['port'],
                    amount = data['amount'],
                    payment_center = data['payment_center'],
                    invoice_date= data['invoice_date'],
                    trans_date = data['trans_date'],
                   
                    # Other fields here...
                    stamp=stamp_file,  # Update the stamp field with the image file
                    customer=cust,  # Assign fetched customer object
                    sale_id=bok,  # Assign fetched customer object
                   
                )
            save_bin.save()

            resp['status'] = 'success'
        except ValidationError as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)
        except Exception as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)

    return JsonResponse(resp)











@login_required
def save_consale(request):
    resp = {'status': 'failed'}
    
    if request.method == 'POST':
        data = request.POST
       
        
        try:
            cust = Customer.objects.filter(id=data['customer']).first()
            veh = Vehicle.objects.filter(id=data['Cont_id']).first()
           
            
            
            if data.get('id').isnumeric() and int(data.get('id')) > 0:
                save_consale = Container_sale.objects.filter(id=data['id']).update(
                    Sale_price=data['Sale_price'],
                    Sale_date = data['Sale_date'],
                  
                 
                    # Other fields here...
                  
                    customer=cust,  # Assign fetched customer object
                    Cont_id=veh,  # Assign fetched commodity object
                  
                )
            else:
                save_consale = Container_sale(
                   Sale_price=data['Sale_price'],
                    Sale_date = data['Sale_date'],
                  
           
                  
                    customer=cust,  # Assign fetched customer object
                    Cont_id=veh,  # Assign fetched commodity object
                   
                )
                save_consale.save()

            resp['status'] = 'success'
        except ValidationError as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)
        except Exception as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)

    return JsonResponse(resp)


@login_required
def save_conpur(request):
    resp = {'status': 'failed'}
    
    if request.method == 'POST':
        data = request.POST
       
        
        try:
            ven = Vendor.objects.filter(id=data['vens']).first()
            vehi = Vehicle.objects.filter(id=data['Con_id']).first()
           
            
            
            if data.get('id').isnumeric() and int(data.get('id')) > 0:
                save_conpur = Container_purchase.objects.filter(id=data['id']).update(
                    purchase_price=data['purchase_price'],
                    idd=data['idd'],
                    purchase_date = data['purchase_date'],
                  
                 
                    # Other fields here...
                  
                    vens=ven,  # Assign fetched customer object
                    Con_id=vehi,  # Assign fetched commodity object
                  
                )
            else:
                save_conpur = Container_purchase(
                   purchase_price=data['purchase_price'],
                    purchase_date = data['purchase_date'],
                     idd=data['idd'],
           
                  
                    vens=ven,  # Assign fetched customer object
                    Con_id=vehi,  # Assign fetched commodity object
                   
                )
                save_conpur.save()

            resp['status'] = 'success'
        except ValidationError as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)
        except Exception as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)

    return JsonResponse(resp)
@login_required
def save_rent(request):
    resp = {'status': 'failed'}
    
    if request.method == 'POST':
        data = request.POST
       
        
        try:
            cust = Customer.objects.filter(id=data['buyer']).first()
            vehi = Vehicle.objects.filter(id=data['con_id']).first()
           
            
            
            if data.get('id').isnumeric() and int(data.get('id')) > 0:
                save_rent= lease_rental.objects.filter(id=data['id']).update(
                   rent_start=data['rent_start'],
                    rent_end = data['rent_end'],
                     amount=data['amount'],
           
                  
                    buyer=cust,  # Assign fetched customer object
                    con_id=vehi,  # Assign fetched commodity object
                  
                )
            else:
                save_rent = lease_rental(
                   rent_start=data['rent_start'],
                    rent_end = data['rent_end'],
                     amount=data['amount'],
           
                  
                    buyer=cust,  # Assign fetched customer object
                    con_id=vehi,  # Assign fetched commodity object
                   
                )
                save_rent.save()

            resp['status'] = 'success'
        except ValidationError as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)
        except Exception as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)

    return JsonResponse(resp)

@login_required
def save_pursol(request):
    resp = {'status': 'failed'}
    
    if request.method == 'POST':
        data = request.POST
       
        
        try:
            vehi = Vehicle.objects.filter(id=data['con_id']).first()
            set = Settlement.objects.filter(id=data['set_type']).first()
           
            
            
            if data.get('id').isnumeric() and int(data.get('id')) > 0:
                save_pursol = Container_slot.objects.filter(id=data['id']).update(
                    slot_start=data['slot_start'],
                  slot_end = data['slot_end'],
                   rate = data['rate'],
                  
                 
                    # Other fields here...
                  
                    set_type=set,  # Assign fetched customer object
                     con_id=vehi,   # Assign fetched commodity object
                  
                )
            else:
                save_pursol = Container_slot(
                  slot_start=data['slot_start'],
                  slot_end = data['slot_end'],
                   rate = data['rate'],
                  
                  
           
                  
                    set_type=set,  # Assign fetched customer object
                     con_id=vehi,  # Assign fetched commodity object
                   
                )
                save_pursol.save()

            resp['status'] = 'success'
        except ValidationError as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)
        except Exception as e:
            resp['status'] = 'failed'
            resp['msg'] = str(e)

    return JsonResponse(resp)

################################################### Delete COODE ###############################

@login_required
def delete_expcategory(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Expense_Category.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_set(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Settlement.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")





@login_required
def delete_curex(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Currency_exchange.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
@login_required
def delete_consale(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Container_sale.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
@login_required
def delete_conpur(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Container_purchase.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
    
@login_required
def delete_rent(request):
    data =  request.POST
    resp = {'status':''}
    try:
        lease_rental.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
    
@login_required
def delete_pursol(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Container_slot.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
@login_required
def delete_set(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Settlement.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
@login_required
def delete_freightcategory(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Freight_Category.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
@login_required
def delete_category(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Vehicle_Category.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
@login_required
def delete_comcategory(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Commodity.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_carcategory(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Carrier.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_concategory(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Contract_owner.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_vescategory(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Vessel.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_vehicle(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Vehicle.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_expense(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Expense.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")





@login_required
def delete_employee(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Employees.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_customer(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Customer.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_booking(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Booking.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
@login_required
def delete_upd(request):
    data =  request.POST
    resp = {'status':''}
    try:
        BookingUpdate.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_agent(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Agent.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
@login_required
def delete_vendor(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Vendor.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_spe(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Special_rate.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
@login_required
def delete_bin(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Booking_invoice.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")
############################################################ VIEW CODE ####################################
@login_required
def view_vehicle(request):
    veh = {}
    Veh = Vehicle_Category.objects.filter(status = 1).all() 
   
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            veh = Vehicle.objects.filter(id=id).first()
    context = {
        'veh' : veh,
       
        'Veh' : Veh
    }
    return render(request, 'employee_information/view_vehicle.html',context)


@login_required
def view_expense(request):
    exps = {}
    Expe = Expense_Category.objects.filter(status = 1).all() 
    Vehi = Vehicle.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            exps = Expense.objects.filter(id=id).first()
    context = {
        'Vehi' : Vehi,
       
        'Expe' : Expe,
        "exps":exps
    }
    return render(request, 'employee_information/view_expense.html',context)
@login_required
def view_freight_category(request):
    fr = {}
    fr = Freight_Category.objects.filter(status = 1).all() 

    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            fr = Freight_Category.objects.filter(id=id).first()
    context = {
        
        
        "fr":fr
    }
    return render(request, 'employee_information/view_freight_category.html',context)



@login_required
def view_contract(request):
    con= {}
    con= Contract_owner.objects.filter(status = 1).all() 

    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            con = Contract_owner.objects.filter(id=id).first()
    context = {
        
        
        "con":con
    }
    return render(request, 'employee_information/view_contract.html',context)

@login_required
def view_set(request):
    set= {}
    set= Settlement.objects.filter(status = 1).all() 

    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            set =Settlement.objects.filter(id=id).first()
    context = {
        
        
        "set":set
    }
    return render(request, 'employee_information/view_set.html',context)




@login_required
def view_customer(request):
    cust= {}
    cust= Customer.objects.filter(status = 1).all() 

    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            cust = Customer.objects.filter(id=id).first()
    context = {
        
        
        "cust":cust
    }
    return render(request, 'employee_information/view_customer.html',context)



@login_required
def view_agent(request):
    ag= {}
    ag= Agent.objects.filter(status = 1).all() 

    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            ag = Agent.objects.filter(id=id).first()
    context = {
        
        
        "ag":ag
    }
    return render(request, 'employee_information/view_agent.html',context)




@login_required
def view_vendor(request):
    ven= {}
    ven= Vendor.objects.filter(status = 1).all() 

    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            ven = Vendor.objects.filter(id=id).first()
    context = {
        
        
        "ven":ven
    }
    return render(request, 'employee_information/view_vendor.html',context)

@login_required
def view_booking(request):
    bok= {}
    bok= Booking.objects.filter(status = 1).all() 
    Com= Commodity.objects.filter(status = 1).all() 
    Ves= Vessel.objects.filter(status = 1).all() 
    Ag= Agent.objects.filter(status = 1).all() 
    Con= Contract_owner.objects.filter(status = 1).all() 
    freight= Freight_Category.objects.filter(status = 1).all() 
    Car= Carrier.objects.filter(status = 1).all() 
    Cust=Customer.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            bok = Booking.objects.filter(id=id).first()
    context = {
        
        
        "bok":bok,
        "Com" : Com ,
        "Ves" : Ves ,
        "Ag" : Ag ,
        "Con" : Con ,
        "freight" : freight ,
        "Car" : Car ,
        "Cust" : Cust

    }
    return render(request, 'employee_information/view_booking.html',context)

@login_required
def view_upd(request):
    upd= {}
    Bok= Booking.objects.filter(status = 1).all() 
    upd= BookingUpdate.objects.filter(status = 1).all() 
    Com= Commodity.objects.filter(status = 1).all() 
    Ves= Vessel.objects.filter(status = 1).all() 
    Ag= Agent.objects.filter(status = 1).all() 
    Con= Contract_owner.objects.filter(status = 1).all() 
    freight= Freight_Category.objects.filter(status = 1).all() 
    Car= Carrier.objects.filter(status = 1).all() 
    Cust=Customer.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            upd = BookingUpdate.objects.filter(id=id).first()
    context = {
        
        
        "Bok":Bok,
        "Com" : Com ,
        "Ves" : Ves ,
        "Ag" : Ag ,
        "Con" : Con ,
        "freight" : freight ,
        "Car" : Car ,
        "Cust" : Cust,
        "upd":upd

    }
    return render(request, 'employee_information/view_upd.html',context)




@login_required
def view_spe(request):
    spe= {}
    spe= Special_rate.objects.filter(status = 1).all() 
    Com= Commodity.objects.filter(status = 1).all() 
    Ves= Vessel.objects.filter(status = 1).all() 
    Ag= Agent.objects.filter(status = 1).all() 
    Con= Contract_owner.objects.filter(status = 1).all() 
    freight= Freight_Category.objects.filter(status = 1).all() 
    Car= Carrier.objects.filter(status = 1).all() 
    Cust=Customer.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            spe = Special_rate.objects.filter(id=id).first()
    context = {
        
        
        "spe":spe,
        "Com" : Com ,
        "Ves" : Ves ,
        "Ag" : Ag ,
        "Con" : Con ,
        "freight" : freight ,
        "Car" : Car ,
        "Cust" : Cust

    }
    return render(request, 'employee_information/view_spe.html',context)

@login_required
def view_bin(request):
    bin= {}
    bin= Booking_invoice.objects.filter(status = 1).all()
    Set= Settlement.objects.filter(status = 1).all()
    Bok= Booking.objects.filter(status = 1).all() 
    Com= Commodity.objects.filter(status = 1).all() 
    Ves= Vessel.objects.filter(status = 1).all() 
    Ag= Agent.objects.filter(status = 1).all() 
    Con= Contract_owner.objects.filter(status = 1).all() 
    freight= Freight_Category.objects.filter(status = 1).all() 
    Car= Carrier.objects.filter(status = 1).all() 
    Cust=Customer.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            bin = Booking_invoice.objects.filter(id=id).first()
    context = {
        
        
        "Bok":Bok,
        "Com" : Com ,
        "Ves" : Ves ,
        "Ag" : Ag ,
        "Con" : Con ,
        "freight" : freight ,
        "Car" : Car ,
        "Cust" : Cust,
          "bin" : bin,
          "Set": Set,


    }
    return render(request, 'employee_information/view_bok_invoice.html',context)



@login_required
def view_consale(request):
    
 
    cns= {}
   
    cns= Container_sale.objects.filter(status = 1).all() 
    
    Vehi=Vehicle.objects.filter(status = 1).all() 
    Cust=Customer.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            cns = Container_sale.objects.filter(id=id).first()
    context = {
        
        
      
        "cns" : cns ,
       
        "Vehi" :Vehi,
        "Cust": Cust

    }
    return render(request, 'employee_information/view_consale.html',context)


@login_required
def view_conpur(request):
 
    cnp= {}
   
    cnp= Container_purchase.objects.filter(status = 1).all() 
    
    Vehi=Vehicle.objects.filter(status = 1).all() 
    Ven=Vendor.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            cnp = Container_purchase.objects.filter(id=id).first()
    context = {
        
        
      
        "cnp" : cnp ,
       
        "Vehi" :Vehi,
        "Ven": Ven

    }
    return render(request, 'employee_information/view_conpur.html',context)

@login_required
def view_rent(request):
 
    ren= {}
   
    ren= lease_rental.objects.filter(status = 1).all() 
    
    Vehi=Vehicle.objects.filter(status = 1).all() 
    Cust=Customer.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            ren = lease_rental.objects.filter(id=id).first()
    context = {
        
        
      
        "ren" : ren ,
       
        "Vehi" :Vehi,
        "Cust": Cust

    }
    return render(request, 'employee_information/view_rent.html',context)


@login_required
def view_pursol(request):
    
 
    purs= {}
   
    purs= Container_slot.objects.filter(status = 1).all() 
    
    Set=Settlement.objects.filter(status = 1).all() 
    Vehi=Vehicle.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            purs =Container_slot.objects.filter(id=id).first()
    context = {
        
        
      
        "purs" : purs ,
       
        "Set" :Set,
        "Vehi": Vehi

    }
    return render(request, 'employee_information/view_purslot.html',context)




@login_required
def view_commodity(request):
    com= {}
    com= Commodity.objects.filter(status = 1).all() 

    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            com = Commodity.objects.filter(id=id).first()
    context = {
        
        
        "com":com
    }
    return render(request, 'employee_information/view_commodity.html',context)
@login_required
def view_curex(request):
    cur= {}
    cur= Currency_exchange.objects.filter(status = 1).all() 

    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            cur = Currency_exchange.objects.filter(id=id).first()
    context = {
        
        
        "cur":cur
    }
    return render(request, 'employee_information/view_curex.html',context)


@login_required
def view_carrier(request):
    car= {}
    car= Carrier.objects.filter(status = 1).all() 

    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            car = Carrier.objects.filter(id=id).first()
    context = {
        
        
        "car":car
    }
    return render(request, 'employee_information/view_carrier.html',context)



@login_required
def view_vessel(request):
    ves= {}
    ves= Vessel.objects.filter(status = 1).all() 

    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            ves = Vessel.objects.filter(id=id).first()
    context = {
        
        
        "ves":ves
    }
    return render(request, 'employee_information/view_vessel.html',context)


@login_required
def view_employee(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
    return render(request, 'employee_information/view_employee.html',context)

from django.shortcuts import render
from django.http import JsonResponse
from .models import Expense

################################################### CSV CODE ##############################################

def vehicle_csv(request):
  response= HttpResponse(content_type='text/csv')
  response['content-Disposition']='attachment; filename=Vehicle' + \
   str (datetime.datetime.now())+ '.csv'
   #  font_style=csv.XFStyle()
   #  font_style.font.bold=True
  wr=csv.writer(response)
  wr.writerow(['Container DETAILS'])
  wr.writerow(['ID', 'Container Number','Type','Capacity','Size']) 
  veh=Vehicle.objects.all()
  for veh in veh:
   wr.writerow([veh.id,veh.vehicle_number,veh.vehicle_id.type,veh.capacity, veh.size])
  return response
def bok_csv(request):
  response= HttpResponse(content_type='text/csv')
  response['content-Disposition']='attachment; filename=booking' + \
   str (datetime.datetime.now())+ '.csv'
   #  font_style=csv.XFStyle()
   #  font_style.font.bold=True
  wr=csv.writer(response)
  wr.writerow(['Booking DETAILS'])
  wr.writerow(['ID', 'Order No','Customer','Commodity','Company','Pol','Pofd','Amount','Booking date','Delivery Date']) 
  bok=Booking.objects.all()
  for bok in bok:
   wr.writerow([bok.id,bok.order_no,bok.customer.name,bok.Commodity.type,bok.com, bok.Pol , bok.Pofd,bok.amount,bok.Booking_date, bok.Sailing_date])
  return response

############################################ PDF CODE  ##########################################
def  vehicle_pdf(request):


     veh=Vehicle.objects.all()
     context = {'veh':veh}

     html_string = render_to_string('employee_information/veh_pdf.html', context)
     html = HTML(string=html_string, base_url=request.build_absolute_uri())
     pdf = html.write_pdf()

     response= HttpResponse(pdf, content_type='application/pdf')
     response['content-Disposition']='initials; attachment; filename=Vehicle' + \
      str (datetime.datetime.now())+ '.pdf'
     response['content-Transfer-Encoding'] ='binary'

     return response
def bok_pdfff(request, order_no):
    # Filter Booking records based on order_no
    bok = Booking.objects.filter(order_no=order_no)
    context = {'Bok': bok}

    html_string = render_to_string('employee_information/bok_pdf.html', context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['content-Disposition'] = 'initials; attachment; filename=Booking' + str(datetime.datetime.now()) + '.pdf'
    response['content-Transfer-Encoding'] = 'binary'

    return response
def  bok_pdf(request):


     bok=Booking.objects.all()
     context = {'Bok':bok}

     html_string = render_to_string('employee_information/bok_pdf.html', context)
     html = HTML(string=html_string, base_url=request.build_absolute_uri())
     pdf = html.write_pdf()

     response= HttpResponse(pdf, content_type='application/pdf')
     response['content-Disposition']='initials; attachment; filename=Booking' + \
      str (datetime.datetime.now())+ '.pdf'
     response['content-Transfer-Encoding'] ='binary'

     return response



#################################################### CHART CODE #####################################

from django.db.models import Sum
def expense_chart (request):
    categories = Expense_Category.objects.all()
    category_names = [category.type for category in categories]
    expense_sums = []

    for category in categories:
        total_expense = Expense.objects.filter(expense_id=category).aggregate(Sum('amount'))['amount__sum'] or 0
        expense_sums.append(float(total_expense))  # 

    data = {
        'category_names': category_names,
        'expense_sums': expense_sums,
    }
    return render(request, 'employee_information/charts.html', {'data': json.dumps(data)})

@login_required
def con_menu (request):
    expenses = Expense.objects.all()
    exp_count=expenses.count()
    expn=Expense_Category.objects.all()


    category_sums = Expense.objects.values('expense_id__type').annotate(sum_amount=Sum('amount'))
    sales = Container_sale.objects.all()

    

    # Extracting customer names and sale prices
    customers = [sale.customer.name for sale in sales]
    sale_prices = [sale.Sale_price for sale in sales]

    # Calculating count of total customers and sum of all sale prices
    total_customers = len(customers)  # Count unique customers
    total_sale_price = sum(sale_prices)

    
      
    
    context = {
        'expenses': expenses,
         'expen': expn,
        ' exp_count': exp_count,
        'category_sums': category_sums,
          'customers': json.dumps(customers),
        'sale_prices': json.dumps(sale_prices),
        'total_customers': total_customers,
        'total_sale_price': total_sale_price
       
    }
    return render(request, 'employee_information/container_menue.html', context)
def vehicle_chart (request):
    categories = Vehicle_Category.objects.all()
    category_names = [category.type for category in categories]
    vehicle_counts = []

    for category in categories:
        count = Vehicle.objects.filter(vehicle_id=category).count()
        vehicle_counts.append(count)

    data = {
        'category_names': category_names,
        'vehicle_counts': vehicle_counts,
    }
    return render(request, 'employee_information/vehicle_menu.html', {'data': json.dumps(data)})

def log_cat(request):
    Cust = Customer.objects.all()
    orders_data = Booking.objects.all().values('customer__name').annotate(total=Count('id'), total_amount=Sum('amount'))

    labels = []
    order_count = []
    amount_sum = []

    for entry in orders_data:
        labels.append(entry['customer__name'])
        order_count.append(entry['total'])
        amount_sum.append(entry['total_amount'])

    context = {
        'labels': labels,
        'order_count': order_count,
        'amount_sum': amount_sum,
        'Cust':Cust,
        'employees':employees,
     
        'total_employee':len(Carrier.objects.all()),
         'total_veh':len(Freight_Category.objects.all()),
         'total_cat':len(Vessel.objects.all()),
            'total_exp':len(Contract_owner.objects.all()),
         'total_set':len(Settlement.objects.all()),\
              'total_cur':len(Currency_exchange.objects.all()),
    }
    return render(request, 'employee_information/log-cat.html', context)
def emp_cat(request):
    Cust = Customer.objects.all()
    orders_data = Booking.objects.all().values('customer__name').annotate(total=Count('id'), total_amount=Sum('amount'))

    labels = []
    order_count = []
    amount_sum = []

    for entry in orders_data:
        labels.append(entry['customer__name'])
        order_count.append(entry['total'])
        amount_sum.append(entry['total_amount'])

    context = {
        'labels': labels,
        'order_count': order_count,
        'amount_sum': amount_sum,
        'Cust':Cust,
        'employees':employees,
     
        'total_employee':len(Department.objects.all()),
         'total_veh':len(Employees.objects.all()),
         'total_cat':len(Position.objects.all()),
          
    }
    return render(request, 'employee_information/emp-men.html', context)

from django.db.models import Count, Sum
def bok_chart(request):
    Cust = Customer.objects.all()
    orders_data = Booking.objects.all().values('customer__name').annotate(total=Count('id'), total_amount=Sum('amount'))

    labels = []
    order_count = []
    amount_sum = []

    for entry in orders_data:
        labels.append(entry['customer__name'])
        order_count.append(entry['total'])
        amount_sum.append(entry['total_amount'])

    context = {
        'labels': labels,
        'order_count': order_count,
        'amount_sum': amount_sum,
        'Cust':Cust,
        'employees':employees,
     
        'total_employee':len(Booking.objects.all()),
         'total_veh':len(BookingUpdate.objects.all()),
         'total_cat':len(Vehicle_Category.objects.all()),
            'total_exp':len(Expense.objects.all()),
    
    }
    return render(request, 'employee_information/bok-chart.html', context)
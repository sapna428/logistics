from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create a new user model with a role field.
class RoleUser(User):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')




################################################# 
class Commodity(models.Model):
   
    type= models.CharField(max_length=50)
    status = models.IntegerField(default=0) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.type
# class Currency(models.Model):
   
#     type= models.CharField(max_length=50)
#     status = models.IntegerField(default=0) 
#     date_added = models.DateTimeField(default=timezone.now) 
#     date_updated = models.DateTimeField(auto_now=True) 

#     def __str__(self):
#         return self.type
class Currency_exchange(models.Model):
   
   
    fom= models.CharField(max_length=500,default=0)
    to= models.CharField(max_length=500)
    rate = models.IntegerField(default=0) 
    amount= models.IntegerField(default=0) 
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(default=0) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.total
class Settlement(models.Model):
   
    type= models.CharField(max_length=50)
    status = models.IntegerField(default=0) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.type



class Freight_Category(models.Model):
   
    type= models.CharField(max_length=50)
    status = models.IntegerField(default=0) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.type
 ########### #####################################################
class Carrier(models.Model):
   
    type= models.CharField(max_length=50)
    status = models.IntegerField(default=0) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.type

######################################################################
class Vessel(models.Model):
   
    type= models.CharField(max_length=50)
    status = models.IntegerField(default=0) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.type

############################################################################

class Contract_owner(models.Model):
   
    type= models.CharField(max_length=50)
    status = models.IntegerField(default=0) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.type       
###########################################################################################
class Agent(models.Model):
   
    name= models.CharField(max_length=50)
    address=models.CharField(max_length=500)
    con = models.IntegerField(default=0)
    email = models.EmailField(default=0)
    status = models.IntegerField(default=0) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name 

class Vendor(models.Model):
   
    name= models.CharField(max_length=50)
    address=models.CharField(max_length=500)
    con = models.IntegerField(default=0)
    email = models.EmailField(default=0)
    status = models.IntegerField(default=0) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name 


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    con = models.IntegerField(default=0)
    company_name = models.CharField(max_length=100,default=0)
    stamp = models.ImageField(upload_to='customer_images/', default=0)
    status = models.IntegerField(default=0) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name 

###########################################################
        # Vehicle model
class Booking(models.Model):
   
    Carrier= models.ForeignKey(Carrier, on_delete=models.CASCADE) 
    Commodity= models.ForeignKey(Commodity, on_delete=models.CASCADE) 
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, default=0)
   
    com= models.CharField(max_length=500,default=0)
    stamp = models.ImageField(upload_to='customer_images/', default=0)
    Pol= models.CharField(max_length=50)
    Pofd= models.CharField(max_length=50)
    Pot1= models.CharField(max_length=50)
    Pot2= models.CharField(max_length=50)

    ship= models.CharField(max_length=500)
    pay= models.CharField(max_length=500,default=1 )
    freight= models.ForeignKey(Freight_Category, on_delete=models.CASCADE) 
    cntr_owner= models.ForeignKey(Contract_owner, on_delete=models.CASCADE) 
    Booking_date = models.DateTimeField(default=timezone.now) 
    Sailing_date = models.DateTimeField(default=timezone.now) 
    vessel= models.ForeignKey(Vessel, on_delete=models.CASCADE) 
    status = models.IntegerField( max_length=20,default=1) 
    amount = models.IntegerField( max_length=20,default=1) 

    agent=models.ForeignKey(Agent, on_delete=models.CASCADE) 
    date_updated = models.DateTimeField(auto_now=True) 
    order_no=models.CharField(max_length=500,default=0)

def __str__(self):
        return self.order_no + ' ' +self.customer.name + ' ' +self.Commodity.type

    


###################################################################################

class Vehicle_Category(models.Model):
   
    type= models.CharField(max_length=50)
    status = models.IntegerField(default=0) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.type

  


# Vehicle model
class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_id = models.ForeignKey(Vehicle_Category, on_delete=models.CASCADE) 
    capacity = models.DecimalField(max_digits=10, decimal_places=2)
    size= models.CharField(max_length=20,default=0 )
    status = models.IntegerField( max_length=20,default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
  

    def __str__(self):
        return self.vehicle_number + ' ' +self.vehicle_id.type + ''
    


class Expense_Category(models.Model):
   
    type= models.CharField(max_length=50)
    status = models.IntegerField(default=0) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.type

  
# Expense model
class Expense(models.Model):
    expense = models.CharField(max_length=20, unique=True,default=0)
    expense_id = models.ForeignKey(Expense_Category, on_delete=models.CASCADE) 
    veh_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE) 
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    Description = models.CharField(max_length=500)
    status = models.IntegerField( max_length=20,default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
  

    def __str__(self):
          return f'{self.expense_id.type} - {self.veh_id.type}'
        # return self.expense_id.type + ' ' +self.veh_id.type + ''
    






    # MaintenancePrediction
 




# Container model





# Shipment model

    







# Inventory model (for managing stock at warehouses)





      









class Container_sale(models.Model):

    Cont_id= models.ForeignKey(Vehicle, on_delete=models.CASCADE )  
    status = models.IntegerField( max_length=20,default=1) 
    Sale_price = models.IntegerField(default=0) 
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    Sale_date = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
def __str__(self):
        return self.Sale_date

class Container_purchase(models.Model):
 idd=models.CharField(max_length=200, default=0)
 Con_id= models.ForeignKey(Vehicle, on_delete=models.CASCADE   )
 status = models.IntegerField( max_length=20,default=1) 
 purchase_price = models.IntegerField(default=0) 
 vens= models.ForeignKey(Vendor, on_delete=models.CASCADE)
 purchase_date = models.DateTimeField(default=timezone.now) 
 date_updated = models.DateTimeField(auto_now=True)
def __str__(self):
        return self.purchase_date

class Purchase_invoice (models.Model):

  pur_id= models.ForeignKey(Container_purchase, on_delete=models.CASCADE )  
  
  set_type= models.ForeignKey(Settlement, on_delete=models.CASCADE )  
  com= models.CharField(max_length=500,default=0)
  stamp = models.ImageField(upload_to='customer_images/', default=0)
  status = models.IntegerField( max_length=20,default=1) 
  amount  = models.IntegerField(default=0) 
  port = models.CharField(max_length=200)
  payment_center = models.CharField(max_length=200)
  vendor= models.ForeignKey(Vendor, on_delete=models.CASCADE)    
  invoice_date = models.DateTimeField(default=timezone.now) 
  trans_date = models.DateTimeField(default=timezone.now) 
  date_updated = models.DateTimeField(auto_now=True)
def __str__(self):
        return self.com





class lease_rental (models.Model):

  con_id= models.ForeignKey(Vehicle, on_delete=models.CASCADE )  
  
  buyer= models.ForeignKey(Customer, on_delete=models.CASCADE )  
  
 
  status = models.IntegerField( max_length=20,default=1) 
  amount  = models.IntegerField(default=0) 
 
  rent_start  = models.DateTimeField(auto_now=True)
  rent_end = models.DateTimeField(auto_now=True)
  date_updated = models.DateTimeField(auto_now=True)
def __str__(self):
        return self.amount



# def __str__(self):
#         return self.rate

class Container_slot (models.Model):

  con_id= models.ForeignKey(Vehicle, on_delete=models.CASCADE, default=1)  
  
  set_type= models.ForeignKey(Settlement, on_delete=models.CASCADE )  
  
 
  status = models.IntegerField( max_length=20,default=1) 
  rate  = models.IntegerField(default=0) 
 
  slot_start = models.TimeField(default=timezone.now) 
  slot_end = models.TimeField(default=timezone.now) 
  date_updated = models.DateTimeField(auto_now=True)
def __str__(self):
        return self.rate

def __str__(self):
        return self.rate






class Booking_invoice (models.Model):

  sale_id= models.ForeignKey(Booking, on_delete=models.CASCADE )  
  
    #    set_type= models.ForeignKey(Settlement, on_delete=models.CASCADE )  
  com= models.CharField(max_length=500,default=0)
  stamp = models.ImageField(upload_to='customer_images/', default=0)
  status = models.IntegerField( max_length=20,default=1) 
  amount  = models.IntegerField(default=0) 
  port = models.CharField(max_length=200)
  payment_center = models.CharField(max_length=200)
  customer= models.ForeignKey(Customer, on_delete=models.CASCADE)    
  invoice_date = models.DateTimeField(default=timezone.now) 
  trans_date = models.DateTimeField(default=timezone.now) 
  date_updated = models.DateTimeField(auto_now=True)
def __str__(self):
        return self.com


class BookingUpdate(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    des = models.TextField()
    updated_at = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(default=1) 
def __str__(self):
        return self.booking.order_no



class Special_rate(models.Model):
    # customer= models.ForeignKey(customer, on_delete=models.CASCADE) Carrier= models.ForeignKey(Carrier, on_delete=models.CASCADE) 
    Commodity= models.ForeignKey(Commodity, on_delete=models.CASCADE) 
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, default=0)
    agent= models.ForeignKey(Agent, on_delete=models.CASCADE) 
    det= models.CharField(max_length=50)
    Pol= models.CharField(max_length=50)
    Pofd= models.CharField(max_length=50)
    Pol2= models.CharField(max_length=50)
    Pofd2= models.CharField(max_length=50)
    rate = models.IntegerField( default=1) 
    ship= models.CharField(max_length=500)
    freight= models.ForeignKey(Freight_Category, on_delete=models.CASCADE) 
   
    tra_date = models.DateTimeField(default=timezone.now) 
    tan_exp = models.DateTimeField(default=timezone.now) 

    status = models.IntegerField( max_length=20,default=1) 
   
    date_updated = models.DateTimeField(auto_now=True) 
    

    def __str__(self):
        return self.pol + ' ' +self.Carrier.type + ''
    














class Department(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name


class Employees(models.Model):
    code = models.CharField(max_length=100,blank=True) 
    firstname = models.TextField() 
    middlename = models.TextField(blank=True,null= True) 
    lastname = models.TextField() 
    gender = models.TextField(blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.TextField() 
    address = models.TextField() 
    email = models.TextField() 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '
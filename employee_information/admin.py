from django.contrib import admin
from employee_information.models import Department, Position, Employees,Vehicle_Category,Vehicle,Expense,Expense_Category,Customer,Booking,BookingUpdate

# Register your models here.
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employees)
admin.site.register(Vehicle_Category)
admin.site.register(Vehicle)
admin.site.register(Expense_Category)
admin.site.register(Expense)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(BookingUpdate)
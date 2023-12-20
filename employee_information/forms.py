from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator
from datetime import datetime
from tkinter import Widget
from xml.dom.minidom import Attr
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from .models import Ccw, Fees, Har, Oka1, Oka2, Oka3, Pak,Reading, Swl1, Swl2, Swl3, Upload, Use,  AdmCha, Adm, Category, City, Expense, Medical, Notification, Stops,Attandence,Student,Education,Experience,Con,Job,City, Veh,Tours,Rent
# from .models import Vehicle_type
# from .models import Vehicle
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
# from emp_register.models import Education,Experience,Con,Job,City,Medical,Use
# from emp_register.models import Attandence
import datetime
class CreateUserForm(UserCreationForm):
 class Meta:
        model=User
        fields=['username','email','password1','password2']

from django.contrib.auth.forms import UserCreationForm
# class SignUpForm(UserCreationForm):
#   email = forms.EmailField(required=True)

# class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")

# def save(self, commit=True):
# 		user = super(SignUpForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user
from product.models import Customer
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()

class CustomerForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['username', 'age', 'gender', 'email', 'password']

class CustomerUpdateForm(UserChangeForm):
  password = None
  class Meta:
    model = Customer
    fields = ['username', 'email']

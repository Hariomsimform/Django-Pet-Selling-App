import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user import views
from user import models
from .models import user_profile
from user import views

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	address = forms.CharField(max_length=200)
	user_type  =forms.ChoiceField(choices=[('Buyer','Buyer'), ('Seller','Seller')])
	class Meta:
		model = User
		fields = ("username", "email", "first_name", "last_name", "address", "user_type", "password1", "password2",)
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['username']
		user.First_Name = self.cleaned_data['first_name']
		user.Last_Name = self.cleaned_data['last_name']
		if commit:
			user.save()
		return user
	
class PetInfoForm(forms.ModelForm):
	PetName = forms.CharField(required=True)
	PetAge = forms.CharField(max_length=200)
	PetType  =forms.ChoiceField(choices=[('Cat','Cat'), ('Dog','Dog')])
	PetGender  =forms.ChoiceField(choices=[('Male','Male'), ('Female','Female')])
	class Meta:
		model = User
		fields = ("PetName", "PetAge", "PetType", "PetGender")
	def save(self, commit=True):
		user = PetInfoForm.save(commit=False)
		
		if commit:
			user.save()
		return user	
	def clean_title(self):
		clean_data = self.cleaned_data
		PetName = clean_data.get('PetName')
		PetAge = clean_data.get('PetAge')
		PetType = clean_data.get('PetType')
		PetGender = clean_data.get('PetGender')
		print(clean_data)
		return clean_data
	print(PetName, PetAge, PetType, PetGender)

class BuyNowForm(forms.Form):
	name = forms.CharField(required=False,widget= forms.TextInput
                           (attrs={
                               'placeholder':'Enter Name',
                               'required': 'True'
                            }))
	email = forms.EmailField(max_length=200,required=False,widget= forms.TextInput
                           (attrs={
                               'placeholder':'Enter Your Email',
                               'required': 'True'
                            }))
	address = forms.CharField(required=False,widget= forms.TextInput
                           (attrs={
                               'placeholder':'Enter House Name, No.',
                               'required': 'True'
                            }))
	city = forms.CharField(max_length=60,required=False,widget= forms.TextInput
                           (attrs={
                               'placeholder':'Enter City Name',
                               'required': 'True'
                            }))
	state = forms.CharField(max_length=30,required=False,widget= forms.TextInput
                           (attrs={
                               'placeholder':'Enter State Name',
                               'required': 'True'
                            }))
	zipcode = forms.CharField(max_length=5,required=False,widget= forms.TextInput
                           (attrs={
                               'placeholder':'Enter Zip Code',
                               'required': 'True'
                            }))
	country = forms.CharField(max_length=50,required=False,widget= forms.TextInput
                           (attrs={
                               'placeholder':'Enter Country Name',
                               'required': 'True'
                            }))
	class Meta:
		model = User
		fields = ("name", "email", "address", "city","state","zipcode", "country")

class UpdateForm(forms.Form):
	pet_name = forms.CharField(required=False,widget= forms.TextInput
                           (attrs={
                               'placeholder':'Enter Updated Pet Name',
                               'required': 'True'
                            }))
	pet_age = forms.IntegerField(required=False,widget= forms.TextInput
                           (attrs={
                               'placeholder':'Enter Updated Pet Name',
                               'required': 'True'
                            }))		
	class Meta:
		model = User
		fields = ("pet_name", "pet_age")											


			

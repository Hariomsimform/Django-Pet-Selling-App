
# from typing_extensions import Self
from unicodedata import name
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import  render, redirect
from .forms import NewUserForm , PetInfoForm, BuyNowForm, UpdateForm
from django.contrib.auth import login, logout
from django.contrib import messages
from user import models
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.utils.datastructures import MultiValueDictKeyError
from .models import user_profile, Pet, Cart
from django.contrib.auth.decorators import login_required
import pdb

def home_page(request):
	if request.method == "POST":
		return HttpResponseRedirect('/register/')
	return render(request=request, template_name='user/home.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		address = request.POST['address']
		user_type = request.POST['user_type']
		
		print(first_name, last_name, address, user_type)
		if form.is_valid():
			user = form.save()
			print("I am saved")
			ins = models.user_profile(user_id = user, first_name = first_name, last_name = last_name, address = address, user_type = user_type )		
			ins.save()
			messages.success(request, "Registration successful." )
			return redirect('/login/')
		else:
			messages.error(request, "Unsuccessful resgistration. Invalid Information")	
			form = NewUserForm()
			return render (request=request, template_name="user/signup.html", context={"register_form":form})
	else:		
		# messages.error(request, "Unsuccessful registration. Invalid information.")
		form = NewUserForm()
		return render (request=request, template_name="user/signup.html", context={"register_form":form})
		
def login(request):
	if request.method == 'POST':
		print('You enterd here')
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username = username, password= password)
		if user is not None:
			auth.login(request, user)
			print("you are logged in successfully")
			
			return render(request, 'user/profile.html')
		else:
			messages.info(request, 'invalid credentials')	
			# print("invalid credentials")
			return redirect("login")
	else:
		return render(request, 'user/login.html')	

def logout_reqest(request):
	logout(request)
	messages.info(request, 'Log out successfully')
	messages.info(request, 'Login Again!')
	print("log out successfully")
	return redirect('login')

@login_required(login_url='/login/')
def about(request,pk):
	data = user_profile.objects(pk = pk)
	print(data)
	return render(request=request, template_name='user/userdetail.html', context = {'data':data})

def pet_form(request):
	form = PetInfoForm(request.POST)
	if request.method == "POST":
		
		pet_name = request.POST['PetName']
		pet_age = request.POST['PetAge']
		pet_type = request.POST['PetType']
		pet_gender = request.POST['PetGender']
		context= {'form': form}
		print("I am Inside")
		key_var =request.user.id
		print(key_var)
		user = User.objects.get(id=key_var)
		PetObject = Pet(pet_name =pet_name, pet_age=pet_age, pet_type =pet_type, pet_gender =pet_gender,owner_id=user)
		PetObject.save()
		return render(request, 'user/profile.html', context = context)
	return render (request=request, template_name="user/petdetail.html", context={"pet_form":form})

def product_page(request):
	latest_product_list = Pet.objects.all()
	# print(request.Pet.pet_name)
	print(latest_product_list)
	
	context = {'latest_product_list': latest_product_list}
	return render(request = request, template_name='user/buyerproductpage.html', context= context)

def only_cat(request):
	cat_product_list = Pet.objects.all().filter(pet_type="Cat")
	print(cat_product_list)
	context = {'latest_product_list': cat_product_list}
	return render(request = request, template_name='user/buyerproductpage.html', context= context)

def only_dog(request):
	dog_product_list = Pet.objects.all().filter(pet_type="Dog")
	print(dog_product_list)
	context = {'latest_product_list': dog_product_list}
	return render(request = request, template_name='user/buyerproductpage.html', context= context)	

def cart(request):
	product = request.POST.get('product')
	print(product)
	pet = Pet.objects.get(id=product)
	print(pet.id)
	key_var =request.user.id
	user = User.objects.get(id=key_var)
	print(user.id)
	cartobj = Cart(pet_id=pet, buyer_id=user.id)
	cartobj.save()
	return redirect('/productpage')

def view_cart(request):
	key_var =request.user.id
	user_cart_product = Cart.objects.all().filter(buyer_id=key_var)
	for product in user_cart_product:
		print(product)
	context = {'latest_product_list': user_cart_product}
	return render(request = request, template_name='user/buyercartpage.html', context= context)	

def del_item(request):
	del_id =request.POST.get('delproduct')
	print(del_id)
	Cart.objects.filter(id=del_id).delete()
	return redirect("/view/cart")

def buy_page(request):
	# form = BuyNowForm(request.POST or None)
	if request.method == "POST":
		form = BuyNowForm(request.POST)
		messages.info(request,'Order Placed Successfully')
		# return redirect('/productpage')
	else:		
		form = BuyNowForm(request.POST or None)
		return render (request=request, template_name="user/buynow.html", context={"buynow_form":form})	
	return render (request=request, template_name="user/buynow.html", context={"buynow_form":form})	

def owner_product_page(request):
	key_var =request.user.id	
	owner_product_list = Pet.objects.all().filter(owner_id=key_var)
	for product in owner_product_list:
		print(product)
	context = {'latest_product_list': owner_product_list}
	return render(request = request, template_name='user/ownerproductpage.html', context= context)

def delete_owner_product(request):
	del_id =request.POST.get('delproduct')
	print(del_id)
	Pet.objects.filter(id=del_id).delete()
	return redirect("/pet/list")



def update_owner_product(request,pk):
	print(pk)
	form=UpdateForm()
	if request.method == "POST":
		try:
			pet_name = request.POST['pet_name']
		except MultiValueDictKeyError:
			pet_name = False
		try:
			pet_age = request.POST['pet_age']
		except MultiValueDictKeyError:
			pet_age = False	

		pet_obj = Pet.objects.get(id=pk)
		pet_obj.pet_name=pet_name
		pet_obj.pet_age=pet_age
		pet_obj.save()	
		print(pet_name, pet_age,pk)
	else:		
		form = PetInfoForm(request.POST or None)
		return render (request=request, template_name="user/updateform.html", context={"update_form":form})	
	return render (request=request, template_name="user/updateform.html", context={"update_form":form})	

def order_successful(request):
	messages.info(request, 'Congratulations, Order Placed Successfully')
	return redirect('/productpage/')


	
		

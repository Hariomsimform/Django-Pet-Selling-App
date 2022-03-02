from django.contrib import admin

# Register your models here.
# from user.models import user_profile
from django.contrib.auth.models import User
from .models import Pet
from .models import user_profile, Cart
from django.contrib.admin import ModelAdmin
from django.contrib.admin import SimpleListFilter
class PetAdmin(admin.ModelAdmin):
    date_hierarchy = 'pet_name'

admin.site.register([Pet,user_profile, Cart])
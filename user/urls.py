from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('register/', views.signup, name ='Signup'),
    path("register/", views.register_request, name="register"),
    # path('login/', views.loginPage, name ='Login')
    # path("register/profile/", views.new_user_profile, name="profile"),
    path("", views.home_page, name = "home"),
    path("login/", views.login, name = "login"),
    path('about/<int:pk>', views.about, name = 'about' ),
    path("logout/", views.logout_reqest, name = "logout"),
    path("petform/", views.pet_form, name = "pet"),
    path("productpage/", views.product_page, name = "product"),
    path("product/cat", views.only_cat, name = "product-cat"),
    path("product/dog", views.only_dog, name = "product-cat"),
    path("#", views.cart, name='cart'),
    path("view/cart", views.view_cart, name="viewcart"),
    path("/delete", views.del_item, name='deleteitem'),
    path("/buynow", views.buy_page, name='buy'),
    path("pet/list", views.owner_product_page, name='owner'),
    path("pet/update/<str:pk>", views.update_owner_product, name='update'),
    path("pet/delete", views.delete_owner_product, name='delete'),
    path("order/successful", views.order_successful, name='order_successful'),
    
]
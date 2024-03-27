from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('about', views.about, name='about-page'),
    path('client', views.client, name='client-page'),
    path('contact', views.contact, name='contact-page'),
    path('products', views.products, name='products-page'),
    path('reg/', views.userReg, name='reg-page'),
    path('login/', views.userLog, name='log-page'),
    path('logout/', views.userLogout, name='log-out-page'),

]
from django.urls import path
from . import views
from store.controller import authview

urlpatterns = [
    path('', views.home, name='home'),
    path('categories', views.categories, name='categories'),
    path('categories/<str:slug>', views.categoriesview, name='categoriesview' ),
    path('categories/<str:cate_slug>/<str:prod_slug>', views.productview, name='productview'),
    path('register/', authview.register, name='register'),
    path('login/', authview.loginpage, name='loginpage'),
    path('logout/', authview.logoutpage, name='logout')
]
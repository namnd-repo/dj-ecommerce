from django.urls import path
from . import views
from store.controller import authview, cart, checkout, order

urlpatterns = [
    path('', views.home, name='home'),
    path('categories', views.categories, name='categories'),
    path('categories/<str:slug>', views.categoriesview, name='categoriesview' ),
    path('categories/<str:cate_slug>/<str:prod_slug>', views.productview, name='productview'),
    
    path('register/', authview.register, name='register'),
    path('login/', authview.loginpage, name='loginpage'),   
    path('logout/', authview.logoutpage, name='logout'),

    path('add-to-cart', cart.addtocart, name='addtocart'),
    path('cart', cart.viewcart, name='cart'),
    path('update-cart', cart.updatecart, name='updatecart'),
    path('delete-cart-item', cart.deletecartitem, name='deletecartitem'),

    path('checkout', checkout.index, name='checkout'),
    path('place-order', checkout.placeorder, name='placeorder'),

    path('my-orders', order.index, name='myorders'),
    path('view-order/<str:t_no>', order.vieworder, name='orderview'),
]
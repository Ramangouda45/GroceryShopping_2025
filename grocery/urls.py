"""
URL configuration for grocery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('user_home', views.user_home, name='user_home'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('Reg',views.Reg,name='Reg'),
    path('Add_category', views.Add_category, name='Add_category'),
    path('addgrocery', views.addgrocery, name='addgrocery'),
    path('grocery_item', views.grocery_item, name='grocery_item'),
    path('grocery_order', views.grocery_order, name='grocery_order'),
    path('Addpayment', views.Addpayment, name='Addpayment'),
    path('add_reviews', views.add_reviews, name='add_reviews'),

    path('user_view',views.user_view,name='user_view'),
    path('reg_view',views.reg_view,name='reg_view'),
    path('category_view', views.category_view, name='category_view'),
    path('grocery_view', views.grocery_view, name='grocery_view'),
    path('itemgrocery_view', views.itemgrocery_view, name='itemgrocery_view'),
    path('ordergrocery_view', views.ordergrocery_view, name='ordergrocery_view'),
    path('payment_view', views.payment_view, name='payment_view'),
    path('review_view', views.review_view, name='review_view'),

    path('user_del/<int:pk>', views.user_del, name='user_del'),
    path('reg_del/<int:pk>', views.reg_del, name='reg_del'),
    path('category_del/<int:pk>', views.category_del, name='category_del'),
    path('grocery_del/<int:pk>', views.grocery_del, name='grocery_del'),
    path('itemgrocery_del/<int:pk>', views.itemgrocery_del, name='itemgrocery_del'),
    path('ordergrocery_del/<int:pk>', views.ordergrocery_del, name='ordergrocery_del'),
    path('payment_del/<int:pk>', views.payment_del, name='payment_del'),
    path('review_del/<int:pk>', views.review_del, name='review_del'),

    path('login_auth',views.login_auth,name='login_auth'),

    path('otp', views.otp, name='otp'),
    path('forgotpass', views.forgotpass, name='forgotpass'),
    path('resetpass', views.resetpass, name='resetpass'),

    path('reg_edit/<int:pk>',views.reg_edit,name='reg_edit'),
    path('itemgrocery_edit/<int:pk>',views.itemgrocery_edit,name='itemgrocery_edit'),
    path('category_edit/<int:pk>',views.category_edit,name='category_edit'),
    path('grocery_edit/<int:pk>',views.grocery_edit,name='grocery_edit'),
    path('ordergrocery_edit/<int:pk>',views.ordergrocery_edit,name='ordergrocery_edit'),
    path('payment_edit/<int:pk>',views.payment_edit,name='payment_edit'),
    path('review_edit/<int:pk>',views.review_edit,name='review_edit'),

    path('cat_wise/<str:cat>',views.cat_wise,name='cat_wise'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('mycart/', views.mycart, name='mycart'),  # Optional view to show cart
    path('cart_del/<int:pk>',views.cart_del,name='cart_del'),
    path('confirm_order/',views.confirm_order,name='confirm_order'),
    path('pay_bill/<int:total>',views.pay_bill,name='pay_bill'),
    path('myorder',views.myorder,name='myorder'),
    path('customer_orders',views.customer_orders,name='customer_orders'),

    path('view_orders/<int:order_no>',views.view_orders,name='view_orders'),
    path('date_wise_orders',views.date_wise_orders,name='date_wise_orders'),

    path('view_cust_orders/<int:order_no>',views.view_cust_orders,name='view_cust_orders'),
    path('pay_message',views.pay_message,name='pay_message'),
    path('all_products',views.all_products,name='all_products'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
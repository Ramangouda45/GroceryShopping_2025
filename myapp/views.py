import random
from ctypes import pythonapi

from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import UserLogin,UserRegistration,AddCategory,AddGrocery,GroceryItems,GroceryOrder,AddPayment,AddReviews,OtpCode
import datetime
import smtplib
from django.contrib import messages









def index(request):
    reviews = AddReviews.objects.all()
    data = AddCategory.objects.values('category').distinct()[:4]
    return render(request,'index.html',{'data':data,'reviews':reviews})

def admin_home(request):
    return render(request,'admin_home.html')

def user_home(request):
    reviews = AddReviews.objects.all()
    data = AddCategory.objects.values('category').distinct()[:4]
    fruits = GroceryItems.objects.filter(category='Fruits').values()
    return render(request,'user_home.html',{'data':data,'fruits':fruits,'reviews':reviews})


def cat_wise(request,cat):
    cat_data=GroceryItems.objects.filter(category=cat).values()
    data = AddCategory.objects.values('category').distinct()[:4]
    fruits = GroceryItems.objects.filter(category='Fruits').values()
    return render(request,'cat_wise.html',{'cat_data':cat_data,'data':data,'fruits':fruits})


def all_products(request,cat):
    cat_data=GroceryItems.objects.filter(category=cat).values()
    data = AddCategory.objects.values('category').distinct()[:4]
    fruits = GroceryItems.objects.filter(category='Fruits').values()
    return render(request,'all_products.html',{'cat_data':cat_data,'data':data,'fruits':fruits})


def add_to_cart(request):
    order_no=request.session['order_no']
    if request.method == "POST":
        item_id = request.POST.get("item_id")
        quantity = int(request.POST.get("quantity", 1))
        username = request.session.get('username')  # Or request.user.username if using auth
        user = get_object_or_404(UserRegistration, email=username)
        item = get_object_or_404(GroceryItems, id=item_id)
        #item = get_object_or_404(GroceryItems, name=item_name)
        price = item.price
        total = quantity * price

        # Insert into GroceryOrder table
        GroceryOrder.objects.create(
            userid=user,
            item=item,
            qty=quantity,
            price=price,
            total=total,
            payment_status='pending',
            order_status='pending',
            order_no=order_no
        )
        messages.success(request, f"{item.name} added to cart!")
        return redirect('cat_wise', cat=item.category)  # redirect back to same category page






def mycart(request):
    order_no=request.session['order_no']
    data = AddCategory.objects.values('category').distinct()[:4]
    fruits = GroceryItems.objects.filter(category='Fruits').values()
    username = request.session.get('username')  # Email stored in session
    user = get_object_or_404(UserRegistration, email=username)
    cart_items = GroceryOrder.objects.filter(userid=user).filter(payment_status='pending')
    total = sum(item.total for item in cart_items)  # Assuming 'total' is a numeric field
    return render(request, 'mycart.html', {'cart_items': cart_items, 'total': total,'order_no':order_no,'data':data,'fruits':fruits})


def cart_del(request,pk):
    data=GroceryOrder.objects.get(id=pk)
    data.delete()
    return redirect('mycart')


def confirm_order(request):
    order_no=request.session['order_no']
    data=GroceryOrder.objects.filter(order_no=order_no).update(order_status='confirm')
    messages.success(request,'Thank you for the order confirmation..!')
    return redirect('mycart')


def pay_bill(request,total):
    order_no=request.session['order_no']
    if request.method=="POST":
        GroceryOrder.objects.filter(order_no=order_no).update(payment_status='paid')

        return redirect('pay_message')
    return render(request,'pay_bill.html',{'total':total})


def pay_message(request):
    messages.success(request, 'Thank you for the Payment..!')
    return render(request,'pay_message.html')



def myorder(request):
    username = request.session.get('username')  # Email stored in session
    data = AddCategory.objects.values('category').distinct()[:4]
    fruits = GroceryItems.objects.filter(category='Fruits').values()
    user = get_object_or_404(UserRegistration, email=username)
    cart_item = GroceryOrder.objects.filter(userid=user).filter(payment_status='paid')
    cart_items = GroceryOrder.objects.filter(
        userid=user,
        payment_status='paid'
    ).values('order_no').distinct()

    total = sum(item.total for item in cart_item)  # Assuming 'total' is a numeric field
    return render(request, 'myorder.html', {'cart_items': cart_items, 'total': total,'data':data})




def view_orders(request,order_no):
    username = request.session.get('username')  # Email stored in session
    user = get_object_or_404(UserRegistration, email=username)
    cart_items = GroceryOrder.objects.filter(userid=user).filter(payment_status='paid').filter(order_no=order_no)
    total = sum(item.total for item in cart_items)  # Assuming 'total' is a numeric field
    return render(request, 'vieworders.html', {'cart_items': cart_items, 'total': total,'order_no':order_no})



def customer_orders(request):
    cart_item = GroceryOrder.objects.filter(payment_status='paid')
    cart_items = GroceryOrder.objects.filter(
        payment_status='paid'
    ).values('order_no').distinct()

    total = sum(item.total for item in cart_item)  # Assuming 'total' is a numeric field
    return render(request, 'customer_orders.html', {'cart_items': cart_items, 'total': total})


def view_cust_orders(request,order_no):

    cart_items = GroceryOrder.objects.filter(payment_status='paid').filter(order_no=order_no)
    total = sum(item.total for item in cart_items)  # Assuming 'total' is a numeric field
    return render(request, 'view_cust_orders.html', {'cart_items': cart_items, 'total': total, 'order_no': order_no})

def date_wise_orders(request):
    if request.method=="POST":
        dd=request.POST.get('dd')
        cart_items = GroceryOrder.objects.filter(payment_status='paid').filter(order_date=dd)
        total = sum(item.total for item in cart_items)  # Assuming 'total' is a numeric field
        return render(request, 'date_wise_orders2.html',
                      {'cart_items': cart_items, 'total': total,'dd':dd})

    return render(request,'date_wise_orders.html')

# login authentication code
def login_auth(request):
    order_no = random.randint(100000,999999)
    request.session['order_no']=order_no
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('pwd')
        request.session['username']=username

        count=UserLogin.objects.filter(username=username).count()
        if count>=1:
            udata=UserLogin.objects.get(username=username)
            upass = udata.password
            utype= udata.utype

            if password==upass:
                if utype=='admin':
                    return redirect('admin_home')
                if utype=='user':
                        return redirect('user_home')

            else:
                return render(request,'userlogin.html',{'msg':'invalid password'})

        else:
            return render(request, 'userlogin.html', {'msg': 'invalid username'})


    return render(request, 'userlogin.html')


def forgotpass(request):
    if request.method == "POST":
        username = request.POST.get('t1')
        request.session['username']=username
        ucheck=UserLogin.objects.filter(username=username).count()
        if ucheck==1:
            otp = random.randint(1111,9999)
            OtpCode.objects.create(otp=otp, status='active')
            content = "Your OTP IS-" + str(otp)
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('ramangoudasanjusanju@gmail.com','uzyz dgsx hwhy ryqh')
            mail.sendmail('ramangoudasanjusanju@gmail.com',username,content)
            return redirect('otp')
        else:
            return render(request,'forgotpass.html',{'mzg':'Invalid Username'})
    return render(request,'forgotpass.html')



def otp(request):
    if request.method == "POST":
        otp = request.POST.get('t1')
        ucheck = OtpCode.objects.filter(otp=otp).count()
        if ucheck>=1:
            return redirect('resetpass')
        else:
            return render(request,'otp.html',{'msg':'Invalid OTP'})
    return render(request,'otp.html')


def resetpass(request):
    username=request.session['username']
    if request.method=="POST":
        newpass=request.POST.get('t1')
        confirmpass=request.POST.get('t2')
        if newpass==confirmpass:
            UserLogin.objects.filter(username=username).update(password=newpass)
            return redirect('login_auth')
        else:
            return render(request,'resetpass.html',{'msg':'New password must be same'})
    return render(request,'resetpass.html')





def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('pwd')
        utype = request.POST.get('utype')
        UserLogin.objects.create(username=username, password=password, utype=utype)
        return render(request, 'userlogin.html', {'msg': 'record added successfully'})
    return render(request, 'userlogin.html')



def Reg(request):
    if request.method == "POST":
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        city = request.POST.get('city')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        email = request.POST.get('email')
        password = request.POST.get('password')
        count=UserRegistration.objects.filter(email=email).count()
        if count>=1:
            return render(request,'Reg.html',{'msg':'User already Exist'})
        else:
            UserLogin.objects.create(username=email,password=password,utype='user')
            UserRegistration.objects.create(firstname=firstname,lastname=lastname,gender=gender,dob=dob,city=city,address=address,pincode=pincode,email=email)
            return render(request, 'Reg.html', {'success': 'created successfully'})
    return render(request,'Reg.html')


def Add_category(request):
    if request.method == "POST":
        category = request.POST.get('category')
        AddCategory.objects.create(category=category)
        return render(request, 'Add_category.html', {'msg': 'record added successfully'})
    return render(request,'Add_category.html')


def addgrocery(request):
    if request.method == "POST":
        category = request.POST.get('category')
        grocery_name = request.POST.get('grocery')
        AddGrocery.objects.create(category=category,grocery_name=grocery_name)
        return render(request, 'addgrocery.html', {'msg': 'record added successfully'})
    return render(request,'addgrocery.html')


def grocery_item(request):
    category=AddCategory.objects.values('category').distinct()
    if request.method == "POST":
        category = request.POST.get('category')
        name = request.POST.get('name')
        qty = request.POST.get('qty')
        uom = request.POST.get('uom')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        stock = request.POST.get('stock')
        GroceryItems.objects.create(category=category,name=name,qty=qty,uom=uom,price=price,image=image,stock=stock)
        return render(request, 'grocery_item.html', {'msg': 'record added successfully','category':category})
    return render(request,'grocery_item.html',{'category':category})



def grocery_order(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        item = request.POST.get('item')
        qty = request.POST.get('qty')
        price = request.POST.get('price')
        total = request.POST.get('total')

        GroceryOrder.objects.create(userid=userid,item=item,qty=qty,price=price,total=total)
        return render(request, 'grocery_order.html', {'msg': 'record added successfully'})
    return render(request,'grocery_order.html')


def Addpayment(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        order_no = request.POST.get('order_no')
        payment_date = request.POST.get('date')
        AddPayment.objects.create(userid=userid,order_no=order_no,payment_date=payment_date)
        return render(request, 'Addpayment.html', {'msg': 'record added successfully'})
    return render(request,'Addpayment.html')


def add_reviews(request):
    userid=request.session['username']
    data = AddCategory.objects.values('category').distinct()[:4]
    fruits = GroceryItems.objects.filter(category='Fruits').values()
    if request.method == "POST":
        comments = request.POST.get('comments')
        suggestions = request.POST.get('suggestions')
        ratings = request.POST.get('ratings')
        AddReviews.objects.create(userid=userid,comments=comments,suggestions=suggestions,ratings=ratings)
        return render(request, 'add_reviews.html', {'msg': 'Thank you for your review..!'})
    return render(request,'add_reviews.html',{'data':data})

def user_view(request):
    udata = UserLogin.objects.all()
    return render(request,'user_view.html',{'udata':udata})


def reg_view(request):
    udata = UserRegistration.objects.all()
    return render(request,'reg_view.html',{'udata':udata})

def category_view(request):
    udata = AddCategory.objects.all()
    return render(request,'category_view.html',{'udata':udata})


def grocery_view(request):
    udata = AddGrocery.objects.all()
    return render(request,'grocery_view.html',{'udata':udata})


def itemgrocery_view(request):
    udata = GroceryItems.objects.all()
    return render(request,'itemgrocery_view.html',{'udata':udata})

def ordergrocery_view(request):
    udata = GroceryOrder.objects.all()
    return render(request,'ordergrocery_view.html',{'udata':udata})


def payment_view(request):
    udata = AddPayment.objects.all()
    return render(request,'payment_view.html',{'udata':udata})




def review_view(request):
    reviews = AddReviews.objects.all()
    return render(request, 'reviews_list.html', {'reviews': reviews})


def user_del(request,pk):
    udata=UserLogin.objects.get(id=pk)
    udata.delete()
    return redirect('user_view')



def reg_del(request,pk):
    udata=UserRegistration.objects.get(id=pk)
    udata.delete()
    return redirect('reg_view')


def grocery_del(request,pk):
    udata=AddGrocery.objects.get(id=pk)
    udata.delete()
    return redirect('grocery_view')


def category_del(request,pk):
    udata=AddCategory.objects.get(id=pk)
    udata.delete()
    return redirect('category_view')


def itemgrocery_del(request,pk):
    udata=GroceryItems.objects.get(id=pk)
    udata.delete()
    return redirect('itemgrocery_view')

def ordergrocery_del(request,pk):
    udata=GroceryOrder.objects.get(id=pk)
    udata.delete()
    return redirect('ordergrocery_view')


def payment_del(request,pk):
    udata=AddPayment.objects.get(id=pk)
    udata.delete()
    return redirect('payment_view')


def review_del(request,pk):
    udata=AddReviews.objects.get(id=pk)
    udata.delete()
    return redirect('review_view')



def reg_edit(request,pk):
    data=UserRegistration.objects.filter(id=pk).values()
    if request.method == "POST":
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        city = request.POST.get('city')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        email = request.POST.get('email')
        (UserRegistration.objects.filter(id=pk).update
         (firstname=firstname,
         lastname=lastname,gender=gender,
        dob=dob,city=city,address=address,
        pincode=pincode,email=email))
        return redirect('reg_view')

    return render(request,'reg_edit.html',{'data':data})


def category_edit(request,pk):
    data=AddCategory.objects.filter(id=pk).values()
    if request.method == "POST":
        category = request.POST.get('category')
        AddCategory.objects.filter(id=pk).update(category=category)
        return redirect('category_view')
    return render(request, 'category_edit.html', {'data': data})


def grocery_edit(request,pk):
    data=AddGrocery.objects.filter(id=pk).values()
    if request.method == "POST":
        category = request.POST.get('category')
        grocery_name = request.POST.get('grocery')
        AddGrocery.objects.filter(id=pk).update(category=category,grocery_name=grocery_name)
        return redirect('grocery_view')
    return render(request, 'grocery_edit.html', {'data': data})


def itemgrocery_edit(request,pk):
    data=GroceryItems.objects.filter(id=pk).values()
    if request.method == "POST":
        category = request.POST.get('category')
        name = request.POST.get('name')
        qty = request.POST.get('qty')
        uom = request.POST.get('uom')
        price = request.POST.get('price')
        image = request.POST.get('image')
        stock = request.POST.get('stock')
        GroceryItems.objects.filter(id=pk).update(category=category, name=name, qty=qty, uom=uom, price=price, image=image,
                                    stock=stock)
        return redirect('itemgrocery_view')

    return render(request, 'itemgrocery_edit.html', {'data': data})



def ordergrocery_edit(request,pk):
    data=GroceryOrder.objects.filter(id=pk).values()
    if request.method == "POST":
        userid = request.POST.get('userid')
        item = request.POST.get('item')
        qty = request.POST.get('qty')
        price = request.POST.get('price')
        total = request.POST.get('total')
        GroceryOrder.objects.filter(id=pk).update(userid=userid, item=item, qty=qty, price=price, total=total)
        return redirect('ordergrocery_view')

    return render(request, 'ordergrocery_edit.html', {'data': data})


def payment_edit(request,pk):
    data=AddPayment.objects.filter(id=pk).values()
    if request.method == "POST":
        userid = request.POST.get('userid')
        order_no = request.POST.get('order_no')
        payment_date = request.POST.get('date')
        AddPayment.objects.filter(id=pk).update(userid=userid,order_no=order_no,payment_date=payment_date)
        return redirect('payment_view')

    return render(request, 'payment_edit.html', {'data': data})




def review_edit(request,pk):
    data=AddReviews.objects.filter(id=pk).values()
    if request.method == "POST":
        userid = request.POST.get('userid')
        comments = request.POST.get('comments')
        suggestions = request.POST.get('suggestions')
        ratings = request.POST.get('ratings')
        AddReviews.objects.filter(id=pk).update(userid=userid, comments=comments, suggestions=suggestions, ratings=ratings)
        return redirect('review_view')

    return render(request, 'review_edit.html', {'data': data})







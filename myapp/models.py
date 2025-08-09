from django.db import models

# Create your models here.
class UserLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)

class UserRegistration(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    pincode = models.IntegerField()
    email = models.CharField(max_length=50)

class AddCategory(models.Model):
    category = models.CharField(max_length=50)

class AddGrocery(models.Model):
    category = models.CharField(max_length=50)
    grocery_name = models.CharField(max_length=50)

class GroceryItems(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    qty = models.IntegerField()
    uom = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    stock = models.IntegerField()

class GroceryOrder(models.Model):
    order_no = models.IntegerField(null=True, blank=True)
    userid = models.ForeignKey(UserRegistration, on_delete=models.CASCADE,null=True,blank=True)
    item = models.ForeignKey(GroceryItems, on_delete=models.CASCADE,null=True,blank=True)
    qty = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)
    order_date = models.DateField(auto_now_add=True,null=True,blank=True)
    order_time = models.TimeField(auto_now_add=True,null=True,blank=True)
    payment_status = models.CharField(max_length=100, default='pending',null=True,blank=True)
    order_status = models.CharField(max_length=50, default='pending',null=True,blank=True)

    def save(self, *args, **kwargs):
        self.total = self.qty * self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.userid.username} - {self.item.name} - {self.qty}"




class AddPayment(models.Model):
    userid = models.CharField(max_length=50,null=True,blank=True)
    order_no = models.IntegerField()
    payment_date = models.DateField(auto_now_add=True)

class AddReviews(models.Model):
    userid = models.CharField(max_length=50,null=True,blank=True)
    comments = models.CharField(max_length=50,null=True,blank=True)
    suggestions = models.CharField(max_length=50,null=True,blank=True)
    ratings = models.IntegerField(null=True,blank=True)


class OtpCode(models.Model):
    otp = models.IntegerField()
    status  = models.CharField(max_length=50)





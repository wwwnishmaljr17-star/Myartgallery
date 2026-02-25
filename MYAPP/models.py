from django.db import models

# Create your models here.
from django.forms.fields import DateField


class loginTbl(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class userTbl(models.Model):
    LOGIN=models.ForeignKey(loginTbl,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    place=models.CharField(max_length=100)
    pin=models.BigIntegerField()


class artistTbl(models.Model):
    LOGINID=models.ForeignKey(loginTbl,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    image=models.FileField()
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    place=models.CharField(max_length=100)
    pin=models.BigIntegerField()
    post=models.CharField(max_length=100)


class complaintsTbl(models.Model):
    USERID=models.ForeignKey(userTbl,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=750)
    reply=models.CharField(max_length=599)
    date=models.DateField()



class reviewTbl(models.Model):
    USERID=models.ForeignKey(userTbl,on_delete=models.CASCADE)
    review=models.CharField(max_length=100)
    rating=models.FloatField()
    date=models.DateField()


class artistreviewTbl(models.Model):
    ARTIST=models.ForeignKey(artistTbl,on_delete=models.CASCADE)
    USERID=models.ForeignKey(userTbl,on_delete=models.CASCADE)
    review=models.CharField(max_length=100)
    rating=models.FloatField()
    date=models.DateField()

class designTbl(models.Model):
    ARTIST=models.ForeignKey(artistTbl,on_delete=models.CASCADE)
    date=models.DateField()
    name=models.CharField(max_length=100)
    image=models.FileField()
    description=models.CharField(max_length=599)
    status=models.CharField(max_length=100,default="available")

class chatTbl(models.Model):
    from_id=models.ForeignKey(loginTbl,on_delete=models.CASCADE,related_name='s')
    to_id=models.ForeignKey(loginTbl,on_delete=models.CASCADE,related_name='v')
    date=models.DateField()
    message=models.CharField(max_length=599)


class schedulesTbl(models.Model):
    date=models.DateField()
    time=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    ARTIST=models.ForeignKey(artistTbl,on_delete=models.CASCADE)


class bookingsTbl(models.Model):
    USERID=models.ForeignKey(userTbl,on_delete=models.CASCADE)
    date=models.DateField()
    # DESIGNID=models.ForeignKey(designTbl,on_delete=models.CASCADE)
    SCHEDULE=models.ForeignKey(schedulesTbl,on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    payment_status=models.CharField(max_length=100,default="unpaid")


class productTbl(models.Model):
    ARTIST=models.ForeignKey(artistTbl,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    work=models.FileField()
    description=models.CharField(max_length=100)
    amount=models.BigIntegerField()
    date=models.DateField()

class postTbl(models.Model):
    ARTIST=models.ForeignKey(artistTbl,on_delete=models.CASCADE)
    post=models.CharField(max_length=400)
    design=models.FileField()
    date=models.DateField()
    postname=models.CharField(max_length=100)

class comments(models.Model):
    POSTID=models.ForeignKey(postTbl,on_delete=models.CASCADE)
    USERID=models.ForeignKey(userTbl,on_delete=models.CASCADE)
    comments=models.CharField(max_length=100)
    date=models.DateField()

class likeTbl(models.Model):
    POSTID = models.ForeignKey(postTbl, on_delete=models.CASCADE)
    USERID = models.ForeignKey(userTbl, on_delete=models.CASCADE)
    date = models.DateField()
    like=models.IntegerField()


class orderTbl (models.Model):
    USERID = models.ForeignKey(userTbl, on_delete=models.CASCADE)
    product =models.ForeignKey(productTbl, on_delete=models.CASCADE)
    amount =models.FloatField()
    status =models.CharField(max_length=100)
    date = models.DateField()
    qty = models.IntegerField()


class paymentsTbl(models.Model):
    ORDER=models.ForeignKey(orderTbl,on_delete=models.CASCADE)
    amount=models.BigIntegerField()
    date=models.DateField()
    status=models.CharField(max_length=100)



class ProductpaymentsTbl(models.Model):
    PRODUCT=models.ForeignKey(productTbl,on_delete=models.CASCADE)
    amount=models.BigIntegerField()
    date=models.DateField()
    status=models.CharField(max_length=100)
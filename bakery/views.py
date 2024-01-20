from django.shortcuts import render,redirect
from bakery.models import tbl_customer,tbl_order,tbl_payment,tbl_product
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout
import os

# Create your views here.
def index(request):
    return render(request,'index.html')
def homepage(request):
    return render(request,'homepage.html')
def register(request):
    if request.method=='POST':
        a=request.POST['fname']
        b=request.POST['lname']
        c=request.POST['address']
        d=request.POST['place']
        e=request.POST['email']
        f=request.POST['phone']
        g=request.POST['uname']
        i=request.POST['pswd']
        h=tbl_customer(Username=g,First_name=a,Last_name=b,Address=c,Place=d,Email=e,Phone=f)
        data=User(username=g)
        data.set_password(i)
        data.save()
        h.save()
        return HttpResponse('<script>alert("successfully registered"),window.location="/login";</script>')
    return render(request,'Register.html')
def login(request):
    if request.method=="POST":
        a=request.POST['uname']
        b=request.POST['pswd']
        c=authenticate(username=a,password=b)
        request.session["user_id"]=a
        if c is not None and c.is_superuser==0:
            return redirect('/uHome/')
        elif c is not None and c.is_superuser==1:
            return render(request,'admin.html')
        else:
            return HttpResponse('<script>alert("incorrect"),window.location="/login";</script>')
    return render(request,'login.html')
def admin(request):
    return render(request,'admin.html')
def product(request):
    v=tbl_product.objects.all()
    return render(request,'product.html',{'a':v})
def addpro(request):
    if request.method=="POST":
        a=request.POST['name']
        b=request.POST['qn']
        f=request.FILES['photo']
        d=request.POST['price']
        e=tbl_product(Product_name=a,Quantity=b,product_photo=f,Price=d)
        e.save()
        return HttpResponse('<script>alert("Successfully Added"),window.location="/product";</script>')
    return render(request,'addpro.html')
def deletepro(request,id):
    a=tbl_product.objects.get(id=id)
    a.delete()
    return HttpResponse('<script>alert("deleted"),window.location="/product";</script>')
def updatepro(request,id):
    u=tbl_product.objects.get(id=id)
    if request.method=='POST':
        if len(request.FILES)!=0:
            if len(u.product_photo)>0:
                os.remove(u.product_photo.path)
        u.product_photo=request.FILES['photo']
        u.Product_name=request.POST['name']
        u.Quantity=request.POST['qn']
        u.Price=request.POST['price']
        u.save()
        return HttpResponse('<script>alert("Updated"),window.location="/product";</script>')
    return render(request,'product.html',{'b':u})  
def userview(request):
    c=tbl_customer.objects.all()
    return render(request,'customer.html',{'a':c})
def udelete(request,id):
    c=tbl_customer.objects.get(id=id)
    c.delete()
    return HttpResponse('<script>alert("deleted"),window.location="/view customer";</script>')
def uupdate(request,id):
    a=tbl_customer.objects.get(id=id)
    if request.method=='POST':
        a.First_name=request.POST['fname']
        a.Last_name=request.POST['lname']
        a.Address=request.POST['address']
        a.Place=request.POST['place']
        a.Email=request.POST['email']
        a.Phone=request.POST['phone']
        a.Username=request.POST['uname']
        a.save()
        return HttpResponse('<script>alert("updated successfully"),window.location="/view customer";</script>')
    return render(request,'customer.html',{'b':a})
    
            
    
def vieworder(request):
    o=tbl_order.objects.all()
    return render(request,'order.html',{'a':o})
def viewpayment(request):
    a=tbl_payment.objects.all()
    return render(request,'payment.html',{'p':a})
def uHome(request):
    b=tbl_product.objects.all()
    return render(request,'uHome.html',{'d':b})
def checkOut(request,id,pr):
    uid=request.session['user_id']
    p_id=id
    price=pr
    a=tbl_product.objects.get(id=id)
    p_name=a.Product_name
    p_photo=a.product_photo
    if request.method=='POST':
        qnty=request.POST['qn']
        amt=int(qnty)*int(price)
        q=tbl_order(Product_id=p_id,Product_name=p_name,Quantity=qnty,Amount=amt,status='Pending',User_id=uid)
        q.save()
        return HttpResponse('<script>alert("Order Request Send"),window.location="/uHome";</script>')
    return render(request,'checkOut.html',{'x':p_name,'y':p_photo})
def Logout(request):
    logout(request)
    return redirect('/')
def payment(request,id,pr,Product_name):
    c=request.session['user_id']
    order_id=id
    Amount=pr
    pname=Product_name
    d=tbl_order.objects.get(id=id)
    if request.method=='POST':
        b=request.POST['amount']
        c=tbl_payment(order_id=order_id,User_id=c,Amount=b,Status="paid")
        d.status="paid"
        d.save()
        c.save()
        return HttpResponse('<script>alert("payment successfully"),window.location="/uHome";</script>')
    return render(request,'pay.html',{'p': Amount,'Product':pname})
def confirm(request,id):
    a=tbl_order.objects.get(id=id)
    a.status="success"
    a.save()
    return HttpResponse('<script>alert("confirmed"),window.location="/order";</script>')
def myorder(request):
 uid=request.session["user_id"]
 a=tbl_order.objects.filter(User_id=uid)
 return render(request,'vieworder.html',{'b':a})
def reject(request,id):
    a=tbl_order.objects.get(id=id)
    a.status="Rejected"
    a.save()
    return HttpResponse('<script>alert("Rejected"),window.location="/order";</script>')
def transaction(request):
    uid=request.session["user_id"]
    a=tbl_order.objects.filter(User_id=uid)
    return render(request,'Transactions.html',{'T':a})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

                  
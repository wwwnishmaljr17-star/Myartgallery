from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import (
    loginTbl, userTbl, artistTbl, complaintsTbl, reviewTbl, 
    artistreviewTbl, designTbl, chatTbl, schedulesTbl, 
    bookingsTbl, productTbl, postTbl, comments, likeTbl, 
    orderTbl, paymentsTbl, ProductpaymentsTbl
)
import datetime
from django.core.serializers import json


def logout(request):
    auth.logout(request)
    return render(request,"index.html")


# Create your views here.
def login(request):
    return render(request,'index.html')

def adminHome(request):
    return render(request,'admin/index.html')

def admin2(request):
    return render(request,'admin/index2.html')

def loginPost(request):
    uname=request.POST["username"].strip()
    passw=request.POST["password"].strip()


    lo=loginTbl.objects.filter(username__iexact=uname,password=passw)
    if lo.exists():
        p=lo.first()
        request.session['lid'] = p.id
        if p.type =='admin':
            ob1=auth.authenticate(username= 'admin',password='admin')
            if ob1 is not None:
                auth.login(request,ob1)
            return  HttpResponse('''<script>alert('Logined');window.location='/adminHome'</script>''')

        elif p.type =='artist':
            ob1 = auth.authenticate(username='admin', password='admin')
            if ob1 is not None:
                auth.login(request, ob1)
            return  HttpResponse('''<script>alert('artist logined');window.location='/artistHome'</script>''')

        else:
            return  HttpResponse('''<script>alert('invalid');window.location='/'</script>''')

    else:
        return HttpResponse('''<script>alert('Invalid');window.location='/'</script>''')


@login_required(login_url='/')
def view_artist(request):
    ob=artistTbl.objects.all()
    return render(request,'admin/view artist.html',{'data':ob})
@login_required(login_url='/')

def accept_artist(request,id):
    ob=loginTbl.objects.get(id=id)
    ob.type='artist'
    ob.save()
    return HttpResponse('''<script>alert('accepted');window.location='/view_artist'</script>''')
@login_required(login_url='/')

def reject_artist(request,id):
    ob=loginTbl.objects.get(id=id)
    ob.type='artist'
    ob.delete()
    return HttpResponse('''<script>alert('rejected');window.location='/view_artist'</script>''')
@login_required(login_url='/')

def change_password(request):
    return render(request,'admin/change password.html')

# def change_passwordpost(request):
#     currpass=request.POST["currentPassword"]
#     newpass=request.POST["newPassword"]
#     conpass=request.POST["confirmPassword"]
#     c=loginTbl.objects.filter(id=request.session["lid"],password=currpass)
#     if c.exists():
#         if newpass==conpass:
#             c=loginTbl.objects.filter(id=request.session["lid"],password=currpass).update(password=conpass)
#             c.save()
#             return HttpResponse('<script>alert("successfully updated");window.location="/adminHome"</script>')
#         else:
#             return HttpResponse('<script>alert("password mismatch");window.location="/adminHome"</script>')
#     else:
#         return HttpResponse('<script>alert("invalid");window.location="/adminHome"</script>')
#
@login_required(login_url='/')
def change_passwordpost(request):
    currpass=request.POST["currentPassword"]
    newpass=request.POST["newPassword"]
    conpass=request.POST["confirmPassword"]
    c=loginTbl.objects.filter(id=request.session.get("lid"), password=currpass)
    if c.exists():
        if newpass==conpass:
            u=c.first()
            u.password=newpass
            u.save()
            return HttpResponse('<script>alert("successfully updated");window.location="/adminHome"</script>')
        else:
            return HttpResponse('<script>alert("password mismatch");window.location="/adminHome"</script>')
    else:
        return HttpResponse('<script>alert("invalid current password");window.location="/adminHome"</script>')



@login_required(login_url='/')

def artist_change_password(request):
    return render(request,'artist/change password.html')
@login_required(login_url='/')

@login_required(login_url='/')
def artist_change_passwordpost(request):
    currpass=request.POST["textfield"]
    newpass=request.POST["textfield2"]
    conpass=request.POST["textfield3"]
    c=loginTbl.objects.filter(id=request.session.get("lid"), password=currpass)
    if c.exists():
        if newpass==conpass:
            u=c.first()
            u.password=newpass
            u.save()
            return HttpResponse('<script>alert("successfully updated");window.location="/artistHome"</script>')
        else:
            return HttpResponse('<script>alert("password mismatch");window.location="/artistHome"</script>')
    else:
        return HttpResponse('<script>alert("invalid current password");window.location="/artistHome"</script>')


@login_required(login_url='/')

def view_user(request):
    a=userTbl.objects.all()
    return render(request,'admin/view user.html',{'data':a})
@login_required(login_url='/')

def view_complaints_reply(request):
    ob=complaintsTbl.objects.all()
    return render(request,'admin/view complaints and reply.html',{'val':ob})
@login_required(login_url='/')

def view_complaints_reply2(request,id):
    request.session['cid']=id
    ob=complaintsTbl.objects.get(id=request.session['cid'])
    return render(request,'admin/view complaints and reply 2.html')
@login_required(login_url='/')

def view_complaints_reply2post(request):
    reply=request.POST["textfield"]

    ob=complaintsTbl.objects.get(id=request.session['cid'])
    ob.reply=reply
    ob.save()
    return HttpResponse('''<script>alert('reply send sucessfully');window.location='/view_complaints_reply'</script>''')




@login_required(login_url='/')

def review_box(request):
    ob=artistreviewTbl.objects.all()
    print(ob)
    return render(request,'admin/review box.html',{'data':ob})

def artist_registration(request):
    return render(request,'admin/artist registration.html')

def artist_registrationpost(request):
    name=request.POST["textfield"]
    email=request.POST["textfield3"]
    phone=request.POST["textfield4"]
    place=request.POST["textfield5"]
    pin=request.POST["textfield6"]
    post=request.POST["textfield7"]
    uname=request.POST["textfield8"]
    passw=request.POST["textfield9"]
    image=request.FILES["file"]
    fs=FileSystemStorage()
    fp=fs.save(image.name,image)

    lo=loginTbl()
    lo.username=uname
    lo.password=passw
    lo.type='artist'
    lo.save()

    ob=artistTbl()
    ob.LOGINID=lo
    ob.name=name
    ob.place=place
    ob.image=fp
    ob.email=email
    ob.phone=phone
    ob.pin=pin
    ob.post=post
    ob.save()
    return HttpResponse('''<script>alert('registered sucessfully');window.location='/'</script>''')

@login_required(login_url='/')

def view_accepted_artist(request):
    return render(request,'admin/view accepted artist.html')

@login_required(login_url='/')

def add_design(request):
    return render(request,'artist/add design.html')

@login_required(login_url='/')

def add_designpost(request):
    name=request.POST["textfield"]
    desc=request.POST["textfield2"]
    image=request.FILES['file']

    fs=FileSystemStorage()
    fp=fs.save(image.name,image)

    ob = designTbl()
    ob.name = name
    ob.image = fp
    ob.description = desc
    ob.status='pending'
    ob.date=datetime.datetime.now()
    ob.ARTIST = artistTbl.objects.get(LOGINID_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert('Add sucsessfully');window.location='/view_design'</script>''')





@login_required(login_url='/')

def delete_design(request,id):
    request.session['did']=id
    ob=designTbl.objects.get(id=request.session['did'])
    ob.delete()
    return HttpResponse('''<script>alert('delete sucsessfully');window.location='/view_design'</script>''')


@login_required(login_url='/')

def add_product(request):
    return render(request,'artist/add product.html')
@login_required(login_url='/')

def add_productpost(request):
    name = request.POST["productName"]
    desc = request.POST["description"]
    price = request.POST["price"]
    work=request.FILES['workFile']

    fs = FileSystemStorage()
    fp = fs.save(work.name, work)


    ob=productTbl()
    ob.name=name
    ob.work=fp
    ob.description=desc
    ob.date=datetime.datetime.now().date()
    ob.amount=price
    ob.ARTIST=artistTbl.objects.get(LOGINID__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert('added sucsessfully');window.location='/view_product'</script>''')

@login_required(login_url='/')

def add_schedule(request):
    return render(request,'artist/add schedule.html')



@login_required(login_url='/')

def add_schedulepost(request):
    date=request.POST["textfield"]
    time=request.POST["textfield2"]


    ob = schedulesTbl()
    ob.ARTIST = artistTbl.objects.get(LOGINID_id=request.session['lid'])
    ob.date=date
    ob.time=time
    ob.save()
    return HttpResponse('''<script>alert('add sucsessfully');window.location='/view_shedule'</script>''')
@login_required(login_url='/')

def delete_schedule(request,id):
    ob=schedulesTbl.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('delete sucsessfully');window.location='/view_shedule'</script>''')


@login_required(login_url='/')

def edit_schedule(request,id):
    request.session['id']=id
    a=schedulesTbl.objects.get(id=id)
    return render(request,'artist/edit schedule.html',{'data':a})



@login_required(login_url='/')

def edit_schedulepost(request):
    date=request.POST["textfield"]
    time=request.POST["textfield2"]


    ob = schedulesTbl.objects.get(id=request.session['id'])
    ob.date=date
    ob.time=time
    ob.save()
    return HttpResponse('''<script>alert(' sucsessfully');window.location='/view_shedule'</script>''')

@login_required(login_url='/')

def view_booking(request):
    ob = bookingsTbl.objects.filter(SCHEDULE__ARTIST__LOGINID=request.session["lid"])
    return render(request,'artist/view booking.html',{"data":ob})


@login_required(login_url='/')
def accept_design(request,id):
    ob = bookingsTbl.objects.get(id=id)
    ob.status='accepted'
    ob.save()
    return HttpResponse('''<script>alert('accpeted sucsessfully');window.location='/view_booking'</script>''')


@login_required(login_url='/')

def reject_design(request,id):
    ob = bookingsTbl.objects.get(id=id)
    ob.status='rejected'
    ob.save()
    return HttpResponse('''<script>alert('rejected sucsessfully');window.location='/view_booking'</script>''')





@login_required(login_url='/')

def view_comment_and_like(request,pid):
    ob=comments.objects.filter(POSTID=pid)
    return render(request,'artist/view comment and like.html',{"data":ob})
@login_required(login_url='/')

def view_like(request,pid):
    ob=likeTbl.objects.filter(POSTID=pid)
    return render(request, 'artist/like.html',{"data":ob})
@login_required(login_url='/')
def view_design(request):
    ob = designTbl.objects.filter(ARTIST__LOGINID_id=request.session['lid'])
    return render(request, 'artist/view design.html', { 'data': ob })
@login_required(login_url='/')

def view_other_work_and_like(request):
    ob = postTbl.objects.exclude(ARTIST__LOGINID=request.session["lid"])
    return render(request,'artist/view other work and like.html',{'data':ob})
@login_required(login_url='/')

def payment_details(request):
    lid = request.session.get('lid')
    order_payments = paymentsTbl.objects.filter(ORDER__product__ARTIST__LOGINID=lid)
    direct_payments = ProductpaymentsTbl.objects.filter(PRODUCT__ARTIST__LOGINID=lid)
    
    # Simple combination for display
    combined_data = []
    for p in order_payments:
        combined_data.append({
            'id': p.id,
            'item': p.ORDER.product.name,
            'date': p.date,
            'amount': p.amount,
            'status': p.status
        })
    for p in direct_payments:
        combined_data.append({
            'id': p.id,
            'item': p.PRODUCT.name,
            'date': p.date,
            'amount': p.amount,
            'status': p.status
        })
        
    return render(request, 'artist/view payment details.html', {'data': combined_data})
@login_required(login_url='/')
def view_post(request):
    ob = postTbl.objects.filter(ARTIST__LOGINID_id=request.session['lid'])
    return render(request,'artist/view post.html',{'data': ob})
@login_required(login_url='/')

def edit_post(request,id):

    request.session['id'] = id
    a = postTbl.objects.get(id=id)
    return render(request, 'artist/editpost.html', {'data': a})
@login_required(login_url='/')

def edit_postpost(request):
    try:
        name = request.POST.get("postname")
        desc = request.POST.get("textfield2")
        pid = request.session.get('id')
        
        ob = postTbl.objects.filter(id=pid).first()
        if not ob:
            return HttpResponse('''<script>alert('Post not found');window.location='/view_post'</script>''')

        if 'file' in request.FILES:
            design = request.FILES['file']
            fs = FileSystemStorage()
            fp = fs.save(design.name, design)
            ob.design = fp

        ob.postname = name
        ob.post = desc
        ob.date = datetime.date.today()
        
        lid = request.session.get('lid')
        artist = artistTbl.objects.filter(LOGINID_id=lid).first()
        if artist:
            ob.ARTIST = artist
            
        ob.save()
        return HttpResponse('''<script>alert('Updated successfully');window.location='/view_post'</script>''')
    except Exception as e:
        print(e)
        return HttpResponse('''<script>alert('An error occurred');window.location='/view_post'</script>''')
@login_required(login_url='/')

def delete_post(request,id):
    ob=postTbl.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('delete sucsessfully');window.location='/view_post'</script>''')


@login_required(login_url='/')

def add_post(request):
    return render(request,'artist/add post.html')
@login_required(login_url='/')

def add_postpost(request):
    try:
        name = request.POST.get("textfield")
        desc = request.POST.get("textfield2")
        design = request.FILES.get('file')

        if not design:
             return HttpResponse('''<script>alert('Please select a file');window.location='/add_post'</script>''')

        fs = FileSystemStorage()
        fp = fs.save(design.name, design)

        lid = request.session.get('lid')
        artist = artistTbl.objects.filter(LOGINID_id=lid).first()
        if not artist:
            return HttpResponse('''<script>alert('Artist profile not found');window.location='/add_post'</script>''')

        ob = postTbl()
        ob.postname = name
        ob.design = fp
        ob.post = desc
        ob.date = datetime.date.today()
        ob.ARTIST = artist
        ob.save()
        return HttpResponse('''<script>alert('Added successfully');window.location='/view_post'</script>''')
    except Exception as e:
        print(e)
        return HttpResponse(f'''<script>alert('An error occurred');window.location='/add_post'</script>''')
    return HttpResponse("ok")
@login_required(login_url='/')

def view_product(request):
    a=productTbl.objects.filter(ARTIST__LOGINID__id=request.session['lid'])
    return render(request,'artist/view product.html',{'data': a})
@login_required(login_url='/')

def edit_product(request,id):
    request.session['pid'] = id
    a = productTbl.objects.get(id=id)
    return render(request, 'artist/edit product.html', {'data': a})
@login_required(login_url='/')

def edit_productpost(request):
    name = request.POST.get("productName")
    desc = request.POST.get("description")
    price = request.POST.get("price")

    pid = request.session.get('pid')
    ob = productTbl.objects.filter(id=pid).first()
    if not ob:
        return HttpResponse('''<script>alert('Product not found');window.location='/view_product'</script>''')

    if 'workFile' in request.FILES:
        work = request.FILES['workFile']
        fs = FileSystemStorage()
        fp = fs.save(work.name, work)
        ob.work = fp

    ob.name = name
    ob.description = desc
    ob.date = datetime.datetime.now()
    ob.amount = price
    
    lid = request.session.get('lid')
    artist = artistTbl.objects.filter(LOGINID_id=lid).first()
    if artist:
        ob.ARTIST = artist
    ob.save()
    return HttpResponse('''<script>alert('Updated successfully');window.location='/view_product'</script>''')
@login_required(login_url='/')

def delete_product(request,id):
    ob=productTbl.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('delete sucsessfully');window.location='/view_product'</script>''')

@login_required(login_url='/')

def view_profile_and_update(request):
    lid = request.session.get('lid')
    profile = artistTbl.objects.filter(LOGINID_id=lid).first()
    if not profile:
        from .models import loginTbl
        login_obj = loginTbl.objects.filter(id=lid).first()
        if not login_obj:
            return HttpResponse('''<script>alert('Invalid session');window.location='/'</script>''')
        profile = artistTbl.objects.create(
            LOGINID=login_obj,
            name=login_obj.username,
            email="",
            phone=0,
            place="",
            pin=0,
            post=""
        )
    return render(request, 'artist/view profile and update.html', {'profile': profile})

@login_required(login_url='/')

def view_profile_and_updatepost(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    place = request.POST.get("place")
    pin = request.POST.get("pin")
    post = request.POST.get("post")

    lid = request.session.get('lid')
    c = artistTbl.objects.filter(LOGINID_id=lid).first()
    if not c:
        return HttpResponse('''<script>alert('Profile not found');window.location='/view_profile_and_update'</script>''')

    if 'image' in request.FILES:
        image = request.FILES["image"]
        fs = FileSystemStorage()
        fp = fs.save(image.name, image)
        c.image = fp
    c.name=name

    c.email=email
    c.phone=phone
    c.place=place
    c.pin=pin
    c.post=post
    c.save()
    return HttpResponse('''<script>alert('profile updated');window.location='/view_profile_and_update'</script>''')
@login_required(login_url='/')

def view_shedule(request):
    a=schedulesTbl.objects.filter(ARTIST__LOGINID_id=request.session['lid'])
    return render(request,'artist/view schedule.html',{'data':a})
@login_required(login_url='/')

def artistHome(request):
    return render(request,'artist/index.html')



def artist2(request):
    return render(request, 'artist/index2.html')

# =============================================


def logincode(request):
    uname=request.POST["username"]
    passw=request.POST["password"]


    lo=loginTbl.objects.filter(username=uname,password=passw)
    if lo.exists():
        p=loginTbl.objects.get(username=uname,password=passw)
        if p.type =='user':

            return JsonResponse({'status': 'ok','lid':p.id,'type':p.type})


        else:
            return JsonResponse({'status': 'notok'})

    else:
        return JsonResponse({'status': 'notok'})


def registrationcode(request):
    try:
        print(request.POST,"uuuki")
        name=request.POST['name']

        email=request.POST['email']
        phone=request.POST['phone']
        place = request.POST['place']
        pin = request.POST['pin']
        password=request.POST['password']

        lob1=loginTbl()
        lob1.username = email
        lob1.password = password
        lob1.type = 'user'
        lob1.save()

        lob=userTbl()
        lob.name = name
        lob.place =place

        lob.pin = pin
        lob.phone = phone
        lob.email = email
        lob.LOGIN =lob1
        lob.save()
        print("uuuuuuuuu",lob)
        return JsonResponse({'status':'ok'})
    except:
        return JsonResponse({"task": "invalid"})

def user_view_artist(request):
    ob=artistTbl.objects.all()
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'id':i.id,'lid':i.LOGINID.id,'name':i.name,'image':str(i.image.url),'email':i.email,'phone':i.phone}
        mdata.append(data)
    print(mdata)
    return JsonResponse({"status":"ok","data":mdata})


def user_view_post(request):
    ob=postTbl.objects.all()
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'id':i.id,'ARTIST':i.ARTIST.name,'post':i.post,
              'design':request.build_absolute_uri(i.design.url),
              'date':str(i.date),'postname':i.postname}
        mdata.append(data)
    print(mdata)
    return JsonResponse({"status":"ok","data":mdata})







def user_view_design(request):
    ob=designTbl.objects.all()
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'id':i.id,'ARTIST':i.ARTIST.name,'date':i.date,'name':i.name,'image':str(i.image.url),'description':i.description,'status':i.status}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})



def user_view_product(request):
    ob=productTbl.objects.all()
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'id':i.id,'ARTIST':i.ARTIST.name,'date':i.date,'name':i.name,'work':str(i.work.url),'description':i.description,"price":i.amount}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})



def user_view_schedule(request):
    aid=request.POST['aid']
    ob=schedulesTbl.objects.filter(ARTIST_id=aid)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'id':i.id,'date':i.date,'time':i.time,'status':i.status}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})



def user_add_booking(request):
    lid = request.POST['lid']
    did = request.POST['did']
    lob = bookingsTbl()
    lob.USERID = userTbl.objects.get(LOGIN__id=lid)
    lob.SCHEDULE = schedulesTbl.objects.get(id=did)
    lob.status='pending'
    lob.date = datetime.datetime.today().now()
    lob.save()
    return JsonResponse({'status': 'ok'})





def user_view_booking(request):
    lid = request.POST['lid']
    ob=bookingsTbl.objects.filter(USERID__LOGIN_id=lid)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'id':i.id,'date':i.date,'DESIGN':i.SCHEDULE.date,'status':i.status, 'payment_status': i.payment_status}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})



def user_sendfeedback(request):
    review = request.POST['review']
    rating = request.POST['rating']
    lid = request.POST['lid']
    lob = reviewTbl()
    lob.USER = userTbl.objects.get(LOGIN_id=lid)
    lob.review = review
    lob.rating = rating
    lob.date = datetime.today()
    lob.save()
    return JsonResponse({'status': 'ok'})


def user_artistsendfeedback(request):
    review = request.POST['review']
    rating = request.POST['rating']
    aid = request.POST['aid']

    lid = request.POST['lid']
    lob = artistreviewTbl()
    lob.USERID = userTbl.objects.get(LOGIN_id=lid)
    lob.ARTIST = artistTbl.objects.get(id=aid)
    lob.review = review
    lob.rating = rating
    lob.date = datetime.datetime.today()
    lob.save()
    return JsonResponse({'status': 'ok'})




def user_view_rating(request):
    lid = request.POST['lid']
    ob=artistreviewTbl.objects.filter(USERID__LOGIN_id=lid)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'id':i.id,'NAME':i.ARTIST.name,'review':i.review,'rating':i.rating,'date':i.date}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})






# def user_view_post(request):
#     lid = request.POST['lid']
#     ob=postTbl.objects.all()
#     print(ob,"HHHHHHHHHHHHHHH")
#     mdata=[]
#     for i in ob:
#         data={'ARTIST':i.ARTIST,'DESIGN':i.DESIGNID.name,'post':i.post,'date':i.date,'postname':i.postname}
#         mdata.append(data)
#         print(mdata)
#     return JsonResponse({"status":"ok","data":mdata})
#



def user_add_comment(request):
    commentss = request.POST['comments']
    lid = request.POST['lid']
    pid = request.POST['pid']
    lob = comments()
    lob.USERID = userTbl.objects.get(LOGIN_id=lid)
    lob.POSTID = postTbl.objects.get(id=pid)
    lob.comments = commentss
    lob.date = datetime.datetime.now()
    lob.save()
    return JsonResponse({'task': 'ok'})

def user_view_comment(request):
    pid = request.POST['pid']
    ob=comments.objects.filter(POSTID_id=pid)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'id':i.id,'comments':i.comments,'date':i.date,}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})



def user_add_like(request):
    like = request.POST['like']
    lid = request.POST['lid']
    pid = request.POST['pid']
    lob = likeTbl()
    lob.USER = userTbl.objects.get(LOGIN_id=lid)
    lob.POSTID = postTbl.objects.get(id=pid)
    lob.like = like
    lob.date = datetime.datetime.now()
    lob.save()
    return JsonResponse({'task': 'ok'})



def add_like(request):
    if request.method == 'POST':
        try:
            lid = request.POST.get('lid')
            post_id = request.POST.get('post_id')

            if not lid or not post_id:
                return JsonResponse({'status': 'error', 'message': 'Missing parameters'})

            lid = int(lid)
            post_id = int(post_id)

            user = userTbl.objects.filter(LOGINID_id=lid).first()
            post = postTbl.objects.filter(id=post_id).first()

            if not user or not post:
                return JsonResponse({'status': 'error', 'message': 'User or Post not found'})

            existing_like = likeTbl.objects.filter(USERID=user, POSTID=post).first()

            if existing_like:
                existing_like.delete()
                return JsonResponse({'status': 'ok', 'message': 'Disliked'})

            new_like = likeTbl(
                USERID=user,
                POSTID=post,
                date=datetime.date.today()
            )
            new_like.save()

            return JsonResponse({'status': 'ok', 'message': 'Post liked successfully!'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



def user_change_password_post(request):
    lid=request.POST['lid']
    old=request.POST['old']
    new=request.POST['newp']
    confirm=request.POST['confirm']

    a=loginTbl.objects.filter(id=lid,password=old)
    if a.exists():
        if new == confirm:
            ab = loginTbl.objects.filter(id=lid, password=old).update(password=confirm)

            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'not ok'})
    else:
        return JsonResponse({'status': 'nok'})





def user_view_profile(request):
    lid=request.POST['lid']
    a=userTbl.objects.get(LOGIN_id=lid)
    return JsonResponse({'status': 'ok',
                         'name':a.name,'email':a.email,'phone':str(a.phone),'place':a.place,'pin':str(a.pin)
                         })


def user_edit_profile(request):
    print(request.POST,"uuuki")
    name=request.POST['name']
    lid=request.POST['lid']

    email=request.POST['email']
    phone=request.POST['phone']
    place = request.POST['place']
    pin = request.POST['pin']



    lob=userTbl.objects.get(LOGIN_id=lid)
    lob.name = name
    lob.place =place

    lob.pin = pin
    lob.phone = phone
    lob.email = email
    lob.save()
    print("uuuuuuuuu",lob)
    return JsonResponse({'status':'ok'})



def user_artistsendcomplaint(request):
    com = request.POST['complaint']

    lid = request.POST['lid']
    lob = complaintsTbl()
    lob.USERID = userTbl.objects.get(LOGIN_id=lid)
    lob.complaint = com
    lob.date = datetime.datetime.today()
    lob.reply= 'pending'
    lob.save()
    return JsonResponse({'task': 'ok'})



def user_view_complaint(request):
    lid = request.POST['lid']
    ob=complaintsTbl.objects.filter(USERID__LOGIN_id=lid)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'id':i.id,'complaint':i.complaint,'reply':i.reply,'date':str(i.date)}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})





def chatwithuser(request):
    ob = userTbl.objects.all()
    return render(request,"artist/fur_chat.html",{'val':ob})

def chatview(request):
    ob = userTbl.objects.all()
    d = []
    default_img = "placeholder"
    for i in ob:
        r = {
            "name": i.name,
            "email": i.email,
            "loginid": i.LOGIN.id,
            "photo": default_img
        }
        d.append(r)
    return JsonResponse(d, safe=False)




def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=chatTbl()
    ob.from_id=loginTbl.objects.get(id=request.session['lid'])
    ob.to_id=loginTbl.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.datetime.now().strftime("%Y-%m-%d")
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist



def coun_msg(request,id):

    ob1=chatTbl.objects.filter(from_id__id=id,to_id__id=request.session['lid'])
    ob2=chatTbl.objects.filter(from_id__id=request.session['lid'],to_id__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.from_id.id,"msg":i.message,"date":i.date,"chat_id":i.id})

    obu = userTbl.objects.get(LOGIN__id=id)
    default_img = "placeholder"
    return JsonResponse({
        "data": res,
        "name": obu.name,
        "user_lid": obu.LOGIN.id,
        "photo": default_img
    })

#
# def User_viewchat(request):
#     fromid = request.POST["from_id"]
#     toid = request.POST["to_id"]
#     res = chat_table.objects.filter(Q(fromid_id=fromid, toid_id=toid) | Q(fromid_id=toid, toid_id=fromid))
#     l = []
#
#     for i in res:
#         l.append({"id": i.id, "msg": i.msg, "from": i.fromid_id, "date": i.date, "to": i.toid_id})
#
#     return JsonResponse({"status":"ok",'data':l})
#
#
# def User_sendchat(request):
#     FROM_id=request.POST['from_id']
#     TOID_id=request.POST['to_id']
#     print(FROM_id)
#     print(TOID_id)
#     msg=request.POST['message']
#
#     from  datetime import datetime
#     c=chat_table()
#     c.fromid_id=FROM_id
#     c.toid_id=TOID_id
#     c.msg=msg
#     c.date=datetime.now()
#     c.save()
#     return JsonResponse({'status':"ok"})

def viewchat(request):
    print(request.POST)
    fromid = request.POST['from_id']
    toid=request.POST['to_id']
    ob1 = chatTbl.objects.filter(from_id=fromid, to_id=toid)
    ob2 = chatTbl.objects.filter(from_id=toid, to_id=fromid)
    combined_chat = ob1.union(ob2)
    combined_chat = combined_chat.order_by('id')
    res = []
    for i in combined_chat:
        res.append({'msg': i.message, 'fromid': i.from_id.id, 'toid': i.to_id.id, 'date':i.date})
    print(res,"===============================++++++++++++++++++++++++++++++++++========================")
    return JsonResponse({"status": "ok", "data": res})


def sendchat(request):
    print(request.POST)
    msg=request.POST['message']
    fromid=request.POST['fromid']
    toid=request.POST['toid']
    ob=chatTbl()
    ob.message=msg
    ob.from_id=loginTbl.objects.get(id=fromid)
    ob.to_id=loginTbl.objects.get(id=toid)
    ob.date=datetime.datetime.now().date()
    ob.save()
    return JsonResponse({"status": "ok"})

#
# def order_product(request):
#     lid=request.POST["lid"]
#     pid=request.POST["pid"]


import numpy as np

def cosine_similarity(vec1, vec2):
    # Convert input vectors to numpy arrays (if not already)
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    # Compute the dot product of the two vectors
    dot_product = np.dot(vec1, vec2)

    # Compute the L2 norm (magnitude) of each vector
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)

    # Compute the cosine similarity
    similarity = dot_product / (norm_vec1 * norm_vec2)

    return similarity

def recomendation(request):

    lid = request.POST['lid']
    ob=artistreviewTbl.objects.filter(USERID__LOGIN__id=lid,rating__gte=2.5)
    aids=[]
    print(aids)
    for i in ob:
        if i.ARTIST.id not in aids:
            aids.append(i.ARTIST.id)
    obu=artistreviewTbl.objects.filter(ARTIST__id__in=aids,rating__gte=2.5).exclude(USERID__LOGIN__id=lid)
    uids=[]
    for i in obu:
        uids.append(i.USERID.id)
    print("uids")
    print(uids)
    uvec=[]
    for i in aids:
        uvec.append(1)
    clisdt=[]
    for i in uids:
        r=[]
        for j in aids:
            ob = artistreviewTbl.objects.filter(USERID__id=i,ARTIST__id=j, rating__gte=2.5)
            if len(ob)>0:
                r.append(1)
            else:
                r.append(0)
        clisdt.append([i,r])

    simlist=[]
    print("simlist")
    print(simlist)
    for i in clisdt:
        dis=cosine_similarity(i[1],uvec)
        simlist.append({"id":i[0],"dis":dis})
    simlist.sort(key=lambda x: x["dis"])
    suids=[]
    for i in range(0,len(simlist)):
        suids.append(simlist[i]['id'])
        if i>=3:
            break
    ob = artistreviewTbl.objects.filter(USERID__id__in=suids, rating__gte=2.5)
    saids=[]
    for i in ob:
        if i.ARTIST.id not in saids:
            saids.append(i.ARTIST.id)
    ob=artistTbl.objects.filter(id__in=saids).exclude(id__in=aids)

    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'id':i.id,'lid':i.LOGINID.id,'name':i.name,'image':str(i.image.url),'email':i.email,'phone':i.phone}
        mdata.append(data)
    print(mdata)
    return JsonResponse({"status":"ok","data":mdata})


def payment(request):
    if request.method == 'POST':
        ptype = request.POST.get('type', 'product')
        pid = request.POST.get('id', request.POST.get('sid'))
        lid = request.POST.get('lid')

        if not pid or not lid:
            return HttpResponse("Missing required parameters", status=400)

        try:
            if ptype == 'booking':
                booking = bookingsTbl.objects.get(id=pid)
                booking.payment_status = 'paid'
                booking.save()
                return HttpResponse("Booking payment recorded successfully")

            elif ptype == 'product':
                product = productTbl.objects.get(id=pid)
                amount = product.amount
                
                # Create a new Payment record
                payment_record = ProductpaymentsTbl(
                    PRODUCT=product,
                    date=datetime.datetime.now().date(),
                    status='Paid',
                    amount=amount,
                )
                payment_record.save()
                return HttpResponse("Product payment recorded successfully")
            
            else:
                return HttpResponse("Invalid payment type", status=400)
                
        except Exception as e:
            print(e)
            return HttpResponse(f"Error processing payment: {str(e)}", status=500)

    else:
        return HttpResponse("Invalid request method", status=405)


def add_productpost(request):
    try:
        name = request.POST.get("productName")
        desc = request.POST.get("description")
        price = request.POST.get("price")
        work = request.FILES.get('workFile')

        if not work:
             return HttpResponse('''<script>alert('Please select a file');window.location='/add_product'</script>''')

        fs = FileSystemStorage()
        fp = fs.save(work.name, work)

        lid = request.session.get('lid')
        artist = artistTbl.objects.filter(LOGINID_id=lid).first()
        if not artist:
            return HttpResponse('''<script>alert('Artist profile not found');window.location='/add_product'</script>''')

        ob = productTbl()
        ob.name = name
        ob.work = fp
        ob.description = desc
        ob.amount = price
        ob.date = datetime.datetime.now()
        ob.ARTIST = artist
        ob.save()
        return HttpResponse('''<script>alert('Product added successfully');window.location='/view_product'</script>''')
    except Exception as e:
        print(e)
        return HttpResponse(f'''<script>alert('An error occurred');window.location='/add_product'</script>''')

def add_schedulepost(request):
    try:
        date = request.POST.get("date")
        time = request.POST.get("time")

        lid = request.session.get('lid')
        artist = artistTbl.objects.filter(LOGINID_id=lid).first()
        if not artist:
            return HttpResponse('''<script>alert('Artist profile not found');window.location='/view_shedule'</script>''')

        ob = schedulesTbl()
        ob.date = date
        ob.time = time
        ob.status = 'available'
        ob.ARTIST = artist
        ob.save()
        return HttpResponse('''<script>alert('Schedule added successfully');window.location='/view_shedule'</script>''')
    except Exception as e:
        print(e)
        return HttpResponse('''<script>alert('An error occurred');window.location='/add_schedule'</script>''')

def add_designpost(request):
    try:
        name = request.POST.get("name")
        desc = request.POST.get("description")
        image = request.FILES.get('image')

        if not image:
             return HttpResponse('''<script>alert('Please select an image');window.location='/add_design'</script>''')

        fs = FileSystemStorage()
        fp = fs.save(image.name, image)

        lid = request.session.get('lid')
        artist = artistTbl.objects.filter(LOGINID_id=lid).first()
        if not artist:
            return HttpResponse('''<script>alert('Artist profile not found');window.location='/add_design'</script>''')

        ob = designTbl()
        ob.name = name
        ob.image = fp
        ob.description = desc
        ob.date = datetime.date.today()
        ob.ARTIST = artist
        ob.status = 'pending'
        ob.save()
        return HttpResponse('''<script>alert('Design added successfully');window.location='/view_design'</script>''')
    except Exception as e:
        print(e)
        return HttpResponse('''<script>alert('An error occurred');window.location='/add_design'</script>''')

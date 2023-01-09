from django.shortcuts import render,redirect
from .forms import signupform,notesform
from .models import usersignup
from django.contrib.auth import logout
from django.core.mail import send_mail
from NotesProject import settings
import random
import requests

# Create your views here.
def index(request):
    user=request.session.get('user')
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=signupform(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")

                # Email Sending Code
                #otp=random.randint(1111,9999)
                #send_mail(subject='Welcome!',message=f'Hello User\nYour account has been created withg us!\nYour one time password is {otp}\n\nEnjoy our services.\n\nIf any query or help regarding, Please contact us\n\n+91 9724799469 | sanket@gmail.com',from_email=settings.EMAIL_HOST_USER,recipient_list=[request.POST['username']])
                #return redirect('notes')
                return redirect('/')
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']

            user=usersignup.objects.filter(username=unm,password=pas)
            uid=usersignup.objects.get(username=unm) 
            print(uid.id) #get current userID
            if user: #true
                print("Login Successfully!")

                # SMS Sending Code

                """otp=random.randint(1111,9999)
                url = "https://www.fast2sms.com/dev/bulkV2"
                #querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","variables_values":f"{otp}","route":"otp","numbers":"9426046976"}
                querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","message":f"Your account has been login, Your OTP is {otp}\nIf you, please ignor this msg, or confirm this.","language":"english","route":"q","numbers":"9426046976"}
                headers = {
                    'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)"""   

                request.session['user']=unm
                request.session['uid']=uid.id #get current userID
                return redirect('notes')
            else:
                print("Error!Username or Password is wrong!")
    return render(request,'index.html',{'user':user})

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        newnotes=notesform(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been uploaded!")
        else:
            print(newnotes.errors)
    return render(request,'notes.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

def updateprofile(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    cid=usersignup.objects.get(id=uid)
    if request.method=='POST':
        updateuser=signupform(request.POST)
        if updateuser.is_valid():
            updateuser=signupform(request.POST,instance=cid)
            updateuser.save()
            print("Your profile has been updated!")
        else:
            print(updateuser.errors)
    return render(request,'updateprofile.html',{'user':user,'uid':usersignup.objects.get(id=uid)})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def demo1(request):
    if request.method == 'POST':
        uname=request.POST['Username']
        name1=request.POST['name1']
        name2=request.POST['name2']
        email = request.POST['Email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'username taken')
                return redirect('demo1')

            else:
                user=User.objects.create_user(username=uname,password=pass1,email=email,first_name=name1,last_name=name2)
                user.save();
                return  redirect('login')
            print("user created")
        else:
            messages.info(request,'password not matching')
            return  redirect('demo1')
        return redirect('/')



    return render(request,'demo1.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass1']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return  redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return  redirect('login')
    return  render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
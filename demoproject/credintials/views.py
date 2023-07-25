from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.







def loginpg(request):
 if request.method=='POST':
        username=request.POST['username']
        pswd=request.POST['password']
        user=auth.authenticate(username=username,password=pswd)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"INVALID CREDENTIALS")
            return  redirect('loginpg')

 return render(request,"login.html")





def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME TAKEN")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"EMAIL TAKEN")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email,
                                            password=password)

                user.save();
                return redirect('loginpg')
        else:
            messages.info(request,"PASSWORD IS NOT MATCHING")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

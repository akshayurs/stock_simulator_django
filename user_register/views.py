


from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"login.html")

def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        Email=request.POST["Email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]

        if User.objects.filter(username=username):
            messages.error(request,"username already exist")
            return redirect("home")

        if User.objects.filter(email=Email):
            messages.error(request,"email already exist")
            return redirect("home")
        
        if len(username)>16:
            messages.error(request,"username is too long")
            
        
        if pass1!=pass2:
            messages.error(request,"password not matching")
            return redirect("home")
        if not username.isalnum():
            messages.error(request,"invalid username")
            return redirect("home")
        
        myuser = User.objects.create_user(username,Email,pass1)
        myuser.save()
        messages.success(request,"our account has been created successfully")
        return redirect('home')


    return render(request,"login.html")    

def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
       
        pass1=request.POST['pass1']
         
        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return render(request,"index.html")
        else:
            messages.error(request,"incorrect password or email")
            return redirect('signin')
    
    
    
    return render(request,"login.html")    

def signout(request):
     logout(request)
     messages.success(request,"logout success")
     return redirect("home")
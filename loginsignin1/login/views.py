from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def homepage(request):
    return render(request, "index.html")

def siguppage(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        compassword = request.POST.get("comfrompassword")

        if password!=compassword:
            my_user=User.objects.create_user(uname,email,password)
            my_user.save()
            return redirect('login')
            # return HttpResponse("Your password and confrom password are not Same!!")
        if password==compassword:

            return HttpResponse("Your password and confrom password are not Same!!")

        # if password != compassword:
        #     messages.error(request, "Your password and comfrom password do not match")
        #     return redirect('signup')  # Assuming you have a 'signup' URL pattern

        # else:
        #     my_user = User.objects.create_user(uname, email, password)
        #     # No need to call save() here, create_user already saves the user
        #     messages.success(request, "Account created successfully. You can now log in.")
        #     return redirect('login')
       

    return render(request, "signin.html")

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('email')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            # login(request,user)
            # return redirect('home')
            return HttpResponse ("Username or Password is incorrect!!!")
        else:
            login(request,user)
            return redirect('home')
            # return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')
        
    
    # return render(request, "login.html")

def logoutpage(request):
    logout(request)
    return redirect('login')
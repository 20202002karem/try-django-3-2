from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpRequest
# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {'form':form}
    return render(request,'accounts/login.html/', context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login/')
    return render(request,'accounts/logout.html')

def register_view(requset):
    form = UserCreationForm(requset.POST or None)
    print("qqqqqqqqqqqqqqqqq")
    if form.is_valid():
        print("qqqqqqqqqqqqqqqqq")
        form.save()
        return redirect("/login/")
    context={'form':form}
    return render(requset,"accounts/register.html",context=context)

















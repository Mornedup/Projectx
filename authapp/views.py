from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('Success')# Redirect to a success page.
        else:
            return redirect('login', err='Account disabled')# Return a 'disabled account' error message
    else:
        return redirect('login', err='Invalid login username or password')# Return an 'invalid login' error message.

def logged_out():
    logout(request)
    return redirect('logged_out')# Redirect to a success page.

#def create_acc():

#def profile():

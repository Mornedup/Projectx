from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, ProfileEditForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form=ProfileEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileEditForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form=PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user=form.user)
            return redirect('view_profile')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

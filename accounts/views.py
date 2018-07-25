from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, ProfileEditForm, UserProfileEditForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth import update_session_auth_hash, login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('post_list')
    else:
        form = AuthenticationForm(request)
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def view_profile(request):
    args = {'user': request.user, }
    return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        Profileform = ProfileEditForm(request.POST, instance=request.user)
        Userprofile = UserProfileEditForm(request.POST, instance=request.user)
        if (Profileform.is_valid() and Userprofile.is_valid()):
            Profileform.save()
            Userprofile.save()
            return redirect('view_profile')
    else:
        Profileform = ProfileEditForm(instance=request.user)
        Userprofile = UserProfileEditForm(instance=request.user)
        args = {'Userform': Profileform, 'Profileform':Userprofile}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
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

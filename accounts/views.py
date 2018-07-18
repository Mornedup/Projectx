from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, ProfileEditForm
from django.contrib.auth.models import User

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
            return redirect('/accounts/profile')
    else:
        form = ProfileEditForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

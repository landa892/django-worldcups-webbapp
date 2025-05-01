from django.views.generic import CreateView, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, ProfileForm
from .models import Profile

class SignUpView(CreateView):
    form_class = UserRegisterForm
    template_name = 'signup.html'
    success_url = '/accounts/login/'

def login_view(request):
    
    from django.contrib.auth.forms import AuthenticationForm
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

@login_required
def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        uform = UserRegisterForm(request.POST, instance=request.user)
        pform = ProfileForm(request.POST, request.FILES, instance=profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            return redirect('profile')
    else:
        uform = UserRegisterForm(instance=request.user)
        pform = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'uform':uform, 'pform':pform})

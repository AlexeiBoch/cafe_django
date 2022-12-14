from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import logout, login

from users.forms import RegisterForm, ChangePasswordForm

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html')
    

class LoginExtendedView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
        
        
class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = RegisterForm()
        return render(request, 'users/register.html', {'form':form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        return render(request, 'users/register.html', {'form':form})
    
    
def logout_func(request):
    logout(request)
    return redirect('/')


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'users/password_change.html'
    
    
class ChangePasswordDoneView(PasswordChangeView):
    template_name = 'users/password_change_done.html'
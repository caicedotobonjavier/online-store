from django.shortcuts import render
#
from .models import User
#
from .forms import UserForm, LoginUserForm, ActivateUserForm, VerifyUserForm
#
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView, View
#
from .functions import generate_code, send_mail_register, send_mail_verify
#
from datetime import datetime, timezone
#
import pyotp
#
from django.urls import reverse_lazy, reverse
#
from django.http import HttpResponseRedirect
#
from django.contrib.auth import authenticate, login, logout
#
from django.contrib.auth.mixins import LoginRequiredMixin
#
from django.contrib.auth.decorators import login_required
#
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


class RegisterUserView(FormView):
    template_name = 'users/register_user.html'
    form_class = UserForm
    

    def form_valid(self, form):

        code = generate_code()
        code_otp = pyotp.random_base32()  

        user = User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['full_name'],
            form.cleaned_data['password1'],
            date_birth = form.cleaned_data['date_birth'],
            address = form.cleaned_data['address'],
            phone = form.cleaned_data['phone'],
            marketingaccept = form.cleaned_data['marketingaccept'],
            cod_activated = code,        
            otp_base32 = code_otp
        )

        send_mail_register(form.cleaned_data['full_name'], form.cleaned_data['email'], code, user.user_id)


        return HttpResponseRedirect(
            reverse(
                    'users_app:activate',
                    kwargs= {'pk': user.user_id}
                )
        )


class ActivateUserView(FormView):
    template_name = 'users/activate_user.html'
    form_class = ActivateUserForm
    success_url = reverse_lazy('users_app:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = User.objects.get(user_id=self.kwargs['pk'])
        return context
    

    def get_form_kwargs(self):
        kwargs = super(ActivateUserView, self).get_form_kwargs()
        kwargs.update({'pk': self.kwargs['pk']})
        return kwargs
    
    def form_valid(self, form):
        usuario = User.objects.get(user_id=self.kwargs['pk'])    
        usuario.is_active = True   
        usuario.is_staff = True
        usuario.save()       

        return super(ActivateUserView, self).form_valid(form)



class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('home_app:index')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)

        base32 = user.otp_base32        
        totp = pyotp.TOTP(base32).now()
        print(totp)
        user.login_otp = make_password(totp)
        user.created_at = datetime.now(timezone.utc)
        user.use_login_otp = False        

        user.save(update_fields=['created_at', 'use_login_otp', 'login_otp'])
        
        send_mail_verify(user.user_id, totp, email)

        return HttpResponseRedirect(
            reverse(
                'users_app:verify',
                kwargs={'pk':user.user_id}
            )
        )


class VerifyLoginView(FormView):
    template_name = 'users/verify_login.html'
    form_class = VerifyUserForm
    success_url = reverse_lazy('home_app:index')
    

    def get_form_kwargs(self):
        kwargs = super(VerifyLoginView, self).get_form_kwargs()
        kwargs.update({'pk': self.kwargs['pk']})
        return kwargs


    def form_valid(self, form):
        id = self.kwargs['pk']
        code = form.cleaned_data['access_code']
        usuario = User.objects.get(user_id=id)
        usuario.use_login_otp = True
        usuario.save(update_fields=['use_login_otp'])

        login(self.request, usuario)

        return super(VerifyLoginView, self).form_valid(form)






class UserLogoutView(View):
    
    def post(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(
            reverse(
                'users_app:login'
            )
        )


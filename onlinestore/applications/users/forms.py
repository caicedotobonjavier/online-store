from django import forms
#
from .models import User
#
from django.contrib.auth import authenticate
#
from django.contrib.auth.hashers import check_password


class UserForm(forms.ModelForm):

    password1 = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingrese contraseña',
                'class': 'mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'
            }
        )
    )

    password2 = forms.CharField(
        required=True,
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Confirme contraseña',
                'class': 'mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'
            }
        )
    )
    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
            'date_birth',
            'address',
            'phone',
            'marketingaccept',
        )

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder':'Ingrese email',
                    'type':'email',
                    'class' : 'mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese nombre completo',
                    'class': 'mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm',                    
                }
            ),
            'date_birth': forms.DateInput(
                attrs={
                    'placeholder':'Ingrese fecha de nacimiento',
                    'type':'date'
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese dirección',
                    'class': 'mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm',  
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese teléfono'
                }
            ),

            'marketingaccept' : forms.CheckboxInput(
                attrs={
                    'class': 'size-5 rounded-md border-gray-200 bg-white shadow-sm',
                    'type' : 'checkbox',
                    'value' : '1'
                }
            )
        }


    def clean_password2(self):
        password2 = self.cleaned_data['password2']

        if self.cleaned_data['password1'] != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return password2



class LoginUserForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email',
                'type':'email',
                'class' : 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm'
            }
        )
    )

    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class': 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm',
                'type' : 'password'
            }
        )
    )
    

    def clean_password(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Email o contraseña incorrectos')
            
        return password



class ActivateUserForm(forms.Form):
    codigo = forms.CharField(
        required=True,
        label='Codido Activacion',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingrese código de activación',
                'class': 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm'
            }
        )
    )
    
    def __init__(self, pk, *args, **kwargs):     
        self.user = pk
        super(ActivateUserForm, self).__init__(*args, **kwargs)
    

    def clean_codigo(self):
        id_user = self.user
        user = User.objects.get(user_id=id_user)

        codigo = self.cleaned_data['codigo']

        if user.cod_activated != codigo:
            raise forms.ValidationError('Código incorrecto')
        
        return codigo



class VerifyUserForm(forms.Form):
    access_code = forms.CharField(
        required=True,
        label='Codido Activacion',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingrese código de activación',
                'class': 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm'
            }
        )
    )   


    def __init__(self, pk, *args, **kwargs):     
        self.user = pk
        super(VerifyUserForm, self).__init__(*args, **kwargs)
    

    def clean_access_code(self):
        access_code = self.cleaned_data['access_code']
        id_user = self.user
        usuario = User.objects.get(user_id=id_user)

        autenticado = check_password(access_code, usuario.login_otp)
        print(autenticado)
        if not autenticado:
            raise forms.ValidationError('Código incorrecto')

        return access_code
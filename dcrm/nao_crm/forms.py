from urllib import request
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                                                    'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nombre',
                                                                              'class': 'form-control'}),
                                 required = True, help_text = "Required", label = "")
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Apellido',
                                                                             'class': 'form-control'}), required=True, help_text="Required")
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre del Usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido. Puede tener menos de 150 caracteres, Letras, Numeros Y @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Tu contraseña es similar a otro de nuestros registros</li><li>Tu contraseña debe contener al menos 8 caracters.</li><li>Tu contraseña no puede ser comun (Ejemp. 12345678, asdfghj, etc...) </li><li>Tu contraseña no puede ser completamente numerica</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirma la contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Ingresa la misma contraseña que en el campo anterior. </small></span>'


# Create add record Form

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nombre',
                                                                         'class': 'form-control'}), required=True, help_text="Required", label = "")
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Apellidos',
                                                                         'class': 'form-control'}), required=True, help_text="Required", label = "")
    phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Telefono',
                                                                         'class': 'form-control'}), required=False, help_text="Required", label = "")
    adress = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'direccion',
                                                                         'class': 'form-control'}), required=True, help_text="Required", label = "")
    city = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Ciudad',
                                                                         'class': 'form-control'}), required=True, help_text="Required", label = "")
    state = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Estado',
                                                                         'class': 'form-control'}), required=True, help_text="Required", label = "")
    zipcode = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Codigo Postal',
                                                                         'class': 'form-control'}), required=True, help_text="Required", label = "")
    email = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Correo Electronico',
                                                                         'class': 'form-control'}), required=True, help_text="Required", label = "")
    class Meta:
        model = Record
        exclude = ("user",)
from django import forms
from django.forms import PasswordInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from .models import Planes

UserModel = get_user_model()

class formUserRegistro(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-control'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrarse como Usuario'))

class CustomChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Cambiar Contraseña'))
        
class UserProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = PasswordInput(render_value=False)
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Guardar perfil'))

    class Meta:
        model = UserModel
        fields = ['username','first_name', 'last_name']
        
        
class SuscripcionForm(forms.Form):
    plan = forms.ModelChoiceField(queryset=Planes.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'onchange': 'this.form.submit();'}))
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plan'].label_from_instance = lambda obj: obj.nombre
        self.fields['plan'].widget.attrs.update({'class': 'form-control'})

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        
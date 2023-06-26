from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

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
        self.helper.add_input(Submit('submit', 'Registrar'))

class CustomChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar cambios'))
        
class CustomChangePasswordForma(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardara cambios'))
from django.forms import *


class LoginForm(Form):
    login = CharField(max_length=150, widget=TextInput(attrs={'class':'login_input'}))
    password = CharField(max_length=150, widget=PasswordInput())


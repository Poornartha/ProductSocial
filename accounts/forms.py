from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['username'].label = 'User Name'
        self.fields['email'].label = 'Email ID'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

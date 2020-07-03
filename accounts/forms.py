from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
        ('red', 'Red'),
        ('pink', 'Pink'),
        ('yellow', 'Yellow'),
    ]
    FAVOURITE_PRODUCT_CHOICES = [
        ('jeans', 'Jeans'),
        ('shirt', 'Shirt'),
        ('trousers', 'Trousers'),
        ('shorts', 'Shorts'),
        ('tee', 'T-shirts'),
        ('shoes', 'Shoes'),
    ]
    favourite_colour = forms.ChoiceField(
        choices=FAVORITE_COLORS_CHOICES,
    )
    fav_product = forms.ChoiceField(
        choices=FAVOURITE_PRODUCT_CHOICES,
    )

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'favourite_colour', 'fav_product', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['username'].label = 'User Name'
        self.fields['email'].label = 'Email ID'
        self.fields['favourite_colour'].label = 'Favourite Colour'
        self.fields['fav_product'].label = 'Favourite Product'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

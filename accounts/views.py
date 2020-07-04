from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from django.contrib.auth.models import User
from .models import Customer

# class SignUp(CreateView):
#     form_class = forms.UserCreateForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'

def SignUp(request):
    form = forms.CustomerCreationForm()

    if request.method == "POST":
        form = forms.CustomerCreationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            favourite_color = form.cleaned_data.get('favourite_colour')
            fav_product = form.cleaned_data.get('fav_product')
            gender = form.cleaned_data.get('gender')
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            user.save()
            customer = Customer.objects.create(user=user, favourite_color=favourite_color, favourite_item=fav_product, gender=gender)
            customer.save()
            return redirect('login')
        else:
            return render(request, 'accounts/login.html', {'form': form})
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

from django.shortcuts import render
from .operations import scrape, scrape_limeroad, scrape_zobello
from django.contrib.auth.models import User
from accounts.models import Customer
# Create your views here.

def dashboard(request):

    search_terms = []
    search_now = ''
    if request.user.is_active:
        search_terms = request.user.search_set.all()
        if search_terms:
            search_now = search_terms[len(search_terms) - 1].search_term
            listings = scrape(search_now)
            listings += scrape_limeroad(search_now)
            listings += scrape_zobello(search_now)
        else:
            listings = []
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_now,
    }

    return render(request, 'dashboard.html', context)


def shirt(request):

    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = customer.favourite_color
        search_prod = 'shirt'
        search_term = search_color + " " + search_prod
        print(search_term)
        listings = scrape(search_term)
        listings += scrape_limeroad(search_term)
        listings += scrape_zobello(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_term,
    }

    return render(request, 'dashboard.html', context)

def shoes(request):

    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = customer.favourite_color
        search_prod = 'shoes'
        search_term = search_color + " " + search_prod
        print(search_term)
        listings = scrape(search_term)
        listings += scrape_limeroad(search_term)
        listings += scrape_zobello(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_term,
    }

    return render(request, 'dashboard.html', context)

def shorts(request):

    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = customer.favourite_color
        search_prod = 'shorts'
        search_term = search_color + " " + search_prod
        print(search_term)
        listings = scrape(search_term)
        listings += scrape_limeroad(search_term)
        listings += scrape_zobello(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_term,
    }

    return render(request, 'dashboard.html', context)

def jeans(request):

    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = customer.favourite_color
        search_prod = 'jeans'
        search_term = search_color + " " + search_prod
        print(search_term)
        listings = scrape(search_term)
        listings += scrape_limeroad(search_term)
        listings += scrape_zobello(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_term,
    }

    return render(request, 'dashboard.html', context)

###########################################################

def blue(request):

    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = 'blue'
        search_prod = customer.favourite_item
        search_term = search_color + " " + search_prod
        print(search_term)
        listings = scrape(search_term)
        listings += scrape_limeroad(search_term)
        listings += scrape_zobello(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_term,
    }

    return render(request, 'dashboard.html', context)

def red(request):

    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = 'red'
        search_prod = customer.favourite_item
        search_term = search_color + " " + search_prod
        print(search_term)
        listings = scrape(search_term)
        listings += scrape_limeroad(search_term)
        listings += scrape_zobello(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_term,
    }

    return render(request, 'dashboard.html', context)

def green(request):

    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = 'green'
        search_prod = customer.favourite_item
        search_term = search_color + " " + search_prod
        print(search_term)
        listings = scrape(search_term)
        listings += scrape_limeroad(search_term)
        listings += scrape_zobello(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_term,
    }

    return render(request, 'dashboard.html', context)

def black(request):

    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = 'black'
        search_prod = customer.favourite_item
        search_term = search_color + " " + search_prod
        print(search_term)
        listings = scrape(search_term)
        listings += scrape_limeroad(search_term)
        listings += scrape_zobello(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_term,
    }

    return render(request, 'dashboard.html', context)


def yellow(request):

    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = 'yellow'
        search_prod = customer.favourite_item
        search_term = search_color + " " + search_prod
        print(search_term)
        listings = scrape(search_term)
        listings += scrape_limeroad(search_term)
        listings += scrape_zobello(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_term,
    }

    return render(request, 'dashboard.html', context)


def white(request):

    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = 'white'
        search_prod = customer.favourite_item
        search_term = search_color + " " + search_prod
        print(search_term)
        listings = scrape(search_term)
        listings += scrape_limeroad(search_term)
        listings += scrape_zobello(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_term,
    }

    return render(request, 'dashboard.html', context)


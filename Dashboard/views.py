from django.shortcuts import render
from .operations import scrape, scrape_limeroad, scrape_zobello
from django.contrib.auth.models import User
from accounts.models import Customer
# Create your views here.

def dashboard(request):

    search_terms = []
    search_now = ''
    search_now1 = ''
    search_now2 = ''
    search_now3 = ''
    listings1 = []
    listings2 = []
    listings3 = []
    if request.user.is_active:
        search_terms = request.user.search_set.all()
        print(search_terms)
        if search_terms:
            search_now = search_terms[len(search_terms) - 1].search_term
            if 'tee' in search_now.lower():
                listings1 = scrape(search_now)
            else:
                listings1 = scrape_limeroad(search_now)
            search_now1 = search_now
            if len(search_terms) - 2 >= 0:
                search_now = search_terms[len(search_terms) - 2].search_term
                if 'tee' in search_now.lower():
                    listings2 = scrape(search_now)
                else:
                    listings2 = scrape_limeroad(search_now)
                search_now2 = search_now
            elif len(search_terms) - 3 >= 0:
                search_now = search_terms[len(search_terms) - 3].search_term
                if 'tee' in search_now.lower():
                    listings3 = scrape(search_now)
                else:
                    listings3 = scrape_limeroad(search_now)
                search_now3 = search_now
            if len(search_terms) >= 3:
                listings1 = listings1[:3]
                listings2 = listings2[:3]
                listings3 = listings3[:3]
            elif len(search_terms) >= 2:
                listings1 = listings1[:6]
                listings2 = listings2[:6]
        else:
            listings1 = []
            listings2 = []
            listings3 = []
    else:
        listings1 = []
        listings2 = []
        listings3 = []

    context = {
        'listings1': listings1,
        'listings2': listings2,
        'listings3': listings3,
        'search1': search_now1,
        'search2': search_now2,
        'search3': search_now3,
    }

    return render(request, 'dashboard-recent.html', context)


def shirt(request):

    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = customer.favourite_color
        search_prod = 'shirt'
        search_term = request.user.customer.gender + ' ' + search_color + " " + search_prod
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

    return render(request, 'dashboard-product.html', context)

def shoes(request):

    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = customer.favourite_color
        search_prod = 'shoes'
        search_term = search_color + " " + search_prod
        search_term = request.user.customer.gender + ' ' + search_color + " " + search_prod
        print(search_term)
        listings = scrape_limeroad(search_term)
        listings += scrape_zobello(search_term)
        listings += scrape(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_term,
    }

    return render(request, 'dashboard-product.html', context)

def shorts(request):

    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = customer.favourite_color
        search_prod = 'shorts'
        search_term = search_color + " " + search_prod
        search_term = request.user.customer.gender + ' ' + search_color + " " + search_prod
        print(search_term)
        listings = scrape_limeroad(search_term)
        listings += scrape_zobello(search_term)
        listings += scrape(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_term,
    }

    return render(request, 'dashboard-product.html', context)

def jeans(request):
    search_prod = ''
    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = customer.favourite_color
        search_prod = 'jeans'
        search_term = search_color + " " + search_prod
        search_term = request.user.customer.gender + ' ' + search_color + " " + search_prod
        print(search_term)
        listings = scrape_limeroad(search_term)
        listings += scrape_zobello(search_term)
        listings += scrape(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_term,
    }

    return render(request, 'dashboard-product.html', context)

###########################################################

def blue(request):
    search_prod = ''
    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = 'blue'
        search_prod = customer.favourite_item
        search_term = search_color + " " + search_prod
        search_term = request.user.customer.gender + ' ' + search_color + " " + search_prod
        print(search_prod)
        if request.user.customer.gender == 'male':
            listings = scrape(search_term)
            listings += scrape_zobello(search_term)
            listings += scrape_limeroad(search_term)
        else:
            listings = scrape_limeroad(search_term)
            listings += scrape_zobello(search_term)
            listings += scrape(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_prod,
    }

    return render(request, 'dashboard.html', context)

def red(request):
    search_prod = ''
    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = 'red'
        search_prod = customer.favourite_item
        search_term = search_color + " " + search_prod
        search_term = request.user.customer.gender + ' ' + search_color + " " + search_prod
        print(search_term)
        if request.user.customer.gender == 'male':
            listings = scrape(search_term)
            listings += scrape_zobello(search_term)
            listings += scrape_limeroad(search_term)
        else:
            listings = scrape_limeroad(search_term)
            listings += scrape_zobello(search_term)
            listings += scrape(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_prod,
    }

    return render(request, 'dashboard.html', context)

def green(request):
    search_prod = ''
    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = 'green'
        search_prod = customer.favourite_item
        search_term = search_color + " " + search_prod
        search_term = request.user.customer.gender + ' ' + search_color + " " + search_prod
        print(search_term)
        if request.user.customer.gender == 'male':
            listings = scrape(search_term)
            listings += scrape_zobello(search_term)
            listings += scrape_limeroad(search_term)
        else:
            listings = scrape_limeroad(search_term)
            listings += scrape_zobello(search_term)
            listings += scrape(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_prod,
    }

    return render(request, 'dashboard.html', context)

def black(request):
    search_prod = ''
    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = 'black'
        search_prod = customer.favourite_item
        search_term = search_color + " " + search_prod
        search_term = request.user.customer.gender + ' ' + search_color + " " + search_prod
        print(search_term)
        if request.user.customer.gender == 'male':
            listings = scrape(search_term)
            listings += scrape_zobello(search_term)
            listings += scrape_limeroad(search_term)
        else:
            listings = scrape_limeroad(search_term)
            listings += scrape_zobello(search_term)
            listings += scrape(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_prod,
    }

    return render(request, 'dashboard.html', context)


def yellow(request):
    search_prod = ''
    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = 'yellow'
        search_prod = customer.favourite_item
        search_term = search_color + " " + search_prod
        search_term = request.user.customer.gender + ' ' + search_color + " " + search_prod
        print(search_term)
        if request.user.customer.gender == 'male':
            listings = scrape(search_term)
            listings += scrape_zobello(search_term)
            listings += scrape_limeroad(search_term)
        else:
            listings = scrape_limeroad(search_term)
            listings += scrape_zobello(search_term)
            listings += scrape(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_prod,
    }

    return render(request, 'dashboard.html', context)


def white(request):
    search_prod = ''
    search_term = ''
    if request.user.is_active:
        customer = request.user.customer
        search_color = 'white'
        search_prod = customer.favourite_item
        search_term = search_color + " " + search_prod
        search_term = request.user.customer.gender + ' ' + search_color + " " + search_prod
        print(search_term)
        if request.user.customer.gender == 'male':
            listings = scrape(search_term)
            listings += scrape_zobello(search_term)
            listings += scrape_limeroad(search_term)
        else:
            listings = scrape_limeroad(search_term)
            listings += scrape_zobello(search_term)
            listings += scrape(search_term)
    else:
        listings = []

    context = {
        'listings': listings,
        'search': search_prod,
    }

    return render(request, 'dashboard.html', context)

def suggesions(request):
    return render(request, 'dashboard-product.html')

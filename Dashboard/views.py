from django.shortcuts import render
from .operations import scrape, scrape_limeroad, scrape_zobello
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

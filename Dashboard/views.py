from django.shortcuts import render
from .operations import scrape, scrape_limeroad, scrape_zobello
# Create your views here.

def dashboard(request):
    
    search_terms = []
    if request.user.is_active:
        search_terms = request.user.search_set.all()
    
    search_now = search_terms[0].search_term

    listings = scrape(search_now)
    listings += scrape_limeroad(search_now)
    listings += scrape_zobello(search_now)

    context = {
        'listings': listings,
        'search': search_now,
    }

    return render(request, 'dashboard.html', context)

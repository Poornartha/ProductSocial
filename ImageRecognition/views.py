
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms

# Imaginary function to handle an uploaded file.
from .operations import recognize, scrape, scrape_limeroad, scrape_zobello

search_global = ''

def home(request):
    global search_global
    output = search_global
    if 'trunk' in output or 'short' in output or 'mini' in output or 'shorts' in output:
        output = 'shorts' 
    elif 'shoe' in output:
        output = 'shoe'
    search_term = output
    listings = scrape(search_term)
    context = {'search_term': search_term,
                'listings': listings}
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            output = recognize(request.FILES['image'])
            if 'trunk' in output or 'shorts' in output or 'mini' in output:
                output = 'shorts'
            elif 'shoe' in output:
                output = 'shoe'
            to_search = output.split('_')
            search_term = ''
            for i in to_search:
                search_term += i
            search_global = search_term
            listings = scrape(search_term)
            context = {'form': form, 'output': output,
                        'listings': listings,
                        'output': output}
            return render(request, 'search.html', context)
    else:
        form = forms.UploadFileForm()
        context['form'] = form
    return render(request, 'search.html', context)


def limeroad(request):
    global search_global
    output = search_global
    if 'trunk' in output or 'shorts' in output or 'mini' in output:
        output = 'shorts'
    elif 'shoe' in output:
        output = 'shoe'
    search_term = output
    listings = scrape_limeroad(search_term)
    context = {'search_term': search_term,
                'listings': listings}
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            output = recognize(request.FILES['image'])
            if 'trunk' in output or 'shorts' in output or 'mini' in output:
                output = 'shorts'
            elif 'shoe' in output:
                output = 'shoe'
            to_search = output.split('_')
            search_term = ''
            for i in to_search:
                search_term += i
            search_global = search_term
            listings = scrape_limeroad(search_term)
            context = {'form': form, 'output': output,
                        'listings': listings,
                        'output': output}
            return render(request, 'search.html', context)
    else:
        form = forms.UploadFileForm()
        context['form'] = form
    return render(request, 'search.html', context)

def zobello(request):
    global search_global
    output = search_global
    if 'trunk' in output or 'shorts' in output or 'mini' in output:
        output = 'shorts'
    elif 'shoe' in output:
        output = 'shoe'
    search_term = output
    listings = scrape_zobello(search_term)
    context = {'search_term': search_term,
                'listings': listings}
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            output = recognize(request.FILES['image'])
            if 'trunk' in output or 'shorts' in output or 'mini' in output:
                output = 'shorts'
            elif 'shoe' in output:
                output = 'shoe'
            to_search = output.split('_')
            search_term = ''
            for i in to_search:
                search_term += i
            search_global = search_term
            listings = scrape_zobello(search_term)
            context = {'form': form, 'output': output,
                        'listings': listings,
                        'output': output}
            return render(request, 'search.html', context)
    else:
        form = forms.UploadFileForm()
        context['form'] = form
    return render(request, 'search.html', context)


def randomize(request):
    global search_global
    output = search_global
    if 'trunk' in output or 'shorts' in output or 'mini' in output:
        output = 'shorts'
    elif 'shoe' in output:
        output = 'shoe'
    search_term = output
    listings_zob = scrape_zobello(search_term)
    listings_lime = scrape_limeroad(search_term)
    listings_bewa = scrape(search_term)
    if output == 'jean' or output=='jersey':
        listings = listings_lime[:5] + listings_bewa[:5]
    else:
        listings = listings_lime[:5] + listings_zob[:5]
    context = {'search_term': search_term,
                'listings': listings}
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            output = recognize(request.FILES['image'])
            if 'trunk' in output or 'shorts' in output or 'mini' in output:
                output = 'shorts'
            elif 'shoe' in output:
                output = 'shoe'
            to_search = output.split('_')
            search_term = ''
            for i in to_search:
                search_term += i
            search_global = search_term
            listings_zob = scrape_zobello(search_term)
            listings_lime = scrape_limeroad(search_term)
            listings_bewa = scrape(search_term)
            if output == 'jeans' or output == 'jean' or output=='jersey':
                listings = listings_lime[:5] + listings_bewa[:5]
            else:
                listings = listings_lime[:5] + listings_zob[:5]
            context = {'form': form, 'output': output,
                        'listings': listings,
                        'output': output}
            return render(request, 'search.html', context)
    else:
        form = forms.UploadFileForm()
        context['form'] = form
    return render(request, 'search.html', context)



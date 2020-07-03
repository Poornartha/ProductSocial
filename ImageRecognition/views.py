
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms
from .models import Search

# Imaginary function to handle an uploaded file.
from .operations import recognize, scrape, scrape_limeroad, scrape_zobello
from .color_detection import detect_color

search_global = ''

def home(request):
    global search_global
    output = search_global
    search_term = output
    listings = scrape(search_term)
    if len(listings) == 0:
        search_term = search_term.split(' ')[0]
        listings = scrape(search_term.split(' ')[0])
    context = {'search': search_term,
                'listings': listings}
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            output = recognize(request.FILES['image'])
            if 'trunk' in output or 'shorts' in output or 'mini' in output:
                output = 'shorts'
            elif 'shoe' in output:
                output = 'shoe'
            elif 'jersey' in output:
                output = 'tee'
            elif 'cardigan' in output:
                output = 'shirt'
            to_search = output.split('_')
            search_term = ''
            for i in to_search:
                search_term += i
            color_term = detect_color(request.FILES['image'])
            search_term += " " + color_term
            search_global = search_term
            listings = scrape(search_term)
            if len(listings) == 0:
                search_term = color_term
                listings = scrape(color_term)

            if request.user.is_active and search_term != '':
                s, created = Search.objects.get_or_create(search_term=search_term)
                s.users.add(request.user)

            context = {'form': form, 'output': output,
                        'listings': listings,
                        'search': search_term}
            return render(request, 'search.html', context)
    else:
        form = forms.UploadFileForm()
        context['form'] = form
    return render(request, 'search.html', context)


def limeroad(request):
    global search_global
    output = search_global
    search_term = output
    listings = scrape_limeroad(search_term)
    if len(listings) == 0:
        search_term = search_term.split(' ')[0]
        listings = scrape_limeroad(search_term.split(' ')[0])
    context = {'search': search_term,
                'listings': listings}
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            output = recognize(request.FILES['image'])
            if 'trunk' in output or 'shorts' in output or 'mini' in output:
                output = 'shorts'
            elif 'shoe' in output:
                output = 'shoe'
            elif 'jersey' in output:
                output = 'tee'
            elif 'cardigan' in output:
                output = 'shirt'
            to_search = output.split('_')
            search_term = ''
            for i in to_search:
                search_term += i
            color_term = detect_color(request.FILES['image'])
            search_term += " " + color_term
            search_global = search_term
            listings = scrape_limeroad(search_term)
            if len(listings) == 0:
                search_term = color_term
                listings = scrape_limeroad(color_term)

            if request.user.is_active and search_term != '':
                s, created = Search.objects.get_or_create(search_term=search_term)
                s.users.add(request.user)

            context = {'form': form, 'output': output,
                        'listings': listings,
                        'search': search_term}
            return render(request, 'search.html', context)
    else:
        form = forms.UploadFileForm()
        context['form'] = form
    return render(request, 'search.html', context)

def zobello(request):
    global search_global
    output = search_global
    search_term = output
    listings = scrape_zobello(search_term)
    if len(listings) == 0:
        search_term = search_term.split(' ')[0]
        listings = scrape(search_term.split(' ')[0])
    context = {'search': search_term,
                'listings': listings}
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            output = recognize(request.FILES['image'])
            if 'trunk' in output or 'shorts' in output or 'mini' in output:
                output = 'shorts'
            elif 'shoe' in output:
                output = 'shoe'
            elif 'jersey' in output:
                output = 'tee'
            elif 'cardigan' in output:
                output = 'shirt'
            to_search = output.split('_')
            search_term = ''
            for i in to_search:
                search_term += i
            color_term = detect_color(request.FILES['image'])
            search_term += " " + color_term
            search_global = search_term
            listings = scrape_zobello(search_term)
            if len(listings) == 0:
                search_term = color_term
                listings = scrape_zobello(color_term)

            if request.user.is_active and search_term != '':
                s, created = Search.objects.get_or_create(search_term=search_term)
                s.users.add(request.user)


            context = {'form': form, 'output': output,
                        'listings': listings,
                        'search': search_term}
            return render(request, 'search.html', context)
    else:
        form = forms.UploadFileForm()
        context['form'] = form
    return render(request, 'search.html', context)


def randomize(request):
    global search_global
    output = search_global
    search_term = output
    listings_zob = scrape_zobello(search_term)
    listings_lime = scrape_limeroad(search_term)
    listings_bewa = scrape(search_term)
    if output == 'jean' or output=='jersey':
        listings = listings_lime[:5] + listings_bewa[:5]
    else:
        listings = listings_lime[:5] + listings_zob[:5]
    context = {'search': search_term,
                'listings': listings}
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            output = recognize(request.FILES['image'])
            if 'trunk' in output or 'shorts' in output or 'mini' in output:
                output = 'shorts'
            elif 'shoe' in output:
                output = 'shoe'
            elif 'jersey' in output:
                output = 'tee'
            elif 'cardigan' in output:
                output = 'shirt'
            to_search = output.split('_')
            search_term = ''
            for i in to_search:
                search_term += i
            search_term += " " + detect_color(request.FILES['image'])
            search_global = search_term

            if request.user.is_active and search_term != '':
                s, created = Search.objects.get_or_create(search_term=search_term)
                s.users.add(request.user)

            listings_zob = scrape_zobello(search_term)
            listings_lime = scrape_limeroad(search_term)
            listings_bewa = scrape(search_term)
            if output == 'jeans' or output == 'jean' or output=='jersey':
                listings = listings_lime[:5] + listings_bewa[:5]
            else:
                listings = listings_lime[:5] + listings_zob[:5]
            context = {'form': form, 'output': output,
                        'listings': listings,
                        'search': search_term}
            return render(request, 'search.html', context)
    else:
        form = forms.UploadFileForm()
        context['form'] = form
    return render(request, 'search.html', context)


def landing(request):
    return render(request, 'landing.html')


def trending(request):
    search_list = Search.objects.all()
    if len(search_list) > 10:
        search_list = search_list[:10]
    search_list = list(search_list)
    # print(search_list)
    for i in range(len(search_list)):
        for j in range(len(search_list)):
            if len(search_list[i].users.all()) > len(search_list[j].users.all()):
                temp = search_list[j]
                search_list[j] = search_list[i]
                search_list[i] = temp 
    max_1 = search_list[0].search_term
    max_2 = search_list[2].search_term
    listings_1 = scrape_limeroad(max_1)
    listings_2 = scrape_limeroad(max_2)
    listings = listings_1 + listings_2

    context = {
        'search': max_1 + ' and ' + max_2,
        'listings': listings,
    }

    return render(request, 'trending.html', context)

    
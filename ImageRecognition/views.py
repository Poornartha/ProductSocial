
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms

# Imaginary function to handle an uploaded file.
from .operations import recognize, scrape, scrape_limeroad, scrape_zobello


def home(request):
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            output = recognize(request.FILES['image'])
            if 'trunks' in output or 'shorts' in output or 'mini' in output:
                output = 'short'
            elif 'shoe' in output:
                output = 'shoe'
            elif 'jersey':
                output = 'tee'
            else:
                output = 'shirt'
            to_search = output.split('_')
            search_term = ''
            for i in to_search:
                search_term += i 
            listings = scrape(search_term)
            listings += scrape_limeroad(search_term)
            listings += scrape_zobello(search_term)
            return render(request, 'search.html', {'form': form, 'output': output, 'listings': listings})
    else:
    	form = forms.UploadFileForm()
    return render(request, 'search.html', {'form': form})

# def search(request, query):
#     
#     return render(request, 'search.html', {'query': search_term})
import numpy as np
import keras
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Model
from keras.applications import imagenet_utils


def prepare_image(img):
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

def recognize(img):
    from PIL import Image
    mobile = keras.applications.mobilenet.MobileNet()
    img = Image.open(img)
    new_width  = 224
    new_height = 224
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    preprocessed_image = prepare_image(img)
    predictions = mobile.predict(preprocessed_image)
    results = imagenet_utils.decode_predictions(predictions)
    return results[0][0][1]

  
import requests
from django.shortcuts import render
from . import models
from django.utils import timezone
from bs4 import BeautifulSoup
from requests.compat import quote_plus

BASE_FLIPKART_URL = 'https://www.bewakoof.com/search/{}'

def scrape(search):
    final_url = BASE_FLIPKART_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    wrap = soup.find('div', {'class': 'categoryGridWrapper'})
    image_set = wrap.find_all('img')
    link_set = wrap.find_all('a')
    image_collection = []
    link_collection = []

    for link in link_set:
        check = link.get('href')
        link_collection.append(check)


    for image in image_set:
        check = image['src']
        if check != "https://images.bewakoof.com/web/b-coin-gold-3x.png":
            image_collection.append(check)

    for image in image_collection:
        if image == "https://images.bewakoof.com/web/b-coin-gold-3x.png":
            image_collection.remove(image)

    post_listings = soup.find_all('div', {'class': 'productCardDetail'})
    final_postings = []
    i = 0
    # size_listings = soup.find_all('div', {'class': 'productCardDetail'})
    while i<len(post_listings) and i<8:
        post = post_listings[i]
        post_title = post.find('h3').text
        post_price = 'Rs. ' + post.find('b').text
        link_base = "https://www.bewakoof.com{}"
        final_postings.append((post_title, post_price, image_collection[i], link_base.format(link_collection[i+5])))
        i = i + 1
    return final_postings


def scrape_limeroad(search):
    BASE_FLIPKART_URL = 'https://www.limeroad.com/search/{}'
    search_tags = search.split(' ')
    search_term = ''
    for search in search_tags:
        search_term += search + '%20'
    final_url = BASE_FLIPKART_URL.format(search_term)
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    body = soup.find('body')
    prods = body.find_all('div', {'class': "prdC bgF br4 fs12 fg2t dIb vT pR taC bs bd2E bdE"})
    image_set = []
    links_set = []
    brand = []
    post_price = []
    for product in prods:
        image_set.append(product.find('img', {'class': "dB h412 w310 mA pR prdI gtm-p an-ll o0"})['data-src'])
        links_set.append('https://www.limeroad.com/' + product.find('a', {'class': "dB pR taC ldr gtm-p h412 bs oH phref"}).get('href'))
        brand.append(product.find('a', {'class': "c9 dB fs11 wp96 oH tdN ttC wsN pt4"}).text.split('\n')[1].lstrip())
        post_price.append(product.find('div', {'class': "dIb vM c3 fs14"}).text)
    final_postings = []
    for i in range(len(image_set)):
        final_postings.append((brand[i], post_price[i], image_set[i], links_set[i]))
    return final_postings
    

def scrape_zobello(search):
    BASE_FLIPKART_URL = 'https://www.zobello.com/search?type=product&q={}'
    search_tags = search.split(' ')
    search_term = ''
    for search in search_tags:
        search_term += search + '+'
    final_url = BASE_FLIPKART_URL.format(search_term)
    response = requests.get(final_url, timeout=10)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    body = soup.find('body')
    cards = body.find_all('div', {'class': 'main_box'})
    image_set = []
    link_set = []
    price_set = []
    title_set = []
    for card in cards:
        image_set.append('https:' + card.find('img')['srcset'].split(' ')[0])
        link_set.append('https://www.zobello.com/' + card.find('a').get('href'))
        price_set.append(card.find('div', {'class': 'price'}).text)
        title_set.append(card.find('h5').text)
    final_postings = []
    for i in range(len(title_set)):
        final_postings.append((title_set[i], price_set[i], image_set[i], link_set[i]))
    return final_postings



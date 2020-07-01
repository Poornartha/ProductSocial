import numpy as np
import keras
from keras import backend as K
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
    while i<len(post_listings) and i<10:
        post = post_listings[i]
        post_title = post.find('h3').text
        post_price = post.find('b').text
        link_base = "https://www.bewakoof.com{}"
        final_postings.append((post_title, post_price, image_collection[i], link_base.format(link_collection[i+5])))
        i = i + 1
    return final_postings
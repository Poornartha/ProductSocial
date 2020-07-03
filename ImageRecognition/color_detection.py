from sklearn.cluster import KMeans
import numpy as np
from cv2 import cv2 
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def get_colors(image, number_of_colors):
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)
    counts = Counter(labels)
    center_colors = clf.cluster_centers_
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    return rgb_colors


def match_image_by_color(image, color, threshold = 60, number_of_colors = 3): 
    
    image_colors = get_colors(get_image(image), number_of_colors)
    selected_color = rgb2lab(np.uint8(np.asarray([[color]])))

    select_image = False
    for i in range(number_of_colors):
        curr_color = rgb2lab(np.uint8(np.asarray([[image_colors[i]]])))
        diff = deltaE_cie76(selected_color, curr_color)
        if (diff < threshold):
            select_image = True
    
    return select_image

COLORS = {
    'GREEN': [0, 128, 0],
    'BLUE': [0, 0, 128],
    'YELLOW': [255, 255, 0],
    'RED': [255, 0, 0],
    'ORANGE': [255, 69, 0],
    'BLACK': [0, 0, 0],
}

def find_color(img_loc):
    green = match_image_by_color(img_loc, COLORS['GREEN'])
    blue = match_image_by_color(img_loc, COLORS['BLUE'])
    yellow = match_image_by_color(img_loc, COLORS['YELLOW'])
    red = match_image_by_color(img_loc, COLORS['RED'])
    orange = match_image_by_color(img_loc, COLORS['ORANGE'])
    black = match_image_by_color(img_loc, COLORS['BLACK'])
    colors = []
    if green:
        colors.append('Green')
        return colors
    if blue:
        colors.append('Blue')
        return colors
    if yellow:
        colors.append('Yellow')
        return colors
    if red:
        colors.append('Red')
        return colors
    if orange:
        colors.append('Orange')
        return colors
    if black:
        colors.append('Black')
        return colors
    return colors
    



def detect_color(img):
    from PIL import Image
    import numpy
    pil_image = Image.open(img)
    img = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
    col = find_color(img)
    term = ''
    for c in col:
        term += c + ' '
    print(term)
    return term


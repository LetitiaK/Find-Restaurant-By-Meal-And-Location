#!/usr/bin/env python

import httplib2
import json
import datetime

now = datetime.datetime.now()


def getGeocodeLocation(inputString):
    """Get the latitude and longitude of a given city or address using
    the Google Maps Geocode API"""
    google_api_key = "[YOUR KEY HERE]"
    locationString = inputString.replace(" ", "+")
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (locationString, google_api_key)  # NOQA
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return latitude, longitude


def findARestaurant(mealType, location):
    """Find a restaurant at a certain location using the Foursquare API"""
    fs_client_id = "[YOUR ID HERE]"
    fs_client_secret = "[YOUR SECRET HERE]"
    latitude, longitude = getGeocodeLocation(location)
    # Define the search radius
    radius = 5000
    date = now.strftime("%Y%m%d")
    restaurant_url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&ll=%s,%s&radius=%s&intent=browse&query=%s&v=%s'  # NOQA
    % (fs_client_id, fs_client_secret, latitude, longitude, radius, mealType, date))  # NOQA
    h = httplib2.Http()
    response, content = h.request(restaurant_url, 'GET')
    result = json.loads(content)
    # Give a result if there is no restaurant found
    if len(result['response']['venues']) < 1:
        print ("Sorry, there is no suitable restaurant at this location")
        return 0
    restaurants = result['response']['venues']
    restaurant_list = []
    i = 0
    while i < len(restaurants):
        restaurant_id = result['response']['venues'][i]['id']
        restaurant_name = result['response']['venues'][i]['name']
        formatted_address = result['response']['venues'][i]['location']['formattedAddress']  # NOQA
        # Not all restaurants have a full adress so it is necessary to
        # iterate through the formatted address
        restaurant_address = ""
        for j in formatted_address:
            restaurant_address = restaurant_address + " " + j
        # Get the image of the restaurant
        image_url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&client_secret=%s&v=%s'  # NOQA
        % (restaurant_id, fs_client_id, fs_client_secret, date))
        response, content = h.request(image_url, 'GET')
        image_result = json.loads(content)
        # Provide a default picture in case there is no image available
        if len(image_result['response']['photos']['items']) < 1:
            restaurant_image = "https://cdn.pixabay.com/photo/2016/10/08/18/35/restaurant-1724294_960_720.png"  # NOQA
        else:
            # Create an image url consisting of prefix + size + suffix
            image_prefix = image_result['response']['photos']['items'][0]['prefix']  # NOQA
            size = "300x300"
            image_suffix = image_result['response']['photos']['items'][0]['suffix']  # NOQA
            restaurant_image = image_prefix + size + image_suffix
        # Add restaurant to restaurant list
        restaurant_list.append([restaurant_name, restaurant_address, restaurant_image])  # NOQA
        i += 1
    # Print all found restaurants to the console as a dictionary
    for k in restaurant_list:
        print ("Restaunt Name: " + k[0] + "\nRestaurant Address: " + k[1]
               + "\nImage: " + k[2] + "\n")
    # return just a single (i.e. the first) restaurant from the list
    return restaurant_list[0]


findARestaurant("Gyros", "Sidney Australia")

# Find-Restaurant-By-Meal-And-Location
This project uses the Google Maps Geolocation API as well as the Foursquare API to find a restaurant for a given meal type and location

## Getting started
1. For this project you need to set up a Google Developer Account for the Google Maps Geolocation API.
This can be done here: https://developers.google.com/maps/?hl=de
Navigate to "Geolocation" and retrieve the key.

2. You also need to set up a Foursquare Developer Accouont.
This can be done here: https://developer.foursquare.com/
Retrieve your client ID and client Secret.

3. Insert the key, client ID and client Secret into the respective parts in the code. Marked with "[YOUR KEY HERE]".

## Requirements
_Note that this code requires a Python installation (you can download Python [here](https://www.python.org/downloads/))_

1. Download the file
2. Chose one of the two possibilities described below to run the code

#### Command line
1. Open a terminal
2. Change the directory (using `cd`) to access the folder, in which you saved the files
3. Type `python find_restaurants.py` for Python 2.x or `py find_restaurants.py` for Python 3

#### Python IDLE (Python GUI)
1. Open Python IDLE (it is automatically installed with the Python installation)
2. Open the file **find_restaurants.py**
3. Run the code by pressing `F5`

## Troubleshooting
1. If running the code in the terminal throws an error, reinstall Python and make sure to select **Add python.exe to Path** during installation.

2. If you need to install httplib2 run `pip2 install httplib2` in your terminal for Python 2.x and `pip3 install httplib2` for Python 3.



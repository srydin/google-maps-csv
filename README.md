# google-maps-csv
Use google Maps API to create a local CSV

Instructions for use on OSX:

1. Open the file and insert your own API key on line 17. You can get one from this URL: https://developers.google.com/places/web-service/get-api-key
2. Run the file in terminal with Python e.g. "python ~/Desktop/google-maps-csv.py"
3. At the prompts, answer the following:
  -Filename to write on Desktop - Entering "restaurants" will write restaurants.csv to Desktop.
  -GPS coordinates in Lat/Long - Entering "32.7767,-96.7970" for example.
  -Radius of search area in meters - Entering "50000" is the max radius.
  -Keywords to add to search, linked with a + symbol - Entering "restaurants" or "indian+food" for example.

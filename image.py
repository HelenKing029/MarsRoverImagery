# Goal: Return Nasa Image
import requests
import urllib
import webbrowser
#Get request to retreive data and convert to json
myData = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=mast&api_key=opgXVZiIrRKyW9mydmhToEfG8Pamm6ikpkXHOBpX")
json_dict = myData.json()
#print(json_dict)

#get the image from place "1"
roverImage = json_dict["photos"][3]["img_src"]
#open image in web browser
webbrowser.open_new_tab(roverImage)

print(roverImage)

# opening link - https://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python
# nested json - https://stackoverflow.com/questions/23306653/python-accessing-nested-json-data#

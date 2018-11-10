import requests
import webbrowser

#Get request to retreive data and convert to json
myData = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=ENTER_YOUR_KEY")
json_dict = myData.json()
#print(json_dict)

#get the image from first place holder
roverImage = json_dict["photos"][0]["img_src"]
print(roverImage)

#open image in web browser
webbrowser.open_new_tab(roverImage)


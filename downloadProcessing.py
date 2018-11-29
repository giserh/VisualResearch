from toList import *
from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()

data = txtToDict()

#arguments
arguments = {"keywords":"Yokai",
             "limit":3,
             "print_urls":False, 
             "size":">1024*768", 
             "output_directory":"structure/"}

#Cycle Download Func
for key in list(data.keys()):
    arguments["output_directory"] = "img_structure/" + key + '/'
    #dict to list
    L = data[key]      
    arguments["keywords"] = ",".join(str(i) for i in L)
    response.download(arguments)

#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## prompt the user to enter a date
    startdate = input( "Please enter a start date in this format: [2019-11-11] ")
    enddate= input( "Please enter a end date in this format: [2019-11-11] ")

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(f"{NEOURL}start_date={startdate}&{nasacreds}&end_date={enddate}")

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

    img_data = requests.get(neodata['url']).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)


main()


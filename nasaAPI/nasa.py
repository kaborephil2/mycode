#!/usr/bin/env python3

import requests

API = "http://api.open-notify.org/iss-now.json"

def main():
    # make a get request to API
    response = requests.get(f"{API}")
    data  = response.json()
    print(data)

    #display the current longitude and latitude
    print(f"CURRENT LOCATION OF THE ISS : \nLon: {data['iss_position']['longitude']} \nLat: {data['iss_position']['latitude']}")

main()

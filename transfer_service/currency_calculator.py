#!/usr/bin/env python3

import requests
import json

#apiKey = 'GDVMzrjxOr49mE6UPMMoJMSNyBQIcT57l140'
baseCurrency = 'USD'

#url = 'https://currencyapi.net/api/v1/rates?key='+apiKey+'&base='+baseCurrency

# Define currencyapi.net url.
url = 'https://currencyapi.net/api/v1/rates?'

# This function handle the credential stored in /home/student/ directory.
def handle_credential():
    ## first I want to grab my credentials
    with open("/home/student/currencyAPI.creds", "r") as mycreds:
        currency_creds = mycreds.read()
    ## remove any newline characters from the api_key
    currency_creds = "key=" + currency_creds.strip("\n")+'&base='+baseCurrency
    return currency_creds
    # this is our main function

# This funtion will gather the sender and receiver information for the transfer.
def transaction_info():
    print("Provide us your information:  \n")
    sender_firstname = input("Please enter your first name: ").lower().title()
    sender_lastname = input("Please enter your last name: ").lower().title()
    sender_country = input("Please enter your current country: ").lower().title()
    
    print("Provide us the receiver information:  \n")
    receiver_firstname = input("Please enter your receiver first name: ").lower().title()
    receiver_lastname = input("Please enter your receiver last name: ").lower().title()
    receiver_country = input("Please enter your receiver current country: ").lower().title()
    receiver_country_code = input("Please enter your receiver country 3 letters code: ").title()
    code = receiver_country_code.upper()

    ## first grab credentials
    currency_creds = handle_credential()

    # make a get request
    r = requests.get(url+currency_creds)
    response = r.json()

    print(f" 1 {baseCurrency} = {response['rates'][code]} {code} \n")

    answer = input(" Would you like to proceed with the transaction? yes or no: ")
    if answer == "yes": 
        amount = int(input(" How much would you like to send : "))
        fees = amount * 0.02 
        rate = response['rates'][code]
        total_amount = (amount * rate) + rate
        print(total_amount)
    else:
        print("Thank you for visting our store")

def main():
    transaction_info()

if __name__ == "__main__":
    main()

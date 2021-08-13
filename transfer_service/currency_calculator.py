#!/usr/bin/env python3

import requests
import json
import random

baseCurrency = 'USD'

# Define currencyapi.net url.
url = 'https://currencyapi.net/api/v1/rates?'

# This function handle the credential stored in /home/student/ directory.
def handle_credential():

    # import the credentials
    with open("/home/student/currencyAPI.creds", "r") as mycreds:
        currency_creds = mycreds.read()

    ## remove any newline characters from the api_key
    currency_creds = "key=" + currency_creds.strip("\n")+'&base='+baseCurrency
    return currency_creds

# This funtion will gather the sender and receiver information for the transfer.
def transaction_info():
    print("\n\n           WELCOME TO GLOBAL MONEY TRANSFER, Inc.\n\n")
    print("\n\nSender information:  \n")
    print("*********************************************************************************\n")
    sender_firstname = input("Please enter sender first name: ").lower().title()
    sender_lastname = input("Please enter sender last name: ").lower().title()
    sender_country_code = input("Please enter sender country 3 letters code: ").upper()
    
    print("\n\nReceiver information:  \n")
    print("*********************************************************************************\n")
    receiver_firstname = input("Please enter receiver first name: ").lower().title()
    receiver_lastname = input("Please enter receiver last name: ").lower().title()
    receiver_country = input("Please enter receiver current country: ").lower().title()
    receiver_country_code = input("Please enter receiver country 3 letters code: ").upper()

    print("*********************************************************************************\n")
    # change the country code to uppercase letters
    code = receiver_country_code.upper()

    ## import the credentials from the home directory
    currency_creds = handle_credential()

    # make a get request
    r = requests.get(url+currency_creds)
    response = r.json()
    
    #If the sender is from the US
    if sender_country_code == "USD":

        # Display the conversation rate between US dallar and the receiver country currency
        try:
            print(f" 1 {baseCurrency} = {response['rates'][code]} {code} \n")
        except:
            print(f"Please enter a valide country code. {receiver_country_code} is not valide \n")
            code = input("\nPlease enter your receiver country 3 letters code again: ").upper()
            print(f" 1 {baseCurrency} = {response['rates'][code]} {code} \n")
        
        answer = input("\nWould you like to proceed with the transaction? yes or no: ")
        if answer == "yes": 
            amount = int(input("\nHow much would you like to send [Note: amount is in US Dollar] : "))
            fees = amount * 0.02

            #print 2 decimal places
            format_fees = "{:.2f}".format(fees)
            rate = response['rates'][code]
            amount_without_fees = amount * rate

            #print 2 decimal places
            format_amount_without_fees = "{:.2f}".format(amount_without_fees)

            total_amount = amount  + fees

            #print 2 decimal places
            format_total_amount = "{:.2f}".format(total_amount)
            print(f"\n           Money from {sender_firstname} {sender_lastname} is on the way!")
            print("*********************************************************************************\n")

            # Program to generate a random number between 0 and 9 
            reference_number = random.randint(1000000000,9999999999)

            print(f"""
            Reference No: {reference_number}
            Receiver: {receiver_firstname} {receiver_lastname}
            Country code: {code} , {receiver_country}
            Receiver amount: {format_amount_without_fees} {code} 
            Total charge for the transaction: {format_total_amount} {baseCurrency}\n\n """)
            
        else:
            print("Thank you for visting our store")

    else:
        #Implement the logic for others countries...
        print("This transaction is not currently available in your country\n\n")

def main():
    transaction_info()

if __name__ == "__main__":
    main()

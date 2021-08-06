#!/usr/bin/env python3

import requests

API = "https://opentdb.com/api.php?amount=5&category=24&difficulty=easy&type=multiple"

play = "yes"

#while play == "yes":
response = requests.get(f"{API}")
questions = response.json()
cards = questions['results'][3]
#print(cards)
print(cards['question'])
print("********************************************************************************************************************")
print("Pick one of the answers below: ")
print(cards['correct_answer'])
print(cards['incorrect_answers'][0])
print(cards['incorrect_answers'][1])
print(cards['incorrect_answers'][2])
print("********************************************************************************************************************")
answer = input(" Your answer: ")

if answer == cards['correct_answer']:
    print("Your are correct!!")
else:
    print(f" Correct answer is : {cards['correct_answer']} !!!")

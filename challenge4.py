#!/usr/bin/python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
# animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]

def NE_animals() :
    for ne_animal in farms :
        if ne_animal["name"] == "NE Farm":
            print(ne_animal["agriculture"])

NE_animals()

def choose_farm() :
    select = input("choose a farm from the list: [NE Farm, W Farm, SE Farm]").lower().strip()
    for farm in farms:
        if farm["name"] == select :
            print(farm["agriculture"])

choose_farm()

def choose_animalFarm() :
    select = input("choose a farm from the list: [NE Farm, W Farm, SE Farm]").lower().strip()

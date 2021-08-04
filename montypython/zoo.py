#!/usr/bin/env python3

#visitor answer to visit the farm
answer = "yes"

print("********************************** WELCOME TO Dallas ZOO******************************************"+"\n\n")
print(" Instruction \n"+ " To visit each animal section type a keyword :")
print(" tiger\n"+" elephant\n"+" cheetah\n"+" giraffe\n\n")

#use a dictionaries to match the visitor keyword with the right section to visit
animal = {
    "tiger": "********************* WELCOME TO TIGER SECTION **************************",
    "elephant": "********************* WELCOME TO ELEPHANT SECTION **************************",
    "cheetah": "********************* WELCOME TO CHEETAH SECTION **************************",
    "giraffe": "*********************WELCOME TO GIRAFFE SECTION ***************************"
}

#function to say goodbye for visiting the zoo
def goodbye_message() :
    print("Thank you for visiting Dallas zoo! Have a wonderful day")

while answer == "yes":

    #prompt the visitor to enter a section to visit
    visit = input("Please enter an animal name to visit ")
    if visit  == "tiger":
        print(animal[visit])
        print("Sumatran tigers have more hair around their heads than the other types of tigers, giving them")
        print("a more bearded or maned appearance. They are also the smallest and rarest subspecies of tiger.")
        print("Tigers are one of the few cats that actually like water. They even have partially webbed toes.")
        print("A tiger’s night vision is six times more acute than a human’s!")
        answer = input("Would you like to visit a section again? yes or no ")
        if answer == "no":
            goodbye_message()
    elif visit  == "elephant":
        print(animal[visit])
        print("Elephant herds consist of one or more adult females and their immature offspring ")
        print("who feed, rest, move, and interact in a coordinated manner and are closely bonded.")
        print("An adult elephant can consume up to 300 pounds of roots, grasses, fruit, bark, leaves, and branches in a single day.")
        answer = input("Would you like to visit a section again? yes or no ")
        if answer == "no":
            goodbye_message()
    elif visit  == "cheetah":
        print(animal[visit])
        print("With short bursts up to 70 miles per hour, cheetahs are the fastest mammals on earth!")
        print("Some cats purr and some cats roar, but none do both. Lions and tigers roar; cheetahs purr.")
        answer = input("Would you like to visit a section again? yes or no ")
        if answer == "no":
            goodbye_message()
    elif visit  == "giraffe":
        print(animal[visit])
        print("Giraffes can live 10-15 years in the wild and over 25 years in human care.")
        print("These gentle giants are the world’s tallest living land animals.")
        print("An adult male can be 18 feet tall – that’s taller than three adult humans!")
        answer = input("Would you like to visit a section again? yes or no ")
        if answer == "no":
            goodbye_message()
    else:
        print("Wrong input! Please enter a valid animal name such as [tiger] [elephant] [cheetah], and [giraffe] ")

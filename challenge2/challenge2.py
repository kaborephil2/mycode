#!/usr/bin/env python3

#Creates Icecream list

icecream= ["flavors", "salty"]

#Creates TLG students list

tlgclass= ["Adrian","Bikash","Chas","Chathula","Chris","Hongyi","Jauric","Joe L.","Joe V.","Josh","Justin","Karlo","Kerri-Leigh","Jason","Nicholas","Peng","Philippe","Pierre","Stephen","Yun"]

#Append the number 99 to the icecream list

icecream.append(int(99))

student_range = input("Enter a number between [1-19] : ")

print(f"{icecream[2]} {icecream[0]}, {tlgclass[int(student_range)]} chooses to be {icecream[1]}") 

#!/usr/bin/env python3

fizz_file = open("numfile.txt", "r")
content = fizz_file.read()
print(content)

fizz_list = content.split(",")
fizz_file.close()
print(fizz_list)

counter = 0
for element in fizz_list :
    if element.contain("3"):
        counter += 1



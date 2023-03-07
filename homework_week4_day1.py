#!/usr/bin/python

# Exercise 1: filter out the blank strings
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

filtered_places = list(filter(lambda place: place and place[0].isalpha(), places))
print(filtered_places)

# Exercise 2: sort list by last name
authors = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
new_list = []
# for name in authors:
#     new_list.append(name.split())
# print(new_list)
new_list = list(map(lambda name: name.split(), authors))
sorted_list = sorted(new_list, key=lambda name: name[-1].lower())
joined_sorted_list = list(map(lambda name: ' '.join(name), sorted_list))
print(joined_sorted_list)

# Exercise 3: convert to fahrenheit
# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angeles",44),("Miami",29)]

def convert_to_fahrenheit(c):
    return (c * 9 / 5) + 32

fahrenheit_list = list(map(lambda place: place[1] * 9/5 + 32, places))
print(fahrenheit_list)

# Exercise 4: Fibonacci up to specified member

# Exercise 5: 
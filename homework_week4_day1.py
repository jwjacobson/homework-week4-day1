#!/usr/bin/python

# Exercise 1: filter out the blank strings
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

print(list(filter(lambda place: place and place[0].isalpha(), places)))

# Exercise 2: sort list by last name
authors = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

new_list = list(map(lambda name: name.split(), authors))
sorted_list = sorted(new_list, key=lambda name: name[-1].lower())

print(list(map(lambda name: ' '.join(name), sorted_list)))

# Exercise 3: convert to fahrenheit
# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angeles",44),("Miami",29)]

def convert_to_fahrenheit(c):
    return (c * 9 / 5) + 32

print(list(map(lambda place: place[1] * 9/5 + 32, places)))

# Exercise 4: Fibonacci up to specified member
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def print_fibonacci(num):
    for nums in range(num + 1):
        print(f"Iteration {nums}: {fibonacci(nums)}")

print_fibonacci(10)

# Exercise 5: generator of squares down to 0
def falling_squares(start, step=1):
    stop = 0
    while start > stop:
        yield start**2
        start -= step

for x in falling_squares(10):
    print(x)
#!/usr/bin/python

# Desc: find how many houses presents were delivered with 1 santa

from itertools import product 

text_file = open("problem.dat", "r")

# Starting coordinates
x = 0
y = 0

#empty list that will hold coordinates of houses
my_list = []

f = text_file.read()

for element in range(0, len(f)):
  if f[element] == "^":
    x = x + 1
  elif f[element] == "v":
    x = x - 1
  elif f[element] == ">":
    y = y + 1
  elif f[element] == "<":
    y = y - 1

  my_list.append("{},{}".format(x,y))

# + 1 accounts for the beginning house
print(len(set(my_list)) + 1)
    
#!/usr/bin/python

# Desc: find how many houses presents were delivered with alternating santas

# cycle between 0 and 1 
from itertools import cycle
myIterator = cycle('01')
print(next(myIterator))

text_file = open("problem.dat", "r")
f = text_file.read()

# Starting coordinates for first Santa
x1 = 0
y1 = 0

# Starting coordinates for second Santa
x2 = 0
y2 = 0 

#variable to determine which santa moves
prio = 0

#empty lists that will hold coordinates of houses
santa1 = ['0,0']
santa2 = ['0,0']

print(santa1)
print(santa2)

for element in range(0, len(f)):
  # next(myIterator)
  if str(next(myIterator)) == str(0):
    if f[element] == "^":
      x1 = x1 + 1
    elif f[element] == "v":
      x1 = x1 - 1
    elif f[element] == ">":
      y1 = y1 + 1
    elif f[element] == "<":
      y1 = y1 - 1
    santa1.append("{},{}".format(x1,y1))


  else:
    if f[element] == "^":
      x2 = x2 + 1
    elif f[element] == "v":
      x2 = x2 - 1
    elif f[element] == ">":
      y2 = y2 + 1
    elif f[element] == "<":
      y2 = y2 - 1
    santa2.append("{},{}".format(x2,y2))  
   

#remove dups from sets
print(len(santa2))
print(len(santa2))

combined_santa = santa1 + santa2
print(len(combined_santa))
print(len(set(combined_santa)))




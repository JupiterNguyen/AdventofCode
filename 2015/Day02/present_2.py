#!/usr/bin/python

# Desc: find two numbers that add up to 2020 and multiply them

text_file = open("problem.dat", "r")

lines = text_file.readlines()
dimensions = [x.replace('\n', '') for x in lines]

def smallest_perimeter(l,w,h):
  a = (2*l) + (2*w)
  b = (2*l) + (2*h)
  c = (2*h) + (2*w)
  if a < b and a < c :
    smallest = a
  elif b < c :
    smallest = b
  else :
    smallest = c
  return(smallest)

def bow_length(l,w,h):
  bow = l*w*h
  return(bow)

ribbon_total = 0

for i in dimensions:
  numbers = i.split('x')

  ribbon_total = ribbon_total + smallest_perimeter(int(numbers[0]),int(numbers[1]),int(numbers[2])) + bow_length(int(numbers[0]),int(numbers[1]),int(numbers[2]))
print(ribbon_total)
text_file.close()

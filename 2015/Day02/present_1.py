#!/usr/bin/python

# Desc: find two numbers that add up to 2020 and multiply them

text_file = open("problem.dat", "r")

lines = text_file.readlines()
dimensions = [x.replace('\n', '') for x in lines]

def surface_area(l,w,h):
  s_area = 2*l*w + 2*w*h + 2*h*l
  return(s_area)

def smallest_area(l,w,h):
  a = l*w
  b = l*h
  c = w*h
  if a < b and a < c :
    smallest = a
  elif b < c :
    smallest = b
  else :
    smallest = c
  return(smallest)

total = 0

for i in dimensions:
  numbers = i.split('x')
  surface_area(int(numbers[0]),int(numbers[1]),int(numbers[2]))
  smallest_area(int(numbers[0]),int(numbers[1]),int(numbers[2]))
  total = total + surface_area(int(numbers[0]),int(numbers[1]),int(numbers[2])) + smallest_area(int(numbers[0]),int(numbers[1]),int(numbers[2]))
  
print(total)

#!/usr/bin/python

# Desc: find the position of the character that equals -1 


text_file = open("problem.dat", "r")

f = text_file.read()
count = 0 
for element in range(0, len(f)):
  if f[element] == "(":
    count = count + 1 
  elif f[element] == ")":
    count = count - 1
  
  if count == -1: 
    print(element + 1)
    

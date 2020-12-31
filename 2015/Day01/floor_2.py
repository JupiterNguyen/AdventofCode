#!/usr/bin/python

# Desc: find the position of the character that equals -1 
# --- Part Two ---

# Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

# For example:

#     ) causes him to enter the basement at character position 1.
#     ()()) causes him to enter the basement at character position 5.

# What is the position of the character that causes Santa to first enter the basement?


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
    
text_file.close()
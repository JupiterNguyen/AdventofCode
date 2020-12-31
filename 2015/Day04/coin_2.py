#!/usr/bin/python

# Desc: 
# --- Part Two ---

# Now find one that starts with six zeroes.

import hashlib

text_file = open("problem.dat", "r")
f = text_file.read()

number = 0

condition = 1
while condition == 1:

  setup = f + str(number)
  result = hashlib.md5(setup.encode()) 

  if result.hexdigest().startswith('000000'):
    print(number)
    condition = condition + 1
  else:
    number = number + 1

text_file.close()

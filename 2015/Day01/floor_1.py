#!/usr/bin/python

# Desc: find two numbers that add up to 2020 and multiply them

text_file = open("problem.dat", "r")
f = text_file.read()
open = f.count('(')
close = f.count(')')

floor = open - close
print(floor)
text_file.close()
#!/usr/bin/python

# Desc: find two numbers that add up to 2020 and multiply them

text_file = open("numbers.dat", "r")

lines = text_file.readlines()
numbers = [x.replace('\n', '') for x in lines]
numbers = list(map(int, numbers))

for i in enumerate(numbers):
  sum = i + i+1
  print(sum)
  print("sum == {}".format(sum(i,0)))


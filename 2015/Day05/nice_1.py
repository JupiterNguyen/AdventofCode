#!/usr/bin/python

# Desc: 
# --- Day 5: Doesn't He Have Intern-Elves For This? ---

# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

#     It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#     It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#     It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

# For example:

#     ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
#     aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
#     jchzalrnumimnmhp is naughty because it has no double letter.
#     haegwjzuvuyypxyu is naughty because it contains the string xy.
#     dvszwmarrgswjxmb is naughty because it contains only one vowel.

# How many strings are nice?

import itertools
import collections

text_file = open("problem.dat", "r")
lines = text_file.readlines()
strings = [x.replace('\n', '') for x in lines]
strings = list(map(str, strings))

dict = collections.defaultdict(int)

#conditionals
vowel_conditional = ['a','e','i','o','u']
bad_strings = ['ab','cd','pq','xy']

#list to hold nice strings
nice_list = []

#vowel count
def vowel_count(str): 
  
  count = 0
    
  for char in str: 
    if char in vowel_conditional: 
        count = count + 1

  if count >= 3:  
    check_bad(str)

#remove bad strings
def check_bad(str):
  if not any(map(str.__contains__, bad_strings)):
    dup(str)

# check for duplicate characters in a row
def dup(str):
  
  for i,char in enumerate(str[:-1]):
    if str[i+1] == char:
      nice_list.append(str)


for string in strings: 
  nice_list = list(filter(None, nice_list))
  vowel_count(string)
  
print(len(set(nice_list)))
text_file.close()
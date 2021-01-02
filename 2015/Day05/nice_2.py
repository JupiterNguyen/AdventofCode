#!/usr/bin/python

# Desc: 
# --- Part Two ---

# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

#     It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#     It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

# For example:

#     qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
#     xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
#     uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
#     ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

# How many strings are nice under these new rules?

import re

text_file = open("problem.dat", "r")
lines = text_file.readlines()
strings = [x.replace('\n', '') for x in lines]
strings = list(map(str, strings))

nice_list = []

between = re.compile(r"(.).\1")
dup = re.compile(r"(..).*\1")

def nice(word):
  if between.search(word) is None:
    return False
  return dup.search(word) is not None
          
for string in strings:
  if nice(string):
    nice_list.append(string)

print(len(nice_list))
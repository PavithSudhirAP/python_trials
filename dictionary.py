# creates a simple dictionary based on the json file

import json
from difflib import get_close_matches as match

data = json.load(open("dictionary.json"))
keys = data.keys()

def meaning(word):
  word = word.lower()
  if word in data:
    return data[word]
  else:
    matched = match(word,keys)[0]
    print("Did you mean {} instead of {} ?".format(matched,word))
    return "Try again!!"

word = input("Enter word= ")

print(meaning(word))

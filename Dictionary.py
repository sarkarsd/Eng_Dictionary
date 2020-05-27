import json
from difflib import get_close_matches
import os

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data.keys():
        return data[w]
    elif w.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data:  # in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead ? Enter Y if Yes or N if No : " % get_close_matches(w, data.keys())[0])
        if yn == 'Y' or yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N' or yn == 'n':
            return "The word doesn't exist"
    else:
        return "The word does not exist. Please double check it"


os.system('color')

while True:
    word = input("Enter a word: ")
    output = translate(word)
    if type(output) is list:
        for i in output:
            print("'\33[93m'%s'\33[0m'" % i, "\n")
    else:
        print(output)





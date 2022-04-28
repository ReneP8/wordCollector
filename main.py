import json
import requests
import html
import time
from os.path import exists


def fetchNewNoun():
    word = str(requests.get('https://alex-riedel.de/randV2.php').content)
    word = word[3:-2]
    return word


def writeIntoFile(word):
    jsonFile = open("words.json", "a", encoding='utf8')
    jsonFile.write(word)
    jsonFile.write(",")
    jsonFile.write("\n")
    jsonFile.close()


def existsInFile(word):
    file = open("words.json", "r", encoding='utf8')
    content = file.read()
    file.close()
    return word in content


def createFile():
    file = open("words.json", "w", encoding='utf8')
    file.write("")
    file.close()


words = 0
duplicates = 0
while words < 1000:
    word = html.unescape(fetchNewNoun())

    if not exists("words.json"):
        createFile()

    if not existsInFile(word):
        writeIntoFile(word)
        words += 1
        if words % 50 == 0:
            print(str(words) + " words fetched")
    else:
        duplicates += 1
        print("found duplicates: " + str(duplicates))

print("Finished")

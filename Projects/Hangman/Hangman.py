import json, ssl
from random import Random
import string
import urllib.request
from RandomCryptoCoin import RandomCryptoCoin

#This code prevents error, although it is not recommended to use or necessary.

ssl._create_default_https_context = ssl._create_unverified_context

#Here I create a function in order to acquire my word from random data in an api. I first start the function by using the word def, declaring the function. I then simply added getWord as a function name and then I added the parameters with the parenthesis. After all was said and done, I closed it with a colon.

def getWord():

    #Here I create a variable, calling it cryptocoinLink, as its definition is the very link from which I will be calling a respective word from. The link is the random data in an api that I mentioned earlier.

    cryptocoinLink = "https://random-data-api.com/api/crypto_coin/random_crypto_coin"

    #I create another variable yet again, this time for a urllib request. In essence, I request the URL from the variable I had created earlier, cryptocoinLink, all whilst naming the variable request.

    request = urllib.request.Request(cryptocoinLink)

    #Furthermore, I create a new variable called requestWord. With it, I use json to load the urllib request and open the url, effectively making it "read" all that is written in the website. 

    requestWord= json.loads(urllib.request.urlopen(request).read())

    #Yet again, I have created another variable, this time I call it present_coin, alluding to the fact that it is the current crypto coin I am using, not just any. And after my previous line of code "read" the website, it already knows that RandomCryptoCoin exists and I then request a word from inside the RandomCryptoCoin.

    present_coin = RandomCryptoCoin(**requestWord)

    #Then I return the present_coin along with its name. I achieve this by using the present_coin variable and appending it with .coin_name, which is a variable in the random crypto coin api.
    
    return present_coin.coin_name

#Here I create a variable for the whole function of getWord, in which I use myWord to replace it and I also add the .upper() method to it, which converts all lowercase letters in a string into uppercase letters and returns them. 

myWord = getWord().upper()

#Here I create a new variable called stages. Its purpose is to reassure further lines of code that the stages of the steps begin at stage 0, the very first step in the steps list.

stages = 0

#Here I create a yet another variable with the name Steps. Its definition consists of a json list that contains each and every step to my hangman. Not the game, but hangman itself, with my goal being that after every wrong answer, the steps would increase by 1. I achieve this by using json formatting and adding my own implementations of the hangman.

Steps = ["""
        |____________|
        |            |
        |
        |
        |
        |
        |_____________

        """,
        """
        |____________|
        |            |
        |            O
        |
        |
        |
        |_____________          
        """,
        """
        |____________|
        |            |
        |            O
        |            |
        |
        |
        |_____________

        """,
        """
        |____________|
        |            |
        |            O
        |            |\\
        |
        |
        |_____________
        """,
        """
        |____________|
        |            |
        |            O
        |          //|\\
        |
        |
        |_____________
        """,
        """
        |____________|
        |            |
        |            O
        |          //|\\
        |          //
        |
        |_____________
        """,
        """
        |____________|
        |            |
        |            O
        |          //|\\
        |          // \\
        |
        |_____________
        """
]

Incorrect_integers = ["0","1","2","3","4","5","6","7","8","9"]
Incorrect_characters = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","`","~","[","{","]","}","\\","|",";",":",",","<",">","/","?"]
UsedLetters = []


def getInput():

    while(True):
        letter = input("Type a letter of your choice, be wary, as a wrong letter will cost you:")
    
        if (len(letter) !=1):
            continue

        if letter in Incorrect_characters:
            print("No puedes usar special characters, un bofetón")
            continue
        
        if letter in Incorrect_integers:
            print("No puedes usar integers, un bofetón")
            continue
        
        if stages == 7:
            print("Perdiste, un bofetón")
            continue

        if letter in UsedLetters:
            print("Ya usaste esta, un bofetón")
            continue

        UsedLetters.append(letter)
        return letter

def printword():
    Temp:str = ""
    for letter in myWord:
        if letter in UsedLetters:
            Temp += letter
        else:
            Temp += "_"
    return Temp

while True:
    print (Steps[stages])
    print(printword())
    letter =  getInput().upper()
    if  letter not in myWord:
        stages = stages +1
import json, ssl
import urllib.request
from RandomCryptoCoin import RandomCryptoCoin

ssl._create_default_https_context = ssl._create_unverified_context

Incorrect_Letters = []

def getWord():

    cryptocoinLink = "https://random-data-api.com/api/crypto_coin/random_crypto_coin"

    request = urllib.request.Request(cryptocoinLink)

    requestWord= json.loads(urllib.request.urlopen(request).read())

    present_coin =RandomCryptoCoin(**requestWord)
    
    return present_coin.coin_name

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
Incorrect_characters = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","`","~","[","{","]","}","\\","|",";",":",",","<",".",">","/","?"]

def getInput():
    while(True):
        letter = input("Type a letter of your choice, be wary, as a wrong letter will cost you")

        if (len(letter) !=1):
            continue

        if letter in Incorrect_characters:
            print("Esta mal, un bofetón")
            continue
        
        if letter in Incorrect_integers:
            print("Esta mal, un bofetón")
            continue

        return letter

while True:
    print (Steps[0])
    getInput()
    # print() 

# getInput()

print(getWord())
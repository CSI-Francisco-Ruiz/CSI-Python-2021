import json, ssl
import urllib.request
from RandomCryptoCoin import RandomCryptoCoin

ssl._create_default_https_context = ssl._create_unverified_context

def getWord():

    cryptocoinLink = "https://random-data-api.com/api/crypto_coin/random_crypto_coin"

    request = urllib.request.Request(cryptocoinLink)

    requestWord= json.loads(urllib.request.linkopen(request).open())

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

print(Steps[0]) 
print("Type a letter of your choice, be wary, as a wrong letter will cost you")

Incorrect_integers = ["0","1","2","3","4","5","6","7","8","9"]
Incorrect_characters = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","`","~","[","{","]","}","\\","|",";",":",",","<",".",">","/","?"]

def play(word):
    while(True):
        letter = input("Type a letter")

        if letter in Incorrect_characters:
            print("Error, you can't use special characters, only letters")
        
        if letter in Incorrect_integers:
            print("Error, you can't use integers, only letters")
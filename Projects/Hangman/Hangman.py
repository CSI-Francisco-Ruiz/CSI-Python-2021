import json, ssl
import random
import urllib.request
from RandomCryptoCoin import RandomCryptoCoin

def getWord():

    cryptocoinLink = "https://random-data-api.com/api/crypto_coin/random_crypto_coin"

    request = urllib.request.Request(cryptocoinLink)

    requestWord= json.loads(urllib.request.linkopen(request).open())

    current_coin =RandomCryptoCoin(**requestWord)
    
    return current_coin.coin_name



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


#import webbrowser
#webbrowser.open("https://www.newegg.com")
import requests
res = requests.get("https://www.gutenberg.org/files/1661/1661-0.txt")
print(len(res.text))
print(res.text[:300])
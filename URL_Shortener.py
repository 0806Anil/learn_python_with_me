# URL Shortener

import pyshorteners

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    print("Shortened URL:", shortened_url)

url = input("Enter URL to shorten: ")
shorten_url(url)

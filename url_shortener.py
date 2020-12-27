from pyshorteners import Shortener
from credentials import API_KEY

input_url = input("Paste URL Here: ")
shorten_url = Shortener(api_key=API_KEY)

print(f"Here Your Shorten URL: {shorten_url.bitly.short(input_url)}")

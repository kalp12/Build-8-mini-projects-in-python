import pyshorteners
url = input("Enter url:")
shortener=pyshorteners.Shortener()
a=shortener.tinyurl.short(url)
print(a)
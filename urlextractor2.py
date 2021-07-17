from urllib.request import urlopen


page = urlopen("http://www.google.com")
sourcecode = page.read()
print(sourcecode)
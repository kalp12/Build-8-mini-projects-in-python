from urllib.request import urlopen


page = urlopen("http://www.google.com")
print(page.headers)
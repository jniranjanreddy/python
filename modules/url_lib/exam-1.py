
from urllib import urlopen
# print(dir(urllib))
html = urlopen("https://www.pythonscraping.com/exercises/exercise1.html")
print(html.read())
# for code in html:
#     print(code)

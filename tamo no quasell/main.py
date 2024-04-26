import request
from bs4 import beautifulsoup

url = "https://on.wikipedia.org/wiki/python_(programming_language"

response = requests.get(url)

soup = beautifulsoup(response.text, 'html.parser')

title = soup.find('h1',{'id':'firstheading}).text

print('titulo da pagina:',title)


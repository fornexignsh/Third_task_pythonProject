import requests
from bs4 import BeautifulSoup
from spellchecker import SpellChecker

def check_spelling(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    page_content = soup.get_text()
    spell = SpellChecker()
    words = page_content.split()
    misspelled = spell.unknown(words)
    return misspelled

main_url = "https://nexign.com/ru"
response = requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all('a', href=True)

print("Орфография на главной странице Nexign:")
main_misspelled = check_spelling(main_url)
print(main_misspelled)

for link in links[:5]:
    url = link['href']
    if not url.startswith("http"):
        url = main_url + url
    print(f"Орфография на странице {url}:")
    misspelled = check_spelling(url)
    print(misspelled)

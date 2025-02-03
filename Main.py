import requests
from bs4 import BeautifulSoup
import time

def getresults():
    Word = input("Enter your word: ")

    url = f'https://www.thesaurus.com/browse/{Word}'
    url2 = f'https://promova.com/antonyms-of/{Word}'
    url3 = f'https://www.merriam-webster.com/dictionary/{Word}'



    response = requests.get(url)
    html_content = response.text
    response2 = requests.get(url2)
    html_content2 = response2.text
    response3 = requests.get(url3)
    html_content3 = response3.text

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')
    soup2 = BeautifulSoup(html_content2, 'html.parser')
    soup3 = BeautifulSoup(html_content3, 'html.parser')


    syn = soup.find_all("a", class_="Bf5RRqL5MiAp4gB8wAZa",limit=4)
    ant = soup2.find_all("p", class_="synonyms_list_section_text__dJHzI",limit=4)
    pro = soup3.find(class_="prons-entries-list-inline")
    try:
        pro = [x.text for x in pro][1]
    except:
        pro = "N/a"
    try:
        worldhistory = soup3.find("p", class_="et").text
    except:
        worldhistory = "N/A"
    try:
        firstused = soup3.find("p", class_="ety-sl pb-3").text
    except:
        firstused = "N/A"
    try:
        example = soup3.find_all(class_="sub-content-thread ex-sent sents", limit=3)
        example = [x.text for x in example if x.text != "\n"]
    except:
        example = []
    try:
        definition = soup3.find(class_="dtText").text
    except:
        definition = "N/A"
    try:
        partofspeech = soup3.find(class_="important-blue-link").text
    except:
        partofspeech = "N/A"















    syn = [x.text for x in syn]
    ant = [x.text for x in ant]








    Results = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{str(Word)}').json()

    print(f'\n Definition {definition} \n part of speech: {partofspeech} \n synonyms:{syn}\n antonyms:{ant} \n pronounce:{pro} \n world history:{worldhistory} \n firstused: {firstused}')
    try:amount = int(input(f"{len(example)} examples found how many would you like to see?"))
    except:
        getresults()

    if amount > len(example):
        getresults()


    for x in range(0,int(amount)):
        print(example[x])


    print("\n\n")

    getresults()

getresults()


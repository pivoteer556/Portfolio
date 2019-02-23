#CS 3150
#Homework 1
#3150HW1Wilkening.py
from requests import get
import nltk
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup 

def main():
    home = 'http://shakespeare.mit.edu/'
    myContent = fetchFromURL(home) #returns html code
    firstLinks = get_target_urls(myContent)#converts said HTML to links
    secondLinks = []
    appendLinks = []
    for link in firstLinks[:-5]:
        link = home+link
        appendLinks.append(link)
        newContent = fetchFromURL(link)
        secondLink = get_second_urls(newContent)
        secondLinks.append(secondLink)
    finalLinks = []
    flatList = [item for myList in secondLinks for item in myList] #turns list of lists into list
    lcv = 0
    for myList in secondLinks:
        for url in myList:
            link = appendLinks[lcv]
            newLink = link.replace('index.html', url)
            finalLinks.append(newLink)
        lcv+=1
    #print(finalLinks)
    for link in firstLinks[-5:]:
        link = home+link
        finalLinks.append(link)
    for link in finalLinks:
        data = fetchFromURL(link)
        printable = parse(data)
        output(printable, link)

def parse(data):
    data = BeautifulSoup(data, 'html.parser').text
    tokens = nltk.word_tokenize(data)
    return tokens
    
def output(printable, link):
    link = link[27:]
    link = link.replace('/','')
    f = open(link+'.txt', 'w+')
    printable = ' '.join(printable)
    f.write(printable)
    
def fetchFromURL(url):
    ###
    #Attempt to fetch content from URL via HTTP GET request. If it's HTML/XML return otherwise
    #don't do anything
    ###
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during request to {0}:{1}' . format(url, str(e)))
        return None

def is_good_response(resp):
    #Returns True if response looks like HTML
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
#    log those errors or you'll regret it later...
    print(e)

def get_target_urls(target):
#    Example of isolating different parent elements to gather subsequent URLs
    soup = BeautifulSoup(target, 'html.parser')
    linkList= []
    for row in soup.find_all('td'):
        #print(row)
        for link in row.find_all('a'):
            link = link.get('href')
            if 'tech.mit.edu' not in link and 'www.python.org' not in link:
                linkList.append(link)
    return linkList
def get_second_urls(target):
#    Example of isolating different parent elements to gather subsequent URLs
    soup = BeautifulSoup(target, 'html.parser')
    #print(soup)
    linkList= []
    for link in soup.find_all('a')[3:]:
        link = link.get('href')
        if 'tech.mit.edu' not in link and 'www.python.org' not in link:
            linkList.append(link)
    return linkList
main()

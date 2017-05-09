import os
import urllib


def readFile():

    file_dir = os.curdir+'/movie_quotes.txt'
    quote = open(file_dir)
    file_content = quote.read()
    quote.close()
    return file_content

def check_profanity(text):
    response = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    return  response.read()


print(check_profanity(readFile()))
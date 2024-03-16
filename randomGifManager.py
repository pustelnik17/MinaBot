import requests
import numpy
from bs4 import BeautifulSoup


def getRandomGif(url):
    soup = BeautifulSoup(requests.get(url).text, features="html.parser")
    gifs = [element["src"] for element in soup.find_all("img")]
    return numpy.random.choice(gifs)

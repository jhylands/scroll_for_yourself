import requests
from bs4 import BeautifulSoup
# The purpose of this module is simply to get a feed
# So at the moment this is basically the requests get call

def get_feed(url):
    result = requests.get(url)
    if result.status_code != 200:
        raise Exception(result)
    return result.content

def parse(result):
    soup = BeautifulSoup(result, features='xml')
    articals = soup.findAll("item")
    # Then at this point I want to deviate from what the example does
    # I want to be able to record all the data found in the xml file while not
    # having to structure it as such.
    # The idea is that this then gets put into a neo4j database.



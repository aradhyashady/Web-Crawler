import requests
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''
		
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
		

def validate_url(url):
    if not "http" in url:
        raise ValueError("This is not a valid url")
    return url


def get_input():
    url = input("What is your url? ")
    try:
        validate_url(url)
    except ValueError:
        print("This is an invalid url")
        return get_input()
    return url
	

def main():
    url = get_input()
    with urllib.request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    type(soup)
    print (soup.prettify())
    print("\nDomains Associated with the URL:\n")
    print (get_domain_name(url))
    print("\nLinks associated with URL\n")
    all_links = soup.find_all("a") 
    for link in all_links:
         print(link.get("href")) 
	
main()

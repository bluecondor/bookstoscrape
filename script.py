from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd

pages = []
prices = []
stars = []
titles = []
urlss = []

pages_to_scrape = 1

# Increment trough the pages
for i in range(1, pages_to_scrape + 1):
    url = "http://books.toscrape.com/catalogue/page-{}.html".format(i)
    pages.append(url)

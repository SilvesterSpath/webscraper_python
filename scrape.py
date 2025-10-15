import requests
from bs4 import BeautifulSoup
import json

def fetch_books(page: int):
  url = f"https://books.toscrape.com/catalogue/page-{page}.html"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  print(soup.prettify())
  books = soup.find_all("article", class_="product_pod")
  for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    print(title, price)

def main():
  fetch_books(1)

if __name__ == "__main__":
  main()
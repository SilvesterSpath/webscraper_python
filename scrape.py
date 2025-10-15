import requests
from bs4 import BeautifulSoup
import json

def fetch_books(page: int):
  url = f"https://books.toscrape.com/catalogue/page-{page}.html"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  print(soup.prettify())

  book_list = []
  books = soup.find_all("article", class_="product_pod")
  for item in books:
    title = item.find("h3").find("a")["title"]
    price = item.find("p", class_="price_color").text
    stock = item.find("p", class_="instock availability").text.strip()
    rating = item.find("p", class_="star-rating")["class"][1]
    link = item.find("h3").find("a")["href"]

    book_list.append({
      "title": title,
      "price": price,
      "stock": stock,
      "rating": rating,
      "link": f"https://books.toscrape.com/catalogue/{link}"
    })

  return book_list

def main():
  all_books = []
  max_page = 10

  for current_page in range(1, max_page + 1):
    books_on_page = fetch_books(current_page)
    all_books.extend(books_on_page)
  print(f"Scraped {current_page} books across {max_page} pages")

  # Save data to file
  with open("books.json", "w", encoding="utf-8") as file:
    json.dump(all_books, file, indent=4, ensure_ascii=False)
  print("Data saved to books.json")

if __name__ == "__main__":
  main()
import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops?page="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

all_data = []
exchange_rate = 91.0765

for page in range(1, 6):   # total 5 pages
    url = base_url + str(page)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("div", class_="thumbnail")

    for product in products:
        name = product.find("a", class_="title").get_text(strip=True)
        price = product.find("h4", class_="price").get_text(strip=True)
        description = product.find("p", class_="description").get_text(strip=True)

        # Reviews (correct way)
        review_span = product.find("span", itemprop="reviewCount")
        reviews = int(review_span.get_text(strip=True)) if review_span else 0

        # Rating (correct way)
        rating_p = product.find("p", attrs={"data-rating": True})
        stars = int(rating_p["data-rating"]) if rating_p else 0

        all_data.append({
            "Name": name,
            "Price_INR": round(float(price.replace("$", "")) * 91.0765),
            "Description": description,
            "Reviews": reviews,
            "Rating": stars
        })
df = pd.DataFrame(all_data)

print(df.head())
print("Total Products:", len(df))

df.to_csv("laptops_dataset.csv", index=False)


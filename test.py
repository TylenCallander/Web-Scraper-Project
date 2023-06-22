from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price

# Prompt the user for the cryptocurrency they want to see
while True:
    cryptocurrency = input("Enter the cryptocurrency you want to see (or 'exit' to quit): ")

    if cryptocurrency == "exit":
        break

    if cryptocurrency in prices:
        print(f"The price of {cryptocurrency} is {prices[cryptocurrency]}")
    else:
        print("Invalid cryptocurrency entered or not in the top 10.")

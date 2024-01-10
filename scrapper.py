import requests
from bs4 import BeautifulSoup

page = requests.get('https://books.toscrape.com')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get('https://books.toscrape.com', headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

# get all "li" elements
# in the ".product_prod" element
soup.find(class_='product_prod').find_all('li')

product_prod = []

productProd_elements = soup.find_all('div', class_='product_prod')

for productProd_element in productProd_elements:
    # extract the text of the product
    text = productProd_element.find('h3', class_='a').text
    # extract the price of the prodcut
    price_color = productProd_element.find('p', class_='price_color').text
    # extract the availability of the prodcut
    instock_availability = productProd_element.find('i', class_='icon_ok').text

product_prod.append(
    {
        'h3': text,
        'p': price_color,
        'i': instock_availability
    }
)

# the URL of the home page of the target website
base_url = 'https://books.toscrape.com'

# retrieve the page and initializing soup...

# get the "Next →" HTML element
next_li_element = soup.find('li', class_='next')

# if there is a next page to scrape
while next_li_element is not None:
    next_page_relative_url = next_li_element.find('a', href=True)['href']

    # get the new page
    page = requests.get(base_url + next_page_relative_url, headers=headers)

    # parse the new page
    soup = BeautifulSoup(page.text, 'html.parser')

    # scraping logic...

    # look for the "Next →" HTML element in the new page
    next_li_element = soup.find('li', class_='next')


import csv

# scraping logic...

# reading  the "product_prod.csv" file and creating it
# if not present
csv_file = open('product_prod.csv', 'w', encoding='utf-8', newline='')

# initializing the writer object to insert data
# in the CSV file
writer = csv.writer(csv_file)

# writing the header of the CSV file
writer.writerow(['h3', 'p', 'i'])

# writing each row of the CSV
for product_prod in product_prod:
    writer.writerow(product_prod.values())

# terminating the operation and releasing the resources
csv_file.close()
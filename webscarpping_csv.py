import requests
from bs4 import BeautifulSoup
import csv
import time

# URL Template
base_url = "https://www.cypherhunter.com/en/c/products/page/{}"

# To fool the website because its blocking unknow calls
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36"
}

# csv file to write our data
with open("cypherhunter_products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "URL"])  

    # Totally there are 503 pages
    for page_num in range(1, 504):
        url = base_url.format(page_num)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            products = soup.select('div.grid a')  
            for product in products:
                title = product.get('title', 'N/A')
                href = product.get('href', 'N/A')
                full_url = f"https://www.cypherhunter.com{href}" if href.startswith('/en') else href
                writer.writerow([title, full_url])  
            print(f"Page {page_num} processed successfully.")
            
            # delay to check if its working
            time.sleep(1)
        
        else:
            print(f"Failed to retrieve page {page_num}. Status code: {response.status_code}")

print("cypherhunter_products.csv over")

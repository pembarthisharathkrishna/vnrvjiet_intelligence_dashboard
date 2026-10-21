import requests
from bs4 import BeautifulSoup
import os

pages_to_scrape = [
    "https://vnrvjiet.ac.in/training-placement/",
    "https://vnrvjiet.ac.in/nirf/"
]

required_keywords = [
    "Placement-Statistics",
    "vnrplacements2023",
    "NIRF",
    "nirf"
]

pdf_links = []

for page_url in pages_to_scrape:
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, "html.parser")

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if ".pdf" in href.lower():
            for key in required_keywords:
                if key.lower() in href.lower():

                    clean_href = href.split("#")[0]

                    if clean_href.startswith("http"):
                        full_link = clean_href
                    else:
                        full_link = "https://vnrvjiet.ac.in" + clean_href

                    if full_link not in pdf_links:
                        pdf_links.append(full_link)

print("Analytics Relevant PDFs Found:")
for link in pdf_links:
    print(link)

os.makedirs("data_raw/auto_downloaded", exist_ok=True)

for link in pdf_links:
    filename = link.split("/")[-1].split("?")[0]
    file_path = os.path.join("data_raw/auto_downloaded", filename)

    pdf_content = requests.get(link).content

    with open(file_path, "wb") as f:
        f.write(pdf_content)

    print(f"Downloaded -> {filename}")

print("Website institutional PDF scraping completed successfully.")
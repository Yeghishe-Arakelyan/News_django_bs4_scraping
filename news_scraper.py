from bs4 import BeautifulSoup
import requests
import json

def clean_text(text):
    cleaned_text = text.replace('\n', '').strip()
    return cleaned_text

def scrape_and_save_to_json(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    div_elements = soup.find_all('div', class_='river-well article')

    scraped_data = []
    url_prefix = 'https://www.computerworld.com/'
    for div_element in div_elements:
        data = {}

        headlines = div_element.find_all('h3')
        data['headlines'] = clean_text(", ".join(headline.get_text() for headline in headlines))

        sub_headlines = div_element.find_all('h4')
        data['sub_headlines'] = clean_text(", ".join(subheadline.get_text() for subheadline in sub_headlines))

        link = div_element.find('a')
        if link:
            data['link'] = url_prefix + link.get("href")
        else:
            data['link'] = "N/A"

        scraped_data.append(data)

    with open(output_file, 'w') as json_file:
        json.dump(scraped_data, json_file, indent=2)

urls_to_scrape = [
    "https://www.computerworld.com/news/",
    "https://www.computerworld.com/category/windows/",
    "https://www.computerworld.com/category/apple/",
]

output_files = [
    "scraped_data_news.json",
    "scraped_data_windows.json",
    "scraped_data_apple.json",
]

for url, output_file in zip(urls_to_scrape, output_files):
    scrape_and_save_to_json(url, output_file)

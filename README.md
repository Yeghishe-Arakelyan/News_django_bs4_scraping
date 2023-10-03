# Scraped News Project

This project is a simple Django web application that displays news articles scraped from various sources. You have the option to update the JSON data files using the `news_scraper.py` script and then run the Django server to view the articles.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Django
- Requests library (for web scraping)
- BeautifulSoup4 (for web scraping)

You can install the required Python packages using pip:

```bash
pip install django requests beautifulsoup4

Update JSON Data (Optional):

If you want to update the JSON data files with fresh news articles, you can run the news_scraper.py script. This script scrapes news articles from specified URLs and saves them to JSON files.
python news_scraper.py
This step is optional if you don't need to update the data.
Start the Development Server:

Start the Django development server to view the news articles:

bash
python manage.py runserver
The server will be running at http://127.0.0.1:8000/.

Accessing the News Pages
Visit the following URLs in your web browser to access the news pages:
News: http://127.0.0.1:8000/
Windows: http://127.0.0.1:8000/windows/
Apple: http://127.0.0.1:8000/apple/
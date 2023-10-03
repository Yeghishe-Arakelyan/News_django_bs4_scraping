import json
from django.core.management.base import BaseCommand
from news.models import News

class Command(BaseCommand):
    help = 'Load news data from JSON files'

    def handle(self, *args, **options):
        for file_name in ['scraped_data_news.json', 'scraped_data_windows.json', 'scraped_data_apple.json']:
            with open(file_name, 'r') as json_file:
                data = json.load(json_file)
                for entry in data:
                    news = News(title=entry['headlines'][0], content=entry['sub_headlines'][0])
                    news.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded news data'))

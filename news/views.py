from django.shortcuts import render
import json

def news_list_view(request):
    
    with open('scraped_data_news.json', 'r') as json_file:
        news_data = json.load(json_file)

    image_url = '/media/mbr.jpg'

    for entry in news_data:
        entry['image_url'] = image_url
    
    return render(request, 'news_list.html', {'news_data': news_data})

def windows_news_list_view(request):
    
    with open('scraped_data_windows.json', 'r') as json_file:
        news_data = json.load(json_file)

    image_url = '/media/win.jpeg'

    for entry in news_data:
        entry['image_url'] = image_url

    return render(request, 'windows_news.html', {'news_data': news_data})


def apple_news_list_view(request):
    
    with open('scraped_data_apple.json', 'r') as json_file:
        news_data = json.load(json_file)
    
    image_url = '/media/apple.jpg'

    for entry in news_data:
        entry['image_url'] = image_url

    return render(request, 'apple_news.html', {'news_data': news_data})


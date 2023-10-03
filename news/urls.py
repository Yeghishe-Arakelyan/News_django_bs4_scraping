from django.urls import path
from . import views
app_name = 'news'

urlpatterns = [
    path('', views.news_list_view, name='news'),
    path('windows/', views.windows_news_list_view, name='windows'),
    path('apple/', views.apple_news_list_view, name='apple'),
   
]
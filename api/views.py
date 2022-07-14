from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests

    news_api = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2022-06-14&sortBy=publishedAt&apiKey=7707892e3b0c4cbb837fac5ea740612e')
    api = json.loads(news_api.content)
    context = {
        'api': api
    }
    return render(request, 'home.html', context)

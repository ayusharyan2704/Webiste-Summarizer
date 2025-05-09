from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from django.shortcuts import render

def get_website_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])
        return content
    except Exception as e:
        return str(e)

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text[:1024], max_length=200, min_length=100, do_sample=False)
    return summary[0]['summary_text']

def index(request):
    return render(request, 'summarize_app/index.html')

def summarize_website(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        original = get_website_content(url)
        summary = summarize_text(original)
        return render(request, 'summarize_app/result.html', {
            'url': url,
            'original': original,
            'summary': summary
        })
    return render(request, 'summarize_app/index.html')

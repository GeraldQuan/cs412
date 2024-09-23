from django.shortcuts import render

# Create your views here.
import random


quotes = [
    "Imagination is more important than knowledge.",
    "Life is like riding a bicycle. To keep your balance, you must keep moving.",
    "Try not to become a man of success, but rather try to become a man of value."
]

images = [
    "/static/images/a.jpg",
    "/static/images/b.jpg",
    "/static/images/c.jpg",

]

def quote(request):
    selected_quote = random.choice(quotes)
    selected_image = random.choice(images)
    return render(request, 'quote.html', {'quote': selected_quote, 'image': selected_image})

def show_all(request):
    return render(request, 'show_all.html', {'quotes': quotes, 'images': images})

def about(request):
    return render(request, 'about.html')

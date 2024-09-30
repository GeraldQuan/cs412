import random
from django.shortcuts import render

def order(request):
    specials = ['Pizza', 'Burger', 'Pasta', 'Salad']
    daily_special = random.choice(specials)
    context = {'daily_special': daily_special}
    return render(request, 'restaurant/order.html', context)

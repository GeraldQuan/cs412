import random
import time
from django.shortcuts import render

def confirmation(request):
    if request.method == 'POST':
        items_ordered = []
        total_price = 0
        menu = {'Pizza': 10, 'Burger': 8, 'Pasta': 12, 'Salad': 7}

        for item, price in menu.items():
            if request.POST.get(item):
                items_ordered.append(item)
                total_price += price

        customer_info = {
            'name': request.POST.get('name'),
            'phone': request.POST.get('phone'),
            'email': request.POST.get('email'),
            'special_instructions': request.POST.get('instructions'),
        }

        ready_time = time.strftime('%I:%M %p', time.localtime(time.time() + random.randint(30, 60) * 60))

        context = {
            'items_ordered': items_ordered,
            'total_price': total_price,
            'customer_info': customer_info,
            'ready_time': ready_time,
        }

        return render(request, 'restaurant/confirmation.html', context)

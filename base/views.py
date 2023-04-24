from django.shortcuts import render
# Create your views here.



rooms = [
    {'id': 1, 'name': "Advaita Vedanta" },
    {'id': 2, 'name': "Vishwadvaita Vedanta" },
    {'id': 3, 'name': "Kriya Yoga" },
]

def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'room.html', {'rooms': rooms})
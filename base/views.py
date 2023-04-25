from django.shortcuts import render
# Create your views here.



rooms = [
    {'id': 1, 'name': "Advaita Vedanta" },
    {'id': 2, 'name': "Vishwadvaita Vedanta" },
    {'id': 3, 'name': "Kriya Yoga" },
]

def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request, pk):
    
    room = None
    
    for i in rooms:
        if i['id'] == int(pk):
            room = i
            
    
    return render(request, 'base/room.html', {'room': room})
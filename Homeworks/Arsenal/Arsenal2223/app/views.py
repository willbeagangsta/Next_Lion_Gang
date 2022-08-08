from django.shortcuts import render,redirect
from .models import Player
# Create your views here.

def home(request):
    
    
    # matches = Match.objects.all()
    goalkeepers = Player.objects.filter(position = 'GK')
    defenders = Player.objects.filter(position = 'DF')
    midfielders = Player.objects.filter(position = 'MF')
    forwards = Player.objects.filter(position = 'FW')

    return render(request, 'home.html', {
        'goalkeepers': goalkeepers, 'defenders': defenders, 'midfielders': midfielders, 
        'forwards': forwards}), #'matches': matches})


def addplayer(request):
    if request.method == 'POST':
        new_player = Player.objects.create(
            name=request.POST['name'],
            backnumber=request.POST['backnumber'],
            position=request.POST['position'],
            age=request.POST['age'],
            nationality=request.POST['nationality'],
            foot=request.POST['foot']
        )
        return redirect('home', new_player.pk)

    return render(request, 'addplayer.html')


# def playerdetail(request, player_pk):

#     player = Player.objects.get(pk=player_pk)

#     return render(request, 'playerdetail.html', {'player': player})

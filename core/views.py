from django.shortcuts import render #,redirect
from core.models import Evento
# Create your views here.

#def index(request): #->urls.py "path('', views.index)"
#    return redirect('/agenda')

def lista_eventos(request):
    usuario = request.user
    #evento = Evento.objects.get(id=1)
    evento = Evento.objects.all() # all() use carefully.
    #evento = Evento.objects.filter(usuario=usuario) # Filtrando view por usuários
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
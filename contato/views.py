from django.shortcuts import render, HttpResponseRedirect
from .forms import FormContato
from .models import Contato


def contato(request):

    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            ins = Contato()
            ins.nome = form.data.get('nome')
            ins.email = form.data.get('email')
            ins.menssagem = form.data.get('menssagem')
            ins.save()
            return HttpResponseRedirect('/')

    else:
        form = FormContato()

    return render(request, 'contato/contato.html', {"form": form})
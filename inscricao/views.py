from django.shortcuts import render
from .forms import FormInscricao
from .models import Inscricao
from django.http import HttpResponseRedirect
from pprint import pprint


def index(request):

    return render(request, "index.html")


def inscricao(request):

    if request.method == 'POST':
        form = FormInscricao(request.POST)
        if form.is_valid():
            ins = Inscricao()
            ins.nome = form.data.get('nome')
            ins.email = form.data.get('email')
            ins.telefone = form.data.get('telefone')
            ins.cpf = form.data.get('cpf')
            ins.dados_institucionais = form.data.get('dados_institucionais')
            ins.numero_tranzacao = form.data.get('cpf')
            ins.save()
            return HttpResponseRedirect('/')

    else:
        form = FormInscricao()

    pprint(form.errors)
    return render(request, "inscricao/inscricao.html", {"form": form})


def confirmacao(request):

    return render(request, "inscricao/confirmacao.html")
from django import forms


class FormContato(forms.Form):

    nome = forms.CharField(label="Nome", max_length=60)
    email = forms.EmailField(label="Email", max_length=60)
    menssagem = forms.CharField(label="Menssagem", max_length=1000)
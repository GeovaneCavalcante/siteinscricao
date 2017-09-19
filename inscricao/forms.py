from django import forms


class FormInscricao(forms.Form):

    nome = forms.CharField(label="Nome", max_length=60)
    email = forms.EmailField(label="Email", max_length=60)
    telefone = forms.CharField(label="Telefone", max_length=60)
    cpf = forms.CharField(label="cpf", max_length=60)
    dados_institucionais = forms.CharField(label="Dados institucionais", max_length=60)
    instituicao = forms.CharField(label="Instituição", max_length=50, min_length=0, required = False)
    curso = forms.CharField(label="Curso", max_length=50, min_length=0, required = False)
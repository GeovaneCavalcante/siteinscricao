from django.db import models


class Inscricao(models.Model):

    nome = models.CharField("Nome", max_length=60)
    email = models.EmailField("Email", max_length=60)
    telefone = models.CharField("Telefone", max_length=50)
    cpf = models.CharField("cpf", unique=True, max_length=50)
    dados_institucionais = models.CharField("Dados institucionais", max_length=60)
    instituicao = models.CharField("Instituição", max_length=50, blank=True)
    curso = models.CharField("Curso", max_length=50, blank=True)
    tipo_inscricao = models.CharField("Tipo da inscricao", max_length=100, blank=True)
    numero_tranzacao = models.CharField("Numero da transação", max_length=100, blank=True, unique=True)
    status_pagamento = models.BooleanField("Pago", default=False)
    created = models.DateTimeField('Criado em:', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):

        return self.nome

    class Meta:
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"

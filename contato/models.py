from django.db import models


class Contato(models.Model):

    nome = models.CharField("Nome", max_length=60)
    email = models.EmailField("Email")
    menssagem = models.TextField("Menssagem")
    created = models.DateTimeField('Criado em:', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

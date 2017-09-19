from django.contrib import admin
from .models import Inscricao


class InscriAdmin(admin.ModelAdmin):

    list_display = ['nome', 'cpf', 'email', 'status_pagamento', "created", "modified"]
    search_fields = ['nome', 'cpf']

admin.site.register(Inscricao, InscriAdmin)

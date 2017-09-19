from django.contrib import admin
from .models import Contato


class ContatoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'email', "created", "modified"]
    search_fields = ['nome', 'email']


admin.site.register(Contato, ContatoAdmin)


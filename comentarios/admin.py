from django.contrib import admin
from .models import Comentarios


class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_comentario', 'email_comentario', 'post_comentario',
                    'usuario_comentario', 'data_comentario', 'publicado_comentario')
    list_display_links = ('id', 'nome_comentario', 'email_comentario',)
    list_editable = ('publicado_comentario',)


admin.site.register(Comentarios, ComentariosAdmin)

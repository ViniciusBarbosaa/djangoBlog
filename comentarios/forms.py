from django.forms import ModelForm
from .models import Comentarios


class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data

        nome = data.get('nome_comentario')

        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais de 5 caracteres'
            )

    class Meta:
        model = Comentarios
        fields = ('nome_comentario', 'email_comentario', 'comentario')


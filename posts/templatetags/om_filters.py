from django import template

register = template.Library()


@register.filter(name='plural_comentarios')
def plural_comentarios(num_comentarios):
    try:
        num_comentarios = int(num_comentarios)

        if num_comentarios == 0:
            return f'Nenhum comentario'
        elif num_comentarios == 1:
            return f'{num_comentarios} comentario'
        else:
            return f'{num_comentarios} comentarios'
    except:
        return f'{num_comentarios} COMENTARIO(s)'

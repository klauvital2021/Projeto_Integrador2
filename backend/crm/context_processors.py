from .models import Usuario


def retorno_familia(request):
    if request.user.is_authenticated:
        user = request.user
        usuario = Usuario.objects.filter(user=user).first()
        if usuario:
            familia = usuario.familia
        else:
            familia = ''
        context = {'familia': familia}
        return context
    return {}

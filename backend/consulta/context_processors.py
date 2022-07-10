from backend.crm.models import Usuario


def retorno_familia(request):
    if request.user.is_authenticated:
        user = request.user
        usuario = Usuario.objects.filter(user=user).first()
        familia = usuario.familia
        context = {'familia': familia}
        return context
    return {}

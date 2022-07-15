from django.contrib.auth.models import Group

from backend.core.services import add_permissions
from backend.crm.models import Responsavel


def responsavel_principal_create(form, user):
    # Define username igual email.
    email = form.cleaned_data.pop('email')
    user.username = email

    user.save()

    # Adiciona ao grupo 'responsavel_principal'.
    group = Group.objects.get(name='responsavel_principal')
    user.groups.add(group)

    # Cria o Responsavel.
    Responsavel.objects.create(user=user)

    # Como é o Responsavel principal,
    # adiciona a permissão can_add_familia.
    add_permissions('responsavel_principal', ['add_familia'])

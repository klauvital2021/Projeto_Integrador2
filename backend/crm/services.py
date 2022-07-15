from django.contrib.auth.models import Group, User

from backend.core.services import add_permissions


def user_create(form):
    first_name = form.cleaned_data.get('first_name')
    last_name = form.cleaned_data.get('last_name')
    email = form.cleaned_data.get('email')
    user = User.objects.create(
        username=email,
        first_name=first_name,
        last_name=last_name,
        email=email,
    )
    return user


def add_to_group_responsavel(form, user):
    # Adiciona o Responsavel no grupo 'responsavel'.
    group = Group.objects.get(name='responsavel')
    user.groups.add(group)

    # Adiciona a permissão view_familia e view_responsavel.
    add_permissions('responsavel', ['view_familia', 'view_responsavel'])


def add_to_group_cuidador(form, user):
    # Adiciona o Cuidador no grupo 'cuidador'.
    group = Group.objects.get(name='cuidador')
    user.groups.add(group)

    # Adiciona a permissão view_familia e view_cuidador.
    add_permissions('cuidador', ['view_familia', 'view_cuidador'])


def add_to_group_dependente(form, user):
    # Adiciona o Dependente no grupo 'dependente'.
    group = Group.objects.get(name='dependente')
    user.groups.add(group)

    # Adiciona a permissão view_familia e view_dependente.
    add_permissions('dependente', ['view_familia', 'view_dependente'])

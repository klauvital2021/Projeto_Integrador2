from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages import constants
from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse_lazy
from backend.core.services import has_group
from backend.crm.models import Responsavel
from .forms import ResponsavelPrincipalForm
from .services import responsavel_principal_create


def responsavel_principal_add(request):
    template_name = 'accounts/responsavel_principal_add.html'
    form = ResponsavelPrincipalForm(request.POST or None)
    success_url = reverse_lazy('home')

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            responsavel_principal_create(form, user)
            messages.add_message(request, constants.SUCCESS,
                                 'Cadastrado com sucesso! Faça seu Login')
            return redirect(success_url)

    context = {'form': form}

    return render(request, template_name, context)


def custom_login(request):
    template_name = 'accounts/login.html'
    #messages.add_message(request, constants.INFO, 'Faça seu login ou cadastre-se no sistema')
    form = AuthenticationForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Autentica
        user_auth = authenticate(username=username, password=password)

        if user_auth:
            # Faz login
            auth_login(request, user_auth)
            # return redirect(resolve_url(settings.LOGIN_REDIRECT_URL))
            user = user_auth

            # Redireciona o Responsável Principal para completar o cadastro dele.
            if has_group(user, 'responsavel_principal'):
                responsavel = Responsavel.objects.get(user=user)


                if responsavel.parentesco_do_responsavel:
                    return redirect(resolve_url(settings.LOGIN_REDIRECT_URL))
                else:
                    messages.add_message(
                        request, constants.WARNING, 'Complete seu cadastrado!')


                return redirect(resolve_url('responsavel_edit', pk=responsavel.pk))
            else:
                return redirect(resolve_url(settings.LOGIN_REDIRECT_URL))

        # Caso não esteja autenticado.
        messages.add_message(request, constants.ERROR,
                             'Usuário ou senha não conferem !')
        return redirect(resolve_url(settings.LOGIN_REDIRECT_URL))

    return render(request, template_name, context)


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_default_redirect_url(self):
        user = self.request.user

        # Redireciona o Responsável Principal para completar o cadastro dele.
        if has_group(user, 'responsavel_principal'):
            responsavel = Responsavel.objects.get(user=user)
            if responsavel.parentesco_do_responsavel:
                return resolve_url(settings.LOGIN_REDIRECT_URL)
            else:
                return resolve_url('responsavel_edit', pk=responsavel.pk)
        else:

            return resolve_url(settings.LOGIN_REDIRECT_URL)

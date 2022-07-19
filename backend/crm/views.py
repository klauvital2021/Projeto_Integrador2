from urllib import request

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.contrib.messages import constants
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import (
    CuidadorAddForm,
    CuidadorUpdateForm,
    DependenteAddForm,
    DependenteUpdateForm,
    FamiliaForm,
    ResponsavelAddForm,
    ResponsavelUpdateForm,

)
from .models import Cuidador, Dependente, Familia, Responsavel
from .services import (
    add_to_group_cuidador,
    add_to_group_dependente,
    add_to_group_responsavel,
    user_create
)


class DependenteListView(LRM, ListView):
    model = Dependente

    def get_queryset(self):
        usuario = self.request.user.usuarios.first()
        familia = usuario.familia
        queryset = Dependente.objects.filter(familia__nome=familia, active=True)  # noqa E501
        return queryset

    def get_context_data(self, **kwargs):
        '''
        Verifica se já existe uma família.
        '''
        context = super().get_context_data(**kwargs)
        usuario = self.request.user.usuarios.first()
        familia = usuario.familia
        if familia:
            context['minha_familia'] = True
        else:
            context['minha_familia'] = False
        return context


class DependenteDetailView(LRM, DetailView):
    model = Dependente


class DependenteCreateView(LRM, CreateView):
    model = Dependente
    form_class = DependenteAddForm

    def form_valid(self, form):
        # Cria o User.
        user = user_create(form)

        self.object = form.save(commit=False)

        # Associa o User ao Dependente
        self.object.user = user

        # Adiciona o Dependente ao grupo 'dependente'.
        add_to_group_dependente(form, user)

        # Associa a Familia.
        usuario = self.request.user.usuarios.first()
        familia = usuario.familia
        self.object.familia = familia
        self.object.save()

        return super().form_valid(form)


class DependenteUpdateView(LRM, UpdateView):
    model = Dependente
    form_class = DependenteUpdateForm


@login_required
def dependente_delete(request, pk):
    obj = get_object_or_404(Dependente, pk=pk)
    obj.active = False
    obj.save()
    return redirect('dependente_list')


class FamiliaListView(LRM, ListView):
    model = Familia

    def get_queryset(self):
        usuario = self.request.user.usuarios.first()
        familia = usuario.familia
        queryset = Familia.objects.filter(nome=familia, active=True)

        return queryset

    def get_context_data(self, **kwargs):
        '''
        Verifica se já existe uma família.
        '''
        context = super().get_context_data(**kwargs)
        usuario = self.request.user.usuarios.first()
        familia = usuario.familia
        if familia:
            context['minha_familia'] = True
        else:
            context['minha_familia'] = False
        return context


class FamiliaDetailView(LRM, DetailView):
    model = Familia


class FamiliaCreateView(LRM, CreateView):
    model = Familia
    form_class = FamiliaForm

    def form_valid(self, form):
        # Pega o objeto Responsavel.
        user = self.request.user
        responsavel = Responsavel.objects.get(user=user)

        # Verifica se já existe uma família.
        usuario = self.request.user.usuarios.first()
        familia = usuario.familia
        if familia:
            return redirect('familia_list')

        self.object = form.save()

        # Associa o Responsavel a Família.
        responsavel.familia = self.object
        responsavel.save()
        return super().form_valid(form)


class FamiliaUpdateView(LRM, UpdateView):
    model = Familia
    form_class = FamiliaForm


@login_required
def familia_delete(request, pk):
    obj = get_object_or_404(Familia, pk=pk)
    obj.active = False
    obj.save()
    return redirect('familia_list')

# crm/views.py


class ResponsavelListView(LRM, ListView):
    model = Responsavel

    def get_queryset(self):
        usuario = self.request.user.usuarios.first()
        if usuario:
            familia = usuario.familia
            queryset = Responsavel.objects.filter(familia__nome=familia, active=True)  # noqa E501
        else:
            queryset = Responsavel.objects.filter(active=True)
        return queryset


class ResponsavelDetailView(LRM, DetailView):
    model = Responsavel


class ResponsavelCreateView(LRM, CreateView):
    model = Responsavel
    form_class = ResponsavelAddForm

    def form_valid(self, form):
        # Cria o User.
        user = user_create(form)

        self.object = form.save(commit=False)

        # Associa o User ao Responsavel
        self.object.user = user

        # Adiciona o Responsavel ao grupo 'responsavel'.
        add_to_group_responsavel(form, user)

        # Associa a Familia.
        usuario = self.request.user.usuarios.first()
        familia = usuario.familia
        self.object.familia = familia
        self.object.save()

        return super().form_valid(form)


class ResponsavelUpdateView(LRM, UpdateView):
    model = Responsavel
    form_class = ResponsavelUpdateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


@login_required
def responsavel_delete(request, pk):
    obj = get_object_or_404(Responsavel, pk=pk)
    obj.active = False
    obj.save()
    return redirect('responsavel_list')


class CuidadorListView(LRM, ListView):
    model = Cuidador

    def get_queryset(self):
        usuario = self.request.user.usuarios.first()
        familia = usuario.familia
        queryset = Cuidador.objects.filter(familia__nome=familia, active=True)  # noqa E501
        return queryset


class CuidadorDetailView(LRM, DetailView):
    model = Cuidador


class CuidadorCreateView(LRM, CreateView):
    model = Cuidador
    form_class = CuidadorAddForm

    def form_valid(self, form):
        # Cria o User.
        user = user_create(form)

        self.object = form.save(commit=False)

        # Associa o User ao Cuidador
        self.object.user = user

        # Adiciona o Cuidador ao grupo 'cuidador'.
        add_to_group_cuidador(form, user)

        # Associa a Familia.
        usuario = self.request.user.usuarios.first()
        familia = usuario.familia
        self.object.familia = familia
        self.object.save()

        return super().form_valid(form)


class CuidadorUpdateView(LRM, UpdateView):
    model = Cuidador
    form_class = CuidadorUpdateForm


@login_required
def cuidador_delete(request, pk):
    obj = get_object_or_404(Cuidador, pk=pk)
    obj.active = False
    obj.save()
    return redirect('cuidador_list')

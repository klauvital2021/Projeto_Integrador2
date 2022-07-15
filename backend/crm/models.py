from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from backend.core.constants import (
    CIVIL_CHOICES,
    PARENTESCO_CHOICES,
    REGIME_CHOICES,
    TURNO_CHOICES
)
from backend.core.models import Active, Address

from .managers import DependenteManager, ResponsavelManager


class Usuario(Address, Active):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='usuário',
        related_name='usuarios',
    )
    familia = models.ForeignKey(
        'Familia',
        on_delete=models.SET_NULL,
        verbose_name='Família',
        related_name='familia_usuarios',
        null=True,
        blank=True
    )
    data_nascimento = models.DateField('Data de Nascimento', blank=True, null=True)  # noqa E501
    rg = models.CharField('RG', max_length=20, blank=True, null=True)  # noqa E501
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)  # noqa E501
    celular_whatsapp = models.CharField('WhatsApp', max_length=20, unique=True, blank=True, null=True)  # noqa E501
    celular_recado = models.CharField('Recado', max_length=20, blank=True, null=True)  # noqa E501
    estado_civil = models.CharField('Estado Civil', max_length=1, choices=CIVIL_CHOICES, blank=True, null=True)  # noqa E501
    nome_conjuge = models.CharField('Cônjuge', max_length=100, blank=True, null=True)  # noqa E501
    nacionalidade = models.CharField('Nacionalidade', max_length=100, blank=True, null=True)  # noqa E501
    parentesco_do_responsavel = models.CharField('Parentesco do Responsável', max_length=1, choices=PARENTESCO_CHOICES, blank=True, null=True)  # noqa E501
    dependente_convenio_medico = models.CharField('Convênio', max_length=100, blank=True, null=True)  # noqa E501
    dependente_contato_fone_convenio = models.CharField('Telefone Convênio', max_length=20, blank=True, null=True)  # noqa E501
    dependente_contato_endereco_convenio = models.CharField('Endereço Convênio', max_length=100, blank=True, null=True)  # noqa E501
    #ativo = models.CharField('Ativo', max_length=10, choices=ATIVO_CHOICES, blank=True, null=True)

    class Meta:
        ordering = ('user__first_name', 'user__last_name')

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name or ""}'.strip()

    def __str__(self):
        return self.full_name


class Familia(Address, Active):
    nome = models.CharField('Nome da Família', max_length=200, unique=True)  # noqa E501

    class Meta:
        verbose_name = 'Família'
        verbose_name_plural = 'Famílias'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('familia_detail', kwargs={'pk': self.pk})


class Responsavel(Usuario):
    objects = ResponsavelManager()

    class Meta:
        proxy = True
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'

    def get_absolute_url(self):
        return reverse('responsavel_detail', kwargs={'pk': self.pk})


class Cuidador(Usuario):
    data_inicio = models.DateField('Admissão', blank=True, null=True)  # noqa E501
    data_fim = models.DateField('Demissão', blank=True, null=True)  # noqa E501
    regime_contratacao = models.CharField('Contratação', max_length=10, choices=REGIME_CHOICES, blank=True, null=True)  # noqa E501
    carga_horaria_semanal = models.IntegerField('Carga Horária Semanal', default=44)  # noqa E501
    turno_trabalho = models.CharField('Turno', max_length=1, choices=TURNO_CHOICES, blank=True, null=True)  # noqa E501
    quem_indicou = models.CharField('Indicação', max_length=100, blank=True, null=True)  # noqa E501
    salario_atual = models.DecimalField('Salário', max_digits=10, decimal_places=2, default=0)  # noqa E501
    adicional = models.DecimalField('Adicional', max_digits=10, decimal_places=2, default=0)  # noqa E501
    dia_pagamento = models.IntegerField('Dia pagamento', blank=True, null=True)  # noqa E501
    observacao = models.TextField('Observação', blank=True, null=True)  # noqa E501

    class Meta:
        verbose_name = 'Cuidador'
        verbose_name_plural = 'Cuidadores'

    def get_absolute_url(self):
        return reverse('cuidador_detail', kwargs={'pk': self.pk})


class Dependente(Usuario):
    objects = DependenteManager()

    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse('dependente_detail', kwargs={'pk': self.pk})

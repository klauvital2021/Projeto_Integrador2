from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class Address(models.Model):
    endereco = models.CharField('Endereço', max_length=200, blank=True, null=True)  # noqa E501
    bairro = models.CharField('Bairro', max_length=200, blank=True, null=True)  # noqa E501
    cidade = models.CharField('Cidade', max_length=200, blank=True, null=True)  # noqa E501
    uf = models.CharField('UF', max_length=2, choices=STATE_CHOICES, blank=True)  # noqa E501

    class Meta:
        abstract = True


class Active(models.Model):
    active = models.BooleanField('ativo', default=True)

    class Meta:
        abstract = True

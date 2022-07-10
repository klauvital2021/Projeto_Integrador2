from django.db import models


class DependenteManager(models.Manager):

    def get_queryset(self):
        return super(DependenteManager, self).get_queryset().filter(user__groups__name='dependente')   # noqa E501


class ResponsavelManager(models.Manager):

    def get_queryset(self):
        groups = ('responsavel_principal', 'responsavel')
        return super(ResponsavelManager, self).get_queryset().filter(user__groups__name__in=groups)   # noqa E501

from django.db import models
from django.urls import reverse

from backend.core.constants import (
    ATENDIMENTO_CHOICES,
    ESPECIALIDADE_CHOICES,
    FORNECEDOR_PRINCIPAL_CHOICES,
    POSOLOGIA_CHOICES,
    TIPO_MEDICAMENTO_CHOICES,
    USO_CONTINUO_CHOICES
)
from backend.crm.models import Dependente, Responsavel


class Consulta(models.Model):
    dependente = models.ForeignKey(
        Dependente,
        on_delete=models.CASCADE,
        related_name='consultas'
    )
    data_consulta = models.DateField('Data Consulta', blank=False, null=False)  # noqa E501
    hora = models.TimeField('Hora', blank=False, null=False)  # noqa E501
    especialidade = models.CharField('Especialidade', max_length=30, choices=ESPECIALIDADE_CHOICES, blank=False, null=False)  # noqa E501
    local = models.CharField('Local', max_length=100, blank=True, null=True)  # noqa E501
    nome_especialista = models.CharField('Especialista', max_length=100, blank=False, null=False)  # noqa E501
    fone_contato = models.CharField('Fone', max_length=100, blank=True, null=True)  # noqa E501
    atendimento = models.CharField('Atendimento', max_length=30, choices=ATENDIMENTO_CHOICES)  # noqa E501
    motivo_consulta = models.CharField('Motivo Consulta', max_length=300, blank=True, null=True)  # noqa E501
    sintomas = models.CharField('Sintomas', max_length=300, blank=True, null=True)  # noqa E501
    observacao = models.CharField('Observação', max_length=300, blank=True, null=True)  # noqa E501
    acompanhante_responsavel = models.ForeignKey(
        Responsavel,
        on_delete=models.CASCADE,
        verbose_name='Acompanhante Responsável'
    )
    cancelamento = models.DateField('Data Cancelamento', blank=True, null=True)  # noqa E501
    motivo_cancelamento = models.CharField('Motivo Cancelamento', max_length=30, choices=ATENDIMENTO_CHOICES, blank=True, null=True)  # noqa E501

    class Meta:
        ordering = ('data_consulta', 'hora')

    def __str__(self):
        return f'{self.pk} - {self.dependente} - {self.data_consulta} - {self.hora} - {self.nome_especialista} - {self.especialidade}'  # noqa E501

    def get_absolute_url(self):
        return reverse("consulta_detail", kwargs={"pk": self.id})


class PosConsulta(models.Model):
    consulta = models.ForeignKey(
        Consulta,
        on_delete=models.CASCADE,
        related_name='pos_consultas'
    )
    acompanhante_responsavel = models.ForeignKey(
        Responsavel,
        on_delete=models.CASCADE,
        verbose_name='Responsável'
    )
    diagnostico = models.TextField('Diagnóstico', blank=False, null=False)  # noqa E501
    tratamento = models.TextField('Tratamento', blank=True, null=True)  # noqa E501
    receita = models.ImageField('Upload Receita', upload_to='', blank=True, null=True)  # noqa E501
    observacao = models.TextField('Observação', blank=True, null=True)  # noqa E501

    def __str__(self):
        return f'{self.pk} - {self.consulta.dependente}'

    def get_upload_to(instance, filename):
        return instance.get_upload_to(filename)

    def get_absolute_url(self):
        return reverse("posconsulta_detail", kwargs={"pk": self.id})


class Medicamento(models.Model):
    medicamento_prescrito = models.CharField('Medicamento Prescrito', max_length=100, blank=False, null=False)  # noqa E501
    principio_ativo = models.CharField('Princípo Ativo', max_length=40, blank=True, null=False)  # noqa E501
    indicacoes = models.TextField('Indicações', blank=True, null=True)  # noqa E501
    tipo_medicamento = models.CharField('Tipo de Medicamento', max_length=18, choices=TIPO_MEDICAMENTO_CHOICES)  # noqa E501
    dosagem = models.CharField('Dosagem', max_length=40, blank=False, null=False)  # noqa E501
    posologia = models.CharField('Posologia', max_length=30, choices=POSOLOGIA_CHOICES)  # noqa E501
    uso_continuo = models.CharField('Uso Continuo', max_length=30, choices=USO_CONTINUO_CHOICES)  # noqa E501
    data_inicio = models.DateField('Dta Inicio', blank=True, null=True)  # noqa E501
    data_fim = models.DateField('Dta Fim', blank=True, null=True)  # noqa E501
    forma_uso = models.TextField('Forma de Uso', blank=False, null=False)  # noqa E501
    orientacao_tratamento = models.TextField('Orientações', blank=False, null=False)  # noqa E501
    medico_responsavel = models.CharField('Médico Responsável', max_length=100, blank=True, null=True)  # noqa E501
    fornecedor_principal = models.CharField('Fornecedor', max_length=20, choices=FORNECEDOR_PRINCIPAL_CHOICES)  # noqa E501
    dependente = models.ForeignKey(
        Dependente,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('dependente', 'medicamento_prescrito')

    def __str__(self):
        #return f'{self.medicamento_prescrito}'
        return f'{self.medicamento_prescrito} - {self.dependente}'

    def get_absolute_url(self):
        return reverse("medicamento_detail", kwargs={"pk": self.id})

from django.contrib import admin

from .models import Consulta, Medicamento, PosConsulta


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'dependente',
        'data_consulta',
        'hora',
        'especialidade',
    )
    # list_display_links = ('dependente',)
    # search_fields = ('name',)
    # list_filter = ('type',)
    # date_hierarchy = 'created'


@admin.register(PosConsulta)
class PosConsultaAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'consulta',
    )
    # list_display_links = ('dependente',)
    # search_fields = ('name',)
    # list_filter = ('type',)
    # date_hierarchy = 'created'


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )
    # list_display_links = ('dependente',)
    search_fields = ('medicamento_prescrito',)
    # list_filter = ('type',)
    # date_hierarchy = 'created'

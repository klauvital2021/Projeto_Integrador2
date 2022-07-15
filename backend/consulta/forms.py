from django import forms

from backend.crm.models import Dependente, Responsavel, Usuario

from .models import Consulta, Medicamento, PosConsulta


class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = '__all__'

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_consulta'].widget.attrs.update({'class': 'mask-date'})   # noqa E501
        self.fields['hora'].widget.attrs.update({'class': 'mask-hora'})

        usuario = Usuario.objects.filter(user=user).first()
        familia = usuario.familia
        queryset = Dependente.objects.filter(familia=familia)
        self.fields['dependente'].queryset = queryset

        queryset_responsavel = Responsavel.objects.filter(familia=familia)
        self.fields['acompanhante_responsavel'].queryset = queryset_responsavel


class PosConsultaForm(forms.ModelForm):

    class Meta:
        model = PosConsulta
        fields = '__all__'

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        usuario = Usuario.objects.filter(user=user).first()
        familia = usuario.familia
        queryset = Responsavel.objects.filter(familia=familia)
        self.fields['acompanhante_responsavel'].queryset = queryset


class MedicamentoForm(forms.ModelForm):

    class Meta:
        model = Medicamento
        fields = '__all__'

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        usuario = Usuario.objects.filter(user=user).first()
        familia = usuario.familia
        queryset = Dependente.objects.filter(familia=familia)
        self.fields['dependente'].queryset = queryset

        self.fields['data_inicio'].widget.attrs.update({'class': 'mask-date'})
        self.fields['data_fim'].widget.attrs.update({'class': 'mask-date'})

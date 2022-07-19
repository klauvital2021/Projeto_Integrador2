from django import forms

from backend.crm.models import Dependente, Responsavel, Usuario

from .models import Consulta, Medicamento, PosConsulta


class DependentesDaFamiliaForm(forms.Form):
    dependente = forms.ModelChoiceField(
        label='Dependente',
        widget=forms.Select(
            attrs={'class': 'form-control'},
        ),
        queryset=Dependente.objects.all()
    )

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        usuario = user.usuarios.first()
        familia = usuario.familia
        queryset = Dependente.objects.filter(familia__nome=familia)
        self.fields['dependente'].queryset = queryset


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

    def __init__(self, request, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # pega o penúltimo item da lista
        # sendo que a lista é ex:
        # '/consulta/posconsulta/add/3/'
        # request.path.split('/')
        # ['', 'consulta', 'posconsulta', 'add', '3', '']
        # ou seja, nesse caso retorna o número 3.
        consulta_pk = request.path.split('/')[-2]
        consulta = Consulta.objects.filter(pk=consulta_pk)
        self.fields['consulta'].queryset = consulta

        acompanhante_responsavel = consulta.first().acompanhante_responsavel
        queryset = Responsavel.objects.filter(pk=acompanhante_responsavel.pk)  # noqa E501
        self.fields['acompanhante_responsavel'].queryset = queryset

        if len(consulta) == 1:
            # Remove os tracinhos.
            self.fields['consulta'].empty_label = None
            self.fields['acompanhante_responsavel'].empty_label = None


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

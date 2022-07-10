from django import forms

from .models import Cuidador, Dependente, Familia, Responsavel


class CustomUserForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nome',
        max_length=150,
    )
    last_name = forms.CharField(
        label='Sobrenome',
        max_length=150,
    )
    email = forms.EmailField(
        label='E-mail',
    )

    class Meta:
        fields = ('first_name', 'last_name', 'email')


class FamiliaForm(forms.ModelForm):

    class Meta:
        model = Familia
        fields = (
            'nome',
            'endereco',
            'bairro',
            'cidade',
            'uf',
        )


class ResponsavelAddForm(CustomUserForm):

    class Meta:
        model = Responsavel
        fields = CustomUserForm.Meta.fields + (
            'data_nascimento',
            'rg',
            'cpf',
            'celular_whatsapp',
            'celular_recado',
            'estado_civil',
            'nome_conjuge',
            'nacionalidade',
            'parentesco_do_responsavel',
            'endereco',
            'bairro',
            'cidade',
            'uf',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-date'})  # noqa E501
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})


class ResponsavelUpdateForm(forms.ModelForm):

    class Meta:
        model = Responsavel
        fields = (
            'data_nascimento',
            'rg',
            'cpf',
            'celular_whatsapp',
            'celular_recado',
            'estado_civil',
            'nome_conjuge',
            'nacionalidade',
            'parentesco_do_responsavel',
            'endereco',
            'bairro',
            'cidade',
            'uf',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-date'})  # noqa E501
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})


class CuidadorAddForm(CustomUserForm):

    class Meta:
        model = Cuidador
        fields = CustomUserForm.Meta.fields + (
            'data_nascimento',
            'rg',
            'cpf',
            'celular_whatsapp',
            'celular_recado',
            'estado_civil',
            'nome_conjuge',
            'nacionalidade',
            'endereco',
            'bairro',
            'cidade',
            'uf',
            'data_inicio',
            'data_fim',
            'regime_contratacao',
            'carga_horaria_semanal',
            'turno_trabalho',
            'quem_indicou',
            'salario_atual',
            'adicional',
            'dia_pagamento',
            'observacao',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-date'})  # noqa E501
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['data_inicio'].widget.attrs.update({'class': 'mask-date'})
        self.fields['data_fim'].widget.attrs.update({'class': 'mask-date'})


class CuidadorUpdateForm(forms.ModelForm):

    class Meta:
        model = Cuidador
        fields = (
            'data_nascimento',
            'rg',
            'cpf',
            'celular_whatsapp',
            'celular_recado',
            'estado_civil',
            'nome_conjuge',
            'nacionalidade',
            'endereco',
            'bairro',
            'cidade',
            'uf',
            'data_inicio',
            'data_fim',
            'regime_contratacao',
            'carga_horaria_semanal',
            'turno_trabalho',
            'quem_indicou',
            'salario_atual',
            'adicional',
            'dia_pagamento',
            'observacao',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-date'})  # noqa E501
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['data_inicio'].widget.attrs.update({'class': 'mask-date'})
        self.fields['data_fim'].widget.attrs.update({'class': 'mask-date'})


class DependenteAddForm(CustomUserForm):

    class Meta:
        model = Dependente
        fields = CustomUserForm.Meta.fields + (
            'data_nascimento',
            'rg',
            'cpf',
            'celular_whatsapp',
            'celular_recado',
            'estado_civil',
            'nome_conjuge',
            'nacionalidade',
            'endereco',
            'bairro',
            'cidade',
            'uf',
            'dependente_convenio_medico',
            'dependente_contato_fone_convenio',
            'dependente_contato_endereco_convenio',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-date'})  # noqa E501
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})


class DependenteUpdateForm(forms.ModelForm):

    class Meta:
        model = Dependente
        fields = (
            'data_nascimento',
            'rg',
            'cpf',
            'celular_whatsapp',
            'celular_recado',
            'estado_civil',
            'nome_conjuge',
            'nacionalidade',
            'endereco',
            'bairro',
            'cidade',
            'uf',
            'dependente_convenio_medico',
            'dependente_contato_fone_convenio',
            'dependente_contato_endereco_convenio',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-date'})  # noqa E501
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})

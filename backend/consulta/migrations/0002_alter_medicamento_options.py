# Generated by Django 4.0.5 on 2022-07-19 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicamento',
            options={'ordering': ('dependente', 'medicamento_prescrito')},
        ),
    ]

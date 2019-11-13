# Generated by Django 2.2.7 on 2019-11-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soldado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome completo')),
                ('cpf', models.IntegerField(max_length=11, verbose_name='CPF')),
                ('categoria', models.CharField(max_length=20, verbose_name='Categoria')),
            ],
        ),
    ]

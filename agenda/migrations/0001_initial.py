# Generated by Django 2.2.4 on 2020-03-15 12:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agendamentosModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estadoPagamento', models.CharField(choices=[('1', 'Pago'), ('2', 'Não Pago')], default=1, max_length=1)),
                ('apartamento', models.CharField(blank=True, max_length=200, null=True)),
                ('locatario', models.CharField(blank=True, max_length=200, null=True)),
                ('quantidadePessoas', models.CharField(blank=True, max_length=200, null=True)),
                ('dataEntrada', models.DateTimeField(default=django.utils.timezone.now)),
                ('dataSaida', models.DateTimeField(default=django.utils.timezone.now)),
                ('valorTotal', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('dataCadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='apartamentoModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rua', models.CharField(blank=True, max_length=1000, null=True)),
                ('numero', models.CharField(blank=True, max_length=10, null=True)),
                ('bairro', models.CharField(blank=True, max_length=1000, null=True)),
                ('cidade', models.CharField(blank=True, max_length=1000, null=True)),
                ('estado', models.CharField(blank=True, max_length=1000, null=True)),
                ('valorDiaria', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('dataCadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='locadorModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=200, null=True)),
                ('sobrenome', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('telefone', models.CharField(blank=True, max_length=14, null=True)),
                ('dataCadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='locatarioModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=200, null=True)),
                ('sobrenome', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('telefone', models.CharField(blank=True, max_length=14, null=True)),
                ('dataCadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
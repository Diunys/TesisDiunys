# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=500)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Instrumento',
                'verbose_name_plural': 'Instrumentos',
            },
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Opcion',
                'verbose_name_plural': 'Opciones',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('numero', models.IntegerField()),
                ('estado', models.BooleanField(default=True, help_text='Indica si esta habilitada')),
            ],
            options={
                'verbose_name': 'Pregunta',
                'verbose_name_plural': 'Preguntas',
            },
        ),
        migrations.CreateModel(
            name='Cerrada',
            fields=[
                ('pregunta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='encuesta.Pregunta')),
                ('multiple', models.BooleanField(default=False)),
                ('otro', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Pregunta Cerrada',
                'verbose_name_plural': 'Preguntas Cerradas',
            },
            bases=('encuesta.pregunta',),
        ),
        migrations.AddField(
            model_name='opcion',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuesta.Cerrada'),
        ),
        migrations.AddField(
            model_name='instrumento',
            name='preguntas',
            field=models.ManyToManyField(to='encuesta.Cerrada'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-04-26 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=128, verbose_name='titulo')),
                ('conteudo', models.TextField()),
                ('data_criacao', models.DateTimeField(blank=True, null=True)),
                ('data_publicacao', models.DateTimeField(blank=True, null=True)),
                ('publicado', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Notícia',
                'verbose_name_plural': 'Notícias',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('data_de_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('telefone_celular', models.CharField(blank=True, help_text='Número do telefone celular no formato (99) 99999-9999', max_length=15, null=True, verbose_name='Telefone celular')),
                ('telefone_fixo', models.CharField(blank=True, help_text='Número do telefone fixo no formato (99) 9999-9999', max_length=14, null=True, verbose_name='Telefone fixo')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_noticias.Pessoa'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='tags',
            field=models.ManyToManyField(to='app_noticias.Tag'),
        ),
    ]

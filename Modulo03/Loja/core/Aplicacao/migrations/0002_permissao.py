# Generated by Django 4.0.5 on 2022-07-08 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.IntegerField()),
                ('id_menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Aplicacao.menu')),
            ],
            options={
                'db_table': 'Permissoes',
            },
        ),
    ]

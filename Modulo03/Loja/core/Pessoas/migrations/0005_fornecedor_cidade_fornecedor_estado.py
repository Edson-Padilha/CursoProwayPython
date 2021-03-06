# Generated by Django 4.0.4 on 2022-05-24 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Local', '0001_initial'),
        ('Pessoas', '0004_cliente_cidade_cliente_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='cidade',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='Local.cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='estado',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='Local.estado'),
            preserve_default=False,
        ),
    ]

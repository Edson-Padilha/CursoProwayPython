# Generated by Django 4.0.4 on 2022-05-20 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Local', '0001_initial'),
        ('Pessoas', '0003_alter_cliente_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cidade',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='Local.cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='Local.estado'),
            preserve_default=False,
        ),
    ]

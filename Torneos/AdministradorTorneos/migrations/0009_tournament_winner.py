# Generated by Django 2.2 on 2020-11-13 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdministradorTorneos', '0008_auto_20201112_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='winner',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tournament_winner', to='AdministradorTorneos.Player'),
        ),
    ]

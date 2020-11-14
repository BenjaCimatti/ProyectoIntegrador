# Generated by Django 2.2 on 2020-11-13 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministradorTorneos', '0009_tournament_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
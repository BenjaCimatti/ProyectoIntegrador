# Generated by Django 2.2 on 2020-11-12 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministradorTorneos', '0007_auto_20201103_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalmatch',
            name='won',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quartermatch',
            name='won',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='semimatch',
            name='won',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.2 on 2020-11-15 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministradorTorneos', '0011_auto_20201113_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='semimatch',
            name='QmFinished',
            field=models.BooleanField(default=False),
        ),
    ]

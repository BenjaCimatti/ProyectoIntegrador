# Generated by Django 2.2 on 2020-11-03 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdministradorTorneos', '0005_auto_20201103_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalmatch',
            name='player1',
            field=models.ForeignKey(blank=True, default='TBD', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='finalmatch_player1', to='AdministradorTorneos.Player'),
        ),
        migrations.AlterField(
            model_name='finalmatch',
            name='player2',
            field=models.ForeignKey(blank=True, default='TBD', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='finalmatch_player2', to='AdministradorTorneos.Player'),
        ),
        migrations.AlterField(
            model_name='quartermatch',
            name='player1',
            field=models.ForeignKey(blank=True, default='TBD', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quartermatch_player1', to='AdministradorTorneos.Player'),
        ),
        migrations.AlterField(
            model_name='quartermatch',
            name='player2',
            field=models.ForeignKey(blank=True, default='TBD', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quartermatch_player2', to='AdministradorTorneos.Player'),
        ),
        migrations.AlterField(
            model_name='semimatch',
            name='player1',
            field=models.ForeignKey(blank=True, default='TBD', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semimatch_player1', to='AdministradorTorneos.Player'),
        ),
        migrations.AlterField(
            model_name='semimatch',
            name='player2',
            field=models.ForeignKey(blank=True, default='TBD', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semimatch_player2', to='AdministradorTorneos.Player'),
        ),
    ]

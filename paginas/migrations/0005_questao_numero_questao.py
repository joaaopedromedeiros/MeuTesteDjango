# Generated by Django 5.1.7 on 2025-03-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0004_questao_simulado_resposta_questao_simulado'),
    ]

    operations = [
        migrations.AddField(
            model_name='questao',
            name='numero_questao',
            field=models.CharField(default=1, max_length=2),
        ),
    ]

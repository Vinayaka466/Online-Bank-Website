# Generated by Django 5.1.3 on 2024-12-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebankingapp', '0005_show_account_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]

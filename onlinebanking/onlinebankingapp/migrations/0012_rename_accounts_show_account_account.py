# Generated by Django 5.1.3 on 2024-12-03 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebankingapp', '0011_remove_show_account_account_show_account_accounts_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show_account',
            old_name='accounts',
            new_name='account',
        ),
    ]

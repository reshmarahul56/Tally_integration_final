# Generated by Django 4.0.4 on 2022-09-30 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0049_alter_currency_alt_buyvorate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_itemcreation',
            name='company',
        ),
        migrations.RemoveField(
            model_name='stock_itemcreation',
            name='godown',
        ),
    ]

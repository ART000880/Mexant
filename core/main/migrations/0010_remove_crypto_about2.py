# Generated by Django 4.0.5 on 2022-07-04 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_crypto_name1_remove_crypto_name2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crypto',
            name='about2',
        ),
    ]

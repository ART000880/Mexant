# Generated by Django 4.0.5 on 2022-07-05 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_crypto_about2_crypto_image1_crypto_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='crypto',
            name='char',
            field=models.TextField(default=1, verbose_name='crypto char'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crypto',
            name='char1',
            field=models.TextField(default=1, verbose_name='crypto char1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crypto',
            name='char2',
            field=models.TextField(default=1, verbose_name='crypto char2'),
            preserve_default=False,
        ),
    ]

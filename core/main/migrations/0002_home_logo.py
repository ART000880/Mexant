# Generated by Django 4.0.5 on 2022-07-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='logo',
            field=models.ImageField(default=1, upload_to='media', verbose_name='logo img'),
            preserve_default=False,
        ),
    ]
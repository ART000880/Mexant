# Generated by Django 4.0.5 on 2022-07-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_about_about1_about_about2_about_name1_about_name2'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default=1, upload_to='media', verbose_name='about img'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.5 on 2022-07-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_about_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about1',
            field=models.TextField(default=1, verbose_name='about1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='about2',
            field=models.TextField(default=1, verbose_name='about2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='name1',
            field=models.CharField(default=1, max_length=200, verbose_name='about name1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='name2',
            field=models.CharField(default=1, max_length=200, verbose_name='about name2'),
            preserve_default=False,
        ),
    ]
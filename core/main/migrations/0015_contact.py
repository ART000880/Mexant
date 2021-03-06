# Generated by Django 4.0.5 on 2022-07-04 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='service1 name')),
                ('about', models.TextField(verbose_name='service1 about')),
                ('image', models.ImageField(upload_to='media', verbose_name='service1 img')),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-05-07 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_vaccinecentre_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccinecentre',
            name='image',
        ),
    ]

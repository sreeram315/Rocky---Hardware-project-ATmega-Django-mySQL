# Generated by Django 2.2.7 on 2020-04-03 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_wallettransactions_ttype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallettransactions',
            name='credit',
        ),
    ]

# Generated by Django 2.2.7 on 2020-06-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_deviceinfo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceinfo',
            name='is_admin_url',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 2.2.7 on 2020-06-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_deviceinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceinfo',
            name='url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
# Generated by Django 2.2.7 on 2020-04-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tollgate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tollgates',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]

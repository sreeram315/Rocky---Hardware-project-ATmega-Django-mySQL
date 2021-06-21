# Generated by Django 2.2.7 on 2020-06-07 06:17

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('video', embed_video.fields.EmbedVideoField(help_text='This is a help text', verbose_name='My video')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]

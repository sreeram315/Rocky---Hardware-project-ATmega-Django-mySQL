# Generated by Django 2.2.7 on 2020-04-02 13:11

from django.db import migrations, models
import django.db.models.deletion
import tollgate.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0004_auto_20200402_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tollgates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(blank=True, max_length=127, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, help_text='Tollgate Latitude', max_digits=9, verbose_name='Latitude')),
                ('longitude', models.DecimalField(decimal_places=6, help_text='Tollgate Longitude', max_digits=9, verbose_name='Longitude')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Tollgate',
                'verbose_name_plural': 'Tollgates',
                'db_table': 'tbl_tollgates',
            },
        ),
        migrations.CreateModel(
            name='TollgateLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttype', models.PositiveIntegerField(blank=True, choices=[(0, 'Entry'), (1, 'Exit')], null=True)),
                ('date', models.DateField(default=tollgate.models.curr_date)),
                ('time', models.TimeField(default=tollgate.models.curr_time)),
                ('min_charge', models.PositiveIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('tollgate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log', to='tollgate.Tollgates')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log', to='vehicles.Vehicles')),
            ],
            options={
                'verbose_name': 'TollgateLog',
                'verbose_name_plural': 'TollgateLogs',
                'db_table': 'tbl_tollgatelog',
            },
        ),
    ]

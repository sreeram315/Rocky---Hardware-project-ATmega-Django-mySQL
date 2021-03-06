# Generated by Django 2.2.7 on 2020-04-03 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_auto_20200403_0824'),
        ('tollgate', '0003_auto_20200402_1859'),
        ('accounts', '0011_auto_20200403_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='TollBillings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('tollgate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='tollgate.Tollgates')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='vehicles.Vehicles')),
            ],
            options={
                'verbose_name': 'Toll Billing',
                'verbose_name_plural': 'Toll Billings',
                'db_table': 'tbl_toll_billing',
            },
        ),
    ]

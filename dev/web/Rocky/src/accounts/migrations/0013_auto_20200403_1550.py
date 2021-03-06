# Generated by Django 2.2.7 on 2020-04-03 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_tollbillings'),
    ]

    operations = [
        migrations.AddField(
            model_name='tollbillings',
            name='transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toll_bill', to='accounts.WalletTransactions'),
        ),
        migrations.AlterField(
            model_name='tollbillings',
            name='tollgate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toll_bill', to='tollgate.Tollgates'),
        ),
        migrations.AlterField(
            model_name='tollbillings',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toll_bill', to='vehicles.Vehicles'),
        ),
    ]

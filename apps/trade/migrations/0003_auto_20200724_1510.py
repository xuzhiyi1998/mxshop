# Generated by Django 3.0.7 on 2020-07-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20200618_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='order_sn',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='订单编号'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='trade_no',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='交易编号'),
        ),
    ]
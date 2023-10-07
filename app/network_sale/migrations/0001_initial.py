# Generated by Django 4.2.6 on 2023-10-06 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Product title')),
                ('model', models.CharField(max_length=100, verbose_name='Product model')),
                ('date', models.DateField(verbose_name='Date of going on sale')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='TradingNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title of Trading network')),
            ],
            options={
                'verbose_name': 'Trading Network',
                'verbose_name_plural': 'Trading Networks',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0, verbose_name='level of unit in hierarchy')),
                ('type', models.CharField(choices=[('Factory', 'Factory'), ('Retail', 'Retail'), ('Individual', 'Individual')], verbose_name='type of unit')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='unit title')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='unit mail')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='country')),
                ('town', models.CharField(max_length=100, verbose_name='town title')),
                ('street', models.CharField(max_length=100, verbose_name='street title')),
                ('structure_number', models.CharField(max_length=100, verbose_name='number of structure for unit')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('arrears', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True, verbose_name='arrears')),
                ('products', models.ManyToManyField(to='network_sale.product')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='network_sale.unit', verbose_name='provider for unit')),
                ('trading_network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_sale.tradingnetwork', verbose_name='unit works in trading Network')),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
            },
        ),
    ]
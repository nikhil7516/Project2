# Generated by Django 4.2.4 on 2023-11-21 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Place', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tbl_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.IntegerField()),
                ('Product_name', models.CharField(max_length=100)),
                ('Quantity', models.IntegerField()),
                ('Amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tbl_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('Amount', models.IntegerField()),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=100)),
                ('Quantity', models.IntegerField()),
                ('Price', models.IntegerField()),
            ],
        ),
    ]

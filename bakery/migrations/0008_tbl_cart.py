# Generated by Django 5.0 on 2024-01-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0007_remove_tbl_payment_address_tbl_payment_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_id', models.CharField(max_length=500)),
                ('item_id', models.CharField(max_length=500)),
                ('item_name', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('status', models.CharField(max_length=500)),
            ],
        ),
    ]

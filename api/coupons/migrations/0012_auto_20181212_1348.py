# Generated by Django 2.1.2 on 2018-12-12 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0011_auto_20181209_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='qr',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 12, 13, 48, 52, 252028)),
        ),
    ]
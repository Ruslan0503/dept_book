# Generated by Django 4.2.5 on 2023-09-15 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0011_customer_deptor_customer_returned_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-12 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0003_alter_customer_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='OrderItem',
        ),
    ]

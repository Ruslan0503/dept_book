# Generated by Django 4.2.5 on 2023-09-12 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0006_remove_orderitem_date_remove_orderitem_last_update_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-id']},
        ),
    ]

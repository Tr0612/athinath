# Generated by Django 3.1.4 on 2020-12-26 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_remove_order_order_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]

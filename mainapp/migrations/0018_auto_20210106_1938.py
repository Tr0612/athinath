# Generated by Django 3.1.4 on 2021-01-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(blank=True, max_length=800, null=True, unique=True),
        ),
    ]

# Generated by Django 3.1.4 on 2021-01-10 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_personalized_tresures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecategories',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category'),
        ),
    ]

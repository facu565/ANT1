# Generated by Django 3.2.1 on 2021-05-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce', '0003_auto_20210526_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('S', 'vehicles'), ('VF', 'Estate'), ('SC', 'Technology'), ('SC', 'Tools'), ('SC', 'Home Appliances'), ('SC', 'Construction'), ('SC', 'Sports'), ('SC', 'Toys'), ('SC', 'Fashion'), ('SC', 'Services')], default='Service', max_length=2),
        ),
    ]

# Generated by Django 4.0 on 2022-02-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_cartaddproduct_productcartadd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcartadd',
            name='quantity',
            field=models.CharField(default=1, max_length=10, verbose_name='Кол-во'),
        ),
    ]
# Generated by Django 4.0 on 2022-02-01 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_cartitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItem',
            new_name='CartAddProduct',
        ),
    ]

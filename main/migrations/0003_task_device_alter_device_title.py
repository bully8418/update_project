# Generated by Django 4.0 on 2022-01-11 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.device'),
        ),
        migrations.AlterField(
            model_name='device',
            name='title',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Устройства'),
        ),
    ]

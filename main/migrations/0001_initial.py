# Generated by Django 4.0 on 2022-01-08 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_foto', models.ImageField(blank=True, upload_to='D:\\Проекты\\Food_city\\media')),
                ('title', models.CharField(max_length=100, verbose_name='Название товара')),
                ('description', models.TextField(max_length=250, verbose_name='Описание товара')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.category')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]

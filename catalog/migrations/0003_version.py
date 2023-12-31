# Generated by Django 4.2.2 on 2023-06-08 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_preview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_version', models.CharField(max_length=150, verbose_name='номер версии')),
                ('title_of_version', models.CharField(max_length=150, verbose_name='имя версии')),
                ('actual_version', models.BooleanField(default=True, verbose_name='актуальность версии')),
                ('name_of_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='наименование')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]

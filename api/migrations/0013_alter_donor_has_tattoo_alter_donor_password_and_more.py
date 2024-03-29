# Generated by Django 5.0.1 on 2024-01-14 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_districts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='has_tattoo',
            field=models.CharField(choices=[('', 'any tattoo'), ('yes', 'Yes'), ('no', 'No')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='donor',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='phone_no',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.districts'),
        ),
        migrations.AlterField(
            model_name='want',
            name='phone_no',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]

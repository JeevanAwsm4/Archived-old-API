# Generated by Django 5.0.1 on 2024-01-12 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_donor_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='phone_no',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]

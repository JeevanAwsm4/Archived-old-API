# Generated by Django 5.0.1 on 2024-01-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_donor_district_alter_want_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='want',
            name='phone_no',
            field=models.CharField(max_length=15),
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-28 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_remove_donor_aadhaar_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='want',
            name='type',
            field=models.CharField(choices=[('blood', 'blood'), ('platelets', 'platelets')], max_length=15, null=True),
        ),
    ]
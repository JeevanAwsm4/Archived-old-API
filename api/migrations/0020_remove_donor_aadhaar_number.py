# Generated by Django 5.0.1 on 2024-01-25 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_want_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='aadhaar_number',
        ),
    ]

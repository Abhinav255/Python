# Generated by Django 4.2.6 on 2023-11-09 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='status',
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-09 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_remove_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='profile_pic/'),
        ),
    ]
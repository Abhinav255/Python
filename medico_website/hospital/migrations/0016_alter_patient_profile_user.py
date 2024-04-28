# Generated by Django 4.2.6 on 2023-11-20 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0015_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.user'),
        ),
    ]
# Generated by Django 4.1.3 on 2023-09-02 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kktechapp', '0014_alter_attendance_evening_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='evening_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='morning_time',
            field=models.TimeField(null=True),
        ),
    ]
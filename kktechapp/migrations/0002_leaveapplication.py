# Generated by Django 4.1.3 on 2023-08-31 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kktechapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=50)),
                ('reason', models.CharField(max_length=100)),
                ('approval', models.BooleanField(default=False)),
            ],
        ),
    ]

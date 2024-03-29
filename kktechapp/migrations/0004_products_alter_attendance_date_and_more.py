# Generated by Django 4.1.3 on 2023-09-01 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kktechapp', '0003_leaveapplication_usr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(null=True, upload_to='product_image')),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('investment', models.FloatField(null=True)),
                ('transportation_cost', models.FloatField(null=True)),
                ('parcel_cost', models.FloatField(null=True)),
                ('profit', models.FloatField(null=True)),
                ('total_cost', models.FloatField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='approval',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='empname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='rawmaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waight', models.CharField(max_length=50, null=True)),
                ('numbers', models.IntegerField(null=True)),
                ('rate', models.FloatField(null=True)),
                ('usr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=150, null=True)),
                ('customer', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('profit', models.FloatField(null=True)),
                ('cotation', models.FloatField(null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kktechapp.products')),
                ('raw_material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kktechapp.rawmaterials')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectGroth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250, null=True)),
                ('date', models.DateField(null=True)),
                ('usr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='raw_material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kktechapp.rawmaterials'),
        ),
        migrations.AddField(
            model_name='products',
            name='usr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PersonWorkingOnProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kktechapp.projectmanagement')),
                ('usr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

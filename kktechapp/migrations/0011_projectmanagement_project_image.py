# Generated by Django 4.1.3 on 2023-09-01 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kktechapp', '0010_rawmaterials_rawmaterial_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmanagement',
            name='project_image',
            field=models.ImageField(null=True, upload_to='project_image'),
        ),
    ]
# Generated by Django 4.2.7 on 2023-11-11 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogposttable',
            name='adds',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='adds/'),
        ),
    ]

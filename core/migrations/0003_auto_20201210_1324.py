# Generated by Django 3.1.4 on 2020-12-10 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='bigDescription',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='video',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]

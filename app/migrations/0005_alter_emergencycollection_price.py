# Generated by Django 5.0.6 on 2024-06-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_emergencycollection_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycollection',
            name='price',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

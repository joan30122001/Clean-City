# Generated by Django 5.0.6 on 2024-06-23 09:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_emergencycollection_paid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('location', models.CharField(choices=[('Yaounde', 'Yaounde'), ('Douala', 'Douala')], max_length=255)),
                ('profile_image', models.ImageField(blank=True, default='users/default-avatar.png', null=True, upload_to='users/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

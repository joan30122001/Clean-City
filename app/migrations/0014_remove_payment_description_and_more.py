# Generated by Django 5.0.6 on 2024-06-24 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_illegaldeposit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='description',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='emergency_collect',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='transaction_code',
        ),
        migrations.AddField(
            model_name='payment',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('MonetBill', 'MonetBill'), ('Orange Money', 'Orange Money'), ('MTN Mobile Money', 'MTN Mobile Money')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]
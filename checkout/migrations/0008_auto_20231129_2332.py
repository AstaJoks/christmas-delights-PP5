# Generated by Django 3.2.22 on 2023-11-29 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20231129_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='carbon_fp_total',
        ),
        migrations.RemoveField(
            model_name='order',
            name='carbon_saved_total',
        ),
    ]
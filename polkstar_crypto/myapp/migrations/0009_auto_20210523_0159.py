# Generated by Django 3.2.3 on 2021-05-22 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_pool_pool_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='pool',
            name='pool_max_amount',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pool',
            name='pool_min_amount',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
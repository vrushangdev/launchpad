# Generated by Django 3.2.3 on 2021-05-24 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20210523_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pool',
            name='pool_coin_image',
        ),
        migrations.AlterField(
            model_name='pool',
            name='pool_tier',
            field=models.CharField(choices=[('Tier 1', 'Tier 1'), ('Tier 2', 'Tier 2'), ('Tier 3', 'Tier 3'), ('Bonus Tier', 'Bonus Tier')], default='Tier 1', max_length=100),
        ),
    ]

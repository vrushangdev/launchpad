# Generated by Django 3.2.3 on 2021-05-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='pool_access',
            field=models.CharField(choices=[('Featured', 'Featured'), ('Upcoming', 'Upcoming')], default='Upcoming', max_length=100),
        ),
    ]

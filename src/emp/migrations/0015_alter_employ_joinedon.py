# Generated by Django 3.2.4 on 2021-06-15 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0014_auto_20210614_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employ',
            name='joinedOn',
            field=models.DateField(default=datetime.date.today, verbose_name='Joined On'),
        ),
    ]

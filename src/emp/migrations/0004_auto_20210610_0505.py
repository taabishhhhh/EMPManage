# Generated by Django 3.2.4 on 2021-06-10 05:05

from django.db import migrations, models
import emp.models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_auto_20210609_0505'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employ',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterField(
            model_name='employ',
            name='empid',
            field=models.IntegerField(validators=[emp.models.validate_empid]),
        ),
    ]

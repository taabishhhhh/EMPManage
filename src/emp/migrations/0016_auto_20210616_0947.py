# Generated by Django 3.2.4 on 2021-06-16 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0015_alter_employ_joinedon'),
    ]

    operations = [
        migrations.AddField(
            model_name='employ',
            name='is_archived',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='employ',
            name='employID',
            field=models.IntegerField(max_length=4, unique=True, verbose_name='Employ ID'),
        ),
    ]

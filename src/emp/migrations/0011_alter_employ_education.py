# Generated by Django 3.2.4 on 2021-06-14 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0010_auto_20210612_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employ',
            name='education',
            field=models.CharField(max_length=50, verbose_name='Highest Education'),
        ),
    ]
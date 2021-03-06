# Generated by Django 3.2.4 on 2021-06-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0009_auto_20210612_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employ',
            name='EmployID',
        ),
        migrations.RemoveField(
            model_name='employ',
            name='githubUsername',
        ),
        migrations.RemoveField(
            model_name='employ',
            name='highestEducation',
        ),
        migrations.RemoveField(
            model_name='employ',
            name='professionalEmail',
        ),
        migrations.AddField(
            model_name='employ',
            name='education',
            field=models.TextField(default='', verbose_name='Highest Education'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employ',
            name='employID',
            field=models.IntegerField(default=0, verbose_name='Employ ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employ',
            name='fladdraEmail',
            field=models.EmailField(default=True, max_length=254, verbose_name='Fladdra Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employ',
            name='github',
            field=models.CharField(default='', max_length=50, verbose_name='Github'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employ',
            name='address',
            field=models.TextField(verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='fname',
            field=models.CharField(max_length=20, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='lname',
            field=models.CharField(max_length=20, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='mobile',
            field=models.IntegerField(default=None, verbose_name='Mobile No'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='personalEmail',
            field=models.EmailField(max_length=254, verbose_name='Personal Email'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='position',
            field=models.CharField(choices=[('Intern', 'Intern'), ('Senior Developer', 'Senior Developer'), ('Junior Developer', 'Junior Developer'), ('HR', 'HR'), ('-', '-'), ('Test', 'Test')], max_length=16, verbose_name='Position'),
        ),
    ]

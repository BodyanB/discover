# Generated by Django 2.2.4 on 2019-08-11 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20190811_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profi',
            name='courses',
            field=models.ManyToManyField(to='mysite.Course'),
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-11 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='This is name', max_length=255, unique=True, verbose_name='Instructor name')),
                ('surname', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
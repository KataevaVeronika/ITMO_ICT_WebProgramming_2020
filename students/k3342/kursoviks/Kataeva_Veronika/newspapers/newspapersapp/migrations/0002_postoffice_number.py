# Generated by Django 3.0.4 on 2020-05-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspapersapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postoffice',
            name='number',
            field=models.IntegerField(default=22),
        ),
    ]
# Generated by Django 3.0.4 on 2020-04-17 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=7)),
                ('car_description', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Car',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=20)),
                ('team_country', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Team',
            },
        ),
        migrations.CreateModel(
            name='Racer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('experience', models.IntegerField()),
                ('grade_of_license', models.CharField(choices=[('A', 'Grade A'), ('B', 'Grade B'), ('C', 'Grade C'), ('IA', 'International Grade A'), ('IB', 'International Grade B'), ('IC', 'International Grade C')], max_length=2)),
                ('description', models.CharField(max_length=50)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='board.Car')),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Team')),
            ],
            options={
                'db_table': 'Racer',
            },
        ),
    ]

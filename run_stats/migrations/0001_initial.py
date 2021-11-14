# Generated by Django 3.2.2 on 2021-11-14 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('time', models.TimeField()),
                ('distance', models.DecimalField(decimal_places=2, max_digits=3)),
                ('average_speed', models.DecimalField(decimal_places=1, max_digits=3)),
                ('steps', models.IntegerField()),
                ('calories_burned', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Split',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('time', models.TimeField()),
                ('full_mile', models.BooleanField()),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='run_stats.run')),
            ],
        ),
    ]

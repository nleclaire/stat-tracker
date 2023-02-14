# Generated by Django 4.0.2 on 2023-02-07 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('run_stats', '0004_run_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='split',
            name='date',
        ),
        migrations.AddField(
            model_name='split',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='split',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

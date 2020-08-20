# Generated by Django 2.2.10 on 2020-08-09 20:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0004_municipality'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='confirmed_date',
            field=models.DateField(default=datetime.date.today, verbose_name='date added'),
        ),
        migrations.AddField(
            model_name='event',
            name='muni',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='idp_data.Municipality'),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_desc',
            field=models.CharField(max_length=200),
        ),
    ]
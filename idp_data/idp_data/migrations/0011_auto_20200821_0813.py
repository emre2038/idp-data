# Generated by Django 2.2.10 on 2020-08-21 08:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0010_hostnamemunicipality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventaction',
            old_name='title',
            new_name='internal_label',
        ),
        migrations.AlterField(
            model_name='event',
            name='confirmed_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Confirmed date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='muni',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='idp_data.Municipality'),
        ),
    ]

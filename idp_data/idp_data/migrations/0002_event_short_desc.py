# Generated by Django 2.2.10 on 2020-08-06 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='short_desc',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
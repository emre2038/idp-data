# Generated by Django 2.2.10 on 2020-08-21 08:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0011_auto_20200821_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventaction',
            name='raw_html',
        ),
        migrations.AddField(
            model_name='eventaction',
            name='description_html',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Description'),
            preserve_default=False,
        ),
    ]

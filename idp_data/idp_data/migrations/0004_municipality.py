# Generated by Django 2.2.10 on 2020-08-09 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0003_auto_20200809_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
            ],
        ),
    ]
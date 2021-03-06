# Generated by Django 2.2.10 on 2020-08-16 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idp_data', '0006_category_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('icon', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(max_length=500)),
                ('event', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='idp_data.Event')),
            ],
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-20 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_your_resources', '0010_auto_20210620_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockist',
            old_name='Area',
            new_name='Area_id',
        ),
    ]

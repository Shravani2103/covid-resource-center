# Generated by Django 3.2.3 on 2021-05-30 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_your_resources', '0004_hospital_h_ph_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='Hospital_resource',
            new_name='Hosres',
        ),
    ]

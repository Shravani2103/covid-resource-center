# Generated by Django 3.2.3 on 2021-06-02 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_your_resources', '0006_auto_20210601_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital_resource',
            name='H_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hres', to='get_your_resources.hospital'),
        ),
    ]
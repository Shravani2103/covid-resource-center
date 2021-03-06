# Generated by Django 3.2.3 on 2021-06-02 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_your_resources', '0007_alter_hospital_resource_h_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharmacy',
            name='Pharm_res',
        ),
        migrations.RemoveField(
            model_name='stockist',
            name='Stockist_resource',
        ),
        migrations.RemoveField(
            model_name='vaccination_center',
            name='Vac_res',
        ),
        migrations.AddField(
            model_name='pharm_res',
            name='P_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pres', to='get_your_resources.pharmacy'),
        ),
        migrations.AddField(
            model_name='stockist_resource',
            name='Stockist_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Sres', to='get_your_resources.stockist'),
        ),
        migrations.AddField(
            model_name='vac_res',
            name='Vc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vres', to='get_your_resources.vaccination_center'),
        ),
    ]

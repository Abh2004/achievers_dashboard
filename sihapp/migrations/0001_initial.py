# Generated by Django 5.0 on 2023-12-20 02:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='RequiredData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depth_md', models.FloatField()),
                ('x_location', models.FloatField()),
                ('y_location', models.FloatField()),
                ('z_location', models.FloatField()),
                ('bulk_density', models.FloatField()),
                ('borehole_size', models.FloatField()),
                ('avg_rate_of_penetration', models.FloatField()),
                ('density_correction_log', models.FloatField()),
                ('wt_of_drilling_mud', models.FloatField()),
                ('image_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sihapp.imagedata')),
            ],
        ),
    ]

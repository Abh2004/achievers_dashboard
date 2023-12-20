# models.py

from django.db import models

class FormData(models.Model):
    image = models.ImageField(upload_to='uploads/')  # Add this line for image upload
    depth_md = models.FloatField()
    x_location = models.FloatField()
    y_location = models.FloatField()
    z_location = models.FloatField()
    bulk_density = models.FloatField()
    borehole_size = models.FloatField()
    avg_rate_of_penetration = models.FloatField()
    density_correction_log = models.FloatField()
    wt_of_drilling_mud = models.FloatField()

    def __str__(self):
        return f"Form Data - {self.pk}"

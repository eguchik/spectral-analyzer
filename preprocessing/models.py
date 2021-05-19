from django.db import models

class FileUpload(models.Model):
    upload_file = models.FileField(upload_to='')
    wl_corr = models.IntegerField(default=900)
    wl_range_start = models.IntegerField(default=190)
    wl_range_end = models.IntegerField(default=900)


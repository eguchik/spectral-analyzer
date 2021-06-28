from django.db import models


class FileUpload(models.Model):
    upload_file = models.FileField(upload_to='')
    wl_corr = models.IntegerField(default=900)


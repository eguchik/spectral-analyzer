from django.db import models

class FileUpload(models.Model):
    upload_file = models.FileField(upload_to='')
    wl_corr = models.IntegerField()


class FileUpload2(models.Model):
    upload_file = models.FileField(upload_to='')
    n_differential = models.IntegerField()
    polyorder = models.IntegerField()
    window_length = models.IntegerField()
    n_smooth = models.IntegerField()
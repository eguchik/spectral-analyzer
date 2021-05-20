from django.db import models

class FileUpload2(models.Model):

    POLYORDER_CHOICE = [
        (2, '2'),
        (4, '4'),
    ]

    upload_file = models.FileField(upload_to='')
    n_differential = models.IntegerField()
    polyorder = models.IntegerField(default=0, choices=POLYORDER_CHOICE)
    window_length = models.IntegerField()
    n_smooth = models.IntegerField()
    wl_range_start = models.IntegerField(default=300)
    wl_range_end = models.IntegerField(default=700)
from django.db import models

class FileUpload(models.Model):

    ALGORITHM_CHOICE = [
        ('FastICA', 'FastICA'),
        ('InfoMax', 'InfoMax'),
        ('JADE', 'JADE'),
    ]

    upload_file = models.FileField(upload_to='')
    n_components = models.IntegerField()
    algo = models.CharField(max_length=255, choices=ALGORITHM_CHOICE)
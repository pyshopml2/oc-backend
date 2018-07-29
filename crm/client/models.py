from django.db import models

class Client(models.Model):
    type_ownership = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)

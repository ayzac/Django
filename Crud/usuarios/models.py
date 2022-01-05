from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length = 100 , blank = False , null = False)
    empresa = models.CharField(max_length = 100 , blank = False , null = False)

    def __str__(self):
        return self.name

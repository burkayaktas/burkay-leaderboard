from django.db import models

class User(models.Model):
    user_id = models.CharField(unique=True, max_length=100)
    display_name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    rank = models.IntegerField(default = 0)
    country = models.CharField(default='tr', max_length=5)

    def __str__(self):
        return self.display_name
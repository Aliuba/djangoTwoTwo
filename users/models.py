from django.db import models

# Create your models here.


class UserModel(models.Model):
    class Meta:
        db_table = 'users'
        verbose_name = 'user'

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name

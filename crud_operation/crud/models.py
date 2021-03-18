from django.db import models

class Post(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=20)
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.Name


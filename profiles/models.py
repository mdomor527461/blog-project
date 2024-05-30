from django.db import models
from author.models import Author
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    phone = models.CharField(max_length=15)
    author = models.OneToOneField(Author,on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.name
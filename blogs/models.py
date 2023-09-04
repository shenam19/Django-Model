from django.db import models

# Create your models here. models = classes ~ tables in DB

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=100)
    date = models.DateField(auto_now= True)
    picture = models.FileField(upload_to='blog_photos', default='sad.jpg')

    def __str__(self): # you will try to print object of this class this method will be called
        return self.title

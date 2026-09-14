from django.db import models

class Post(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField()
    foto = models.ImageField(upload_to='posts/photos/',blank=True,null=True)
    video = models.FileField(upload_to='posts/videos/', blank=True,null=True)
    cr_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
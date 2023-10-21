from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_on = models.DateField()
    image = models.ImageField(upload_to='blogs/images',
                              default='blogs/images/Luffy.jpg')
    bounty = models.ImageField(
        blank=True, upload_to='blogs/images', default='blogs/images/Luffy.jpg')
    description = models.TextField()

    def __str__(self):
        return self.title

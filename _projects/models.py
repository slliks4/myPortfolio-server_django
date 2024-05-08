from django.db import models
from _categories.models import Categories


# Create your models here.
class Projects(models.Model):
    categories = models.ManyToManyField(Categories, related_name='projects')
    image = models.ImageField(upload_to='uploads/_projects/images', blank=True, null=True)
    title = models.CharField(max_length=100);
    text = models.TextField()
    related_blogs = models.ManyToManyField("_blogs.Blogs")
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Projects'
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f"{self.title}-{self.date_created}"
    
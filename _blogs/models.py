from django.db import models
# Create your models here.
class Blogs(models.Model):
    categories = models.ManyToManyField("_categories.Categories")
    image = models.ImageField(upload_to='uploads/_blogs/images', blank=True, null=True)
    title = models.CharField(max_length=100);
    text = models.TextField()
    related_projects = models.ManyToManyField("_projects.Projects", blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Blogs'
        verbose_name = 'Blogs'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return f"{self.title}"
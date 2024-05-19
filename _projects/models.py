from django.db import models

# Create your models here.
class Projects(models.Model):
    categories = models.ManyToManyField("_categories.Categories")
    image = models.ImageField(upload_to='uploads/_projects/images', blank=True, null=True)
    title = models.CharField(max_length=100);
    text = models.TextField()
    links = models.ManyToManyField("_links.Links", blank=True)
    is_lab = models.BooleanField(("isLab"), default=False)
    related_blogs = models.ManyToManyField("_blogs.Blogs", blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Projects'
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f"{self.title}"
    
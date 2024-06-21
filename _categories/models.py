from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Categories")
        verbose_name_plural = ("Categories")
        ordering = ('-id',)

    def save(self, *args, **kwargs):
        # Convert fields to lowercase
        self.name = self.name.lower()
        super(Categories, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
from django.db import models

# Create your models here.

class Links(models.Model):
    name = models.CharField(("Name"), max_length=150)
    title = models.CharField(("Name"), max_length=150, blank=True, null= True)
    url = models.CharField(("Url"), max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Links'
        verbose_name = 'Links'
        verbose_name_plural = 'Links'

    def __str__(self) -> str:
        return f"{self.name, self.title}"
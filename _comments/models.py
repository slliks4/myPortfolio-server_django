from django.db import models

# Create your models here.
class Comments(models.Model):
    blog = models.ForeignKey(
        "_blogs.Blogs", 
        on_delete=models.SET_NULL, 
        related_name='comments', 
        blank=True, 
        null=True
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comments'
        ordering=('-created_at',)

    def __str__(self) -> str:
        return f'{self.message}'
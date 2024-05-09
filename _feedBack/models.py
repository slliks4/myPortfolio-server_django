from django.db import models

# Create your models here.
class FeedBack(models.Model):
    full_name = models.CharField(("Full Name"), max_length=250)
    email = models.EmailField(("Email"), max_length=254)
    subject = models.CharField(("Subject"), max_length=350)
    message = models.TextField(("Message"))
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Feed Back'
        verbose_name = 'Feed Back'
        verbose_name_plural = 'Feed Back'

    def __str__(self) -> str:
        return f"{self.full_name} | {self.email} | {self.date_posted}"
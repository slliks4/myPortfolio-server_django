from django.db import models

# Create your models here.

class Mission(models.Model):
    title = models.CharField(max_length=450)
    statement = models.TextField(("Statement"))

    class Meta:
        db_table = 'Mission'
        verbose_name = 'Mission'
        verbose_name_plural = 'Mission'

    def __str__(self) -> str:
        return self.title
    
class Vision(models.Model):
    title = models.CharField(max_length=450)
    statement = models.TextField(("Statement"))

    class Meta:
        db_table = 'Vision'
        verbose_name = 'Vision'
        verbose_name_plural = 'Vision'

    def __str__(self) -> str:
        return self.title

class Profile(models.Model):
    user_name = models.CharField(("username"), max_length=50)
    first_name = models.CharField(("First name"), max_length=100)
    last_name = models.CharField(("Last name"), max_length=150)
    pic = models.ImageField(
        ("Profile picture"), 
        upload_to='uploads/_profile/images', 
        height_field=None, 
        width_field=None, 
        max_length=None,
        blank= True,
        null= True
    )
    about_pic = models.ImageField(
        ("About page picture"), 
        upload_to='uploads/_profile/images', 
        height_field=None, 
        width_field=None, 
        max_length=None,
        blank= True,
        null= True
    )
    mission = models.OneToOneField(Mission, on_delete=models.SET_NULL, null=True, related_name='mission')
    vision = models.OneToOneField(Vision, on_delete=models.SET_NULL, null=True, related_name='vision')
    address = models.TextField()
    home_text = models.CharField(("Home text"), max_length=500)
    links = models.ManyToManyField("_links.Links", blank=True)
    

    class Meta:
        db_table = 'Profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self) -> str:
        return f"{self.user_name} | {self.first_name},{self.last_name}"

class Files(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='files')
    file = models.FileField(("Files"), upload_to='uploads/_profile/files', max_length=100,blank=True,null=True)
    
    class Meta:
        db_table = 'Files'
        verbose_name = 'Files'
        verbose_name_plural = 'Files'


class Email(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='email')
    email = models.EmailField(("Email"), max_length=254)
    
    class Meta:
        db_table = 'Email'
        verbose_name = 'Email'
        verbose_name_plural = 'Email'

    def __str__(self) -> str:
        return self.email

class Tel(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='tel')
    tel = models.CharField(("Tel"), max_length=14)
    
    class Meta:
        db_table = 'Tel'
        verbose_name = 'Tel'
        verbose_name_plural = 'Tel'

    def __str__(self) -> str:
        return self.tel
    
class Services(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='services')
    title = models.CharField(("Title"), max_length=150)
    text = models.TextField(("Text"))
    icon = models.ImageField(
        ("Icon"), 
        upload_to='uploads/_profile/icons', 
        height_field=None, 
        width_field=None, 
        max_length=None,
        blank=True,
        null= True
    )
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Services'
        verbose_name = 'Services'
        verbose_name_plural = 'Services'

    def __str__(self) -> str:
        return self.title

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='education')
    degree = models.CharField(("Degree name"), max_length=450)
    date_period = models.CharField(("Date Period"), max_length=350)
    school_name = models.CharField(("School Name"), max_length=450)
    school_link = models.CharField(("School Link"), max_length=500, blank=True, null=True)
    text = models.TextField(("Text"))
    
    class Meta:
        db_table = 'Education'
        verbose_name = 'Education'
        verbose_name_plural = 'Education'

    def __str__(self) -> str:
        return f"{self.degree} | {self.school_name}"

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='experience')
    title = models.CharField(("Title"), max_length=450)
    date_period = models.CharField(("Date Period"), max_length=350)
    company_name = models.CharField(("Company Name"), max_length=450)
    company_link = models.CharField(("Company Link"), max_length=500, blank=True, null=True)
    text = models.TextField(("Text"))
    
    class Meta:
        db_table = 'Experience'
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'

    def __str__(self) -> str:
        return f"{self.title} | {self.company_name}"
    
class Skills(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='skills')
    name = models.CharField(("name"), max_length=150)
    level = models.CharField(("level"), max_length=150)
    class Meta:
        db_table = 'Skills'
        verbose_name = 'Skills'
        verbose_name_plural = 'Skills'

    def __str__(self) -> str:
        return f"{self.name} | {self.level}"
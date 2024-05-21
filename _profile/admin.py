from django.contrib import admin
from .models import *

class SkillsInline(admin.StackedInline):
    model = Skills
    extra = 0
class FilesInline(admin.StackedInline):
    model = Files
    extra = 0

class EmailInline(admin.StackedInline):
    model = Email
    extra = 0

class TelInline(admin.StackedInline):
    model = Tel
    extra = 0

class ServicesInline(admin.StackedInline):
    model = Services
    extra = 0

class EducationInline(admin.StackedInline):
    model = Education
    extra = 0

class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 0

class ProfileModelAdmin(admin.ModelAdmin):
    model = Profile
    inlines = [FilesInline, EmailInline, TelInline, EducationInline, ExperienceInline, ServicesInline, SkillsInline]

# Register your models here.
admin.site.register(Profile, ProfileModelAdmin)
admin.site.register(Mission)
admin.site.register(Vision)
admin.site.site_header="My Portfolio"
admin.site.site_title="Portfolio"
admin.site.index_title="Administrator"
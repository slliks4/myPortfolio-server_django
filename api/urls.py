# Imports
from django.urls import path
from .import views
from _categories.views import getCategories
from _blogs.views import getBlogs, getBlogDetail
from _projects.views import getProjects, getProjectDetail

urlpatterns = [
    # End points
    path('', views.EndPoints, name='endpoints'),
    
    # Categories
    path("categories/", getCategories, name="categories"),

    # Blogs
    path("blogs/", getBlogs, name="blogs"),
    path("blog_detail/<int:id>/", getBlogDetail, name="blog_detail"),

    # Projects
    path("projects/", getProjects, name="projects"),
    path("project_detail/<int:id>/", getProjectDetail, name="project_detail"),
]

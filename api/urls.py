# Imports
from django.urls import path
from .import views
from _categories.views import getCategories
from _blogs.views import getBlogs, getBlogDetail
from _projects.views import getProjects, getProjectDetail
from _profile.views import getProfile

urlpatterns = [
    # End points
    path('endpoints/', views.EndPoints, name='endpoints'),
    
    # Categories
    path("categories/", getCategories, name="categories"),

    # Blogs
    path("blog/", getBlogs, name="blogs"),
    path("blog/<int:id>/", getBlogDetail, name="blog_detail"),

    # Projects
    path("project/", getProjects, name="projects"),
    path("project/<int:id>/", getProjectDetail, name="project_detail"),

    # Profile
    path("profile/<str:user_name>/", getProfile, name="profile")
]

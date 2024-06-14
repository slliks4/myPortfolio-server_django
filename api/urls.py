# Imports
from django.urls import path
from .import views
from _categories.views import getCategories
from _blogs.views import getBlogs, getBlogDetail
from _projects.views import getProjects, getProjectDetail
from _profile.views import getProfile
from _feedBack.views import postFeedBack
from _comments.views import getComments, postComments

urlpatterns = [
    # End points
    path('', views.EndPoints, name='endpoints'),
    
    # Categories
    path("categories/", getCategories, name="categories"),

    # Blogs
    path("blog/", getBlogs, name="blogs"),
    path("blog/<int:id>/", getBlogDetail, name="blog_detail"),

    # Blog Comments
    path("getComments/<int:blog_id>", getComments, name="getComments"),
    path("postComments/<int:blog_id>", postComments, name="postComments"),

    # Projects
    path("project/", getProjects, name="projects"),
    path("project/<int:id>/", getProjectDetail, name="project_detail"),

    # Profile
    path("profile/<str:user_name>/", getProfile, name="profile"),

    # FeedBack
    path("postFeedBack", postFeedBack, name="postFeedBack")
]

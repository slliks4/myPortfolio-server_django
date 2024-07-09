# Imports
from django.urls import path
from .import views
from _categories.views import getCategories
from _blogs.views import getBlogs, getBlog
from _projects.views import get_projects, get_project
from _profile.views import getProfile
from _feedBack.views import postFeedBack
from _comments.views import getComments, postComment

urlpatterns = [
    # End points
    path('', views.EndPoints, name='endpoints'),
    
    # Categories
    path("getCategories/", getCategories, name="categories"),

    # Blogs
    path("getBlogs/", getBlogs, name="blogs"),
    path("getBlog/<int:id>/", getBlog, name="blog_detail"),

    # Blog Comments
    path("getComments/<int:blog_id>", getComments, name="getComments"),
    path("postComment/<int:blog_id>", postComment, name="postComment"),

    # Projects
    path("getProjects/", get_projects, name="projects"),
    path("getProject/<int:project_id>/", get_project, name="project_detail"),

    # Profile
    path("getProfile/<str:user_name>/", getProfile, name="profile"),

    # FeedBack
    path("postFeedBack", postFeedBack, name="postFeedBack")
]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path("view/", views.view, name="view"),
    path("database/", views.database, name="databases"),
    path("courses/", views.course, name="course"),
    path("mentor/", views.mentor, name="mentor"),
    path("courses/update_course/<str:code>/", views.update_course, name="update_course"),
    path("courses/update_course_post/<str:code>/", views.update_course_post, name="update_course_post"),
    path("courses/delete_course/<str:code>/", views.delete_course, name="delete_course"),
    path("mentor/update_mentor/<str:menid>/", views.update_mentor, name="update_mentor"),
    path('mentor/update_mentor/save_update_mentor/<str:menid>', views.save_update_mentor, name="save_update_mentor"),
    path('searchcourses/', views.search_course, name="search_course"),
]

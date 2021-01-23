
from django.urls import path, include

from courses import views
app_name = 'courses'



urlpatterns = [
    path('',views.courses, name='courses'),
    path('detail/<slug:slug>',views.courses_detail, name='course_detail'),
    path('feature_course/<slug:slug>',views.courses_detail, name='course_detail'),
    path('feature_course/<slug:slug>',views.courses_detail, name='course_detail_feature_course'),
    path('category/<int:category>',views.courses, name='course_category'),
]

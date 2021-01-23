
from django.urls import path, include

from instructor import views
app_name = 'instructor'



urlpatterns = [
    path('profile/<int:id>',views.profile, name='profile'),
]

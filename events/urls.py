
from django.urls import path, include

from events import views
app_name = 'events'



urlpatterns = [
    path('',views.courses, name='events'),
    path('detail/<int:id>',views.event_detail, name='event_detail'),
    path('category/<int:event_category>',views.courses, name='events_category'),

]

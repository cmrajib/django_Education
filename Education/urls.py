from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('accounts/',include('UserRegistration.urls')),
    path('about/',include('about.urls')),
    path('blog/',include('blog.urls')),
    path('courses/', include('courses.urls')),
    path('events/', include('events.urls')),
    path('instructor/', include('instructor.urls')),
    path('contact/',include('contact.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
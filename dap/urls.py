from django.contrib import admin
from django.urls import path ,include
import book.urls
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(book.urls)),
    path('app-auth/',include('rest_framework.urls'))
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('server/', include('server.urls')),
    path('admin/', admin.site.urls),

]

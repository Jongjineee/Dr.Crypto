from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include, handler400, handler403, handler404, handler500
from doctor import views as doctor_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', doctor_views.index, name = 'root'),
    url(r'^doctor/', include('doctor.urls')),
    #url(r'^accounts/', include('django.contrib.auth.urls')),
    #url(r'^accounts/signup$', doctor_views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

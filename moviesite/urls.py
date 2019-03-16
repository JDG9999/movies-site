from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    path('catalog/', include('moviecatalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('api/', include('api.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

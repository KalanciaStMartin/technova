from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # Pages statiques (accueil, à propos...)
    path('programmes/', include('programmes.urls')),
    path('etudiants/', include('etudiants.urls')),
    path('bibliotheque/', include('bibliotheque.urls')),
    path('blog/', include('blog.urls')),
    path('evenements/', include('evenements.urls')),
]

# Pour servir les fichiers média en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
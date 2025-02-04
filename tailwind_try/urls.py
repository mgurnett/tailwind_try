from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
admin.site.site_header = 'GranaryWatch administration'              # default: "Django Administration"
admin.site.index_title = 'Welcome to the GranaryWatch admin area'   # default: "Site administration"  browser title
admin.site.site_title = 'GranaryWatch admin'                        # default: "Django site admin"

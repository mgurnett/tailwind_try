from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("template/", TemplateView.as_view(), name="template_sheet"),
    path("granary/<int:pk>/", GranaryView.as_view(), name="granary_detail"),

    # htmx
    path ('live_latest_update/<int:pk>/', views.live_latest_update, name='live_latest_updates'),
    path ('live_high_temp_update/<int:pk>/', views.live_high_temp_update, name='live_high_temp_update'),
    path ('live_battery_update/<int:pk>/', views.live_battery_update, name='live_battery_update'),


]

'''

urlpatterns = [
    path ('', views.Home.as_view(), name = 'core_home'),
    path ('utilities/', views.Utilities.as_view(), name = 'utilities'),
    path ('granary/<int:pk>/', views.GranaryDetail.as_view(), name = 'granary_detail'),
    path ('granary_visual/<int:pk>/', views.GranaryVisual.as_view(), name = 'granary_visual'),
    path ('granary/graph/<int:pk>/', views.GranaryGraph.as_view(), name = 'granary_graph'),
    path ('sensor/<int:pk>/', views.SensorDetail.as_view(), name = 'sensor_detail'),
    path ('granary/battery/<int:pk>/', views.Battery_graph.as_view(), name = 'battery_graph'),

    # htmx
    path ('get_temp/<int:pk>/', views.get_temp, name='get_temp'), # New URL for graph updates
    path ('get_graph/<int:pk>/', views.GetGraphView.as_view(), name='get_graph'),

    # button tools
    path ('archive/', Archive_data, name = 'archive_data'),
    path ('alarm_clear/<int:pk>/', Alarm_Clear, name = 'alarm_clear'),
    path ('replace_battery/<int:pk>/', Battery_replace, name = 'replace_battery'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
'''

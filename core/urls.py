from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path("", HomeView.as_view(template_name="core/home.html")),
    path("template/", TemplateView.as_view(template_name="core/template_sheet.html")),
]
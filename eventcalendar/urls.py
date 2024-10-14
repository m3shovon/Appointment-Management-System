
from django.contrib import admin
from django.urls import path, include
from schema_graph.views import Schema

from .views import DashboardView


urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", include("calendarapp.urls")),
    path("schema/", Schema.as_view()),
]

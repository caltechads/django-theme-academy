from typing import Final

from django.urls import path

from .views import HomeView, WildewidgetsView

# These URLs are loaded by demo/urls.py.
app_name: Final[str] = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('wildewidgets', WildewidgetsView.as_view(), name='wildewidgets'),
]

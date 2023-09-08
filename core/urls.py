from django.urls import path
from .views import set_language, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('set_language', set_language, name="set_language")
]
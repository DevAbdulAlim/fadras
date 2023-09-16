from django.urls import path
from .views import set_language, HomePageView, ProjectPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('projects', ProjectPageView.as_view(), name='projects' ),
    path('set_language', set_language, name="set_language")
]
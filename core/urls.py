from django.urls import path
from .views import set_language, HomePageView, AboutPageView, ProjectPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('projects', ProjectPageView.as_view(), name='projects' ),
    path('contact', ContactPageView.as_view(), name='contact' ),
    path('set_language', set_language, name="set_language")
]
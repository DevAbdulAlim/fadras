from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View

# Create your views here.
class HomePageView(View):
    def get(self, request):
        dummy_range = range(6)
        return render(request, 'core/index.html', {"dummy_range": dummy_range})

def set_language(request):
    language = request.GET.get('language')

    # Validate the language parameter
    if language in ['en', 'bn']:
        # Set the language in the session or cookie
        request.session['django_language'] = language

        # Determin the URL to redirect to (you can set it to the page the user was on )
        redirect_url = request.META.get('HTTP_REFERER', '/')
        return redirect(redirect_url)

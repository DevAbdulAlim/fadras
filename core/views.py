from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from product.models import Category
from django.utils.translation import activate
from django.db.models import F

# Create your views here.
class HomePageView(View):
    def get(self, request):
        # Get user's selected language
        user_language = request.session.get('django_language', settings.LANGUAGE_CODE)
       


        # Determine which columns to select based on language
        name_column = F('name_en')
        description_column = F('description_en')
        if user_language == 'ar':
            name_column = F('name_ar')
            description_column = F('description_ar')
       


        # Fetch categories with appropriate columns based on language
      
        category_list = Category.objects.annotate(
            name=name_column,
            description=description_column
        ).values('name', 'description', 'image')

        # Set ther selected language for this view
        activate(user_language)

        # ! markets
        market_list = list(range(6))


        # ! Clients
        client_list = list(range(12))


        return render(request, 'core/index.html', {"category_list": category_list, "market_list": market_list, "client_list": client_list })

class ProjectPageView(View):
    def get(self, request):
        dummy_data = list(range(6))
        return render(request, 'core/projects.html', {"project_list": dummy_data})




def set_language(request):
    language = request.GET.get('language')

    # Validate the language parameter
    if language in ['en', 'ar']:
        # Set the language in the session or cookie
        request.session['django_language'] = language

        # Determin the URL to redirect to (you can set it to the page the user was on )
        redirect_url = request.META.get('HTTP_REFERER', '/')
        return redirect(redirect_url)

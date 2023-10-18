from product.models import Category

def current_path(request):
    return {'current_path': request.path}

def category_list(request):
    categories = Category.objects.all()[:10].values('id', 'name_en')
    
    category_dict = {
        'categories': categories,
    }
    
    return category_dict
    
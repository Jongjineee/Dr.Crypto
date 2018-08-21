from .models import Category

def add_variable_to_context(request):
    nav_user = request.user
    nav_categories = Category.objects.filter(sort="DOCTOR")
    return {
        'nav_user': nav_user,
        'nav_categories': nav_categories
    }

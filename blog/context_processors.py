
from .models import Category
from about.models import SocialLink

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_sociallinks(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)
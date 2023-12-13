from .models import blogCategoryTable


def menu_links(req):
    links = blogCategoryTable.objects.all()
    return dict(links=links)
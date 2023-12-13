
from .models import blogPostTable

def searchProjects(req):

    category = req.GET.get('category')
    search = ''

    if req.GET.get('search'):
        search = req.GET.get('search')
    
    

    if category == None:
        post = blogPostTable.objects.all()
        post = blogPostTable.objects.filter(post_title__icontains=search)
    else:
        post = blogPostTable.objects.filter(category__cate_name = category)

    return search,post
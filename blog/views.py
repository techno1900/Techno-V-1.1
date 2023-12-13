from django.shortcuts import render
from .models import blogPostTable, blogCategoryTable
from .utils import searchProjects

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(req):

    search,post = searchProjects(req)

    page = req.GET.get('page')
    result = 20
    paginator = Paginator(post, result)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        post = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        post = paginator.page(page)

    leftIndex = (int(page)-3)
    if leftIndex <1:
        leftIndex = 1
    
    rightIndex = (int(page) + 5)
    if rightIndex>paginator.num_pages:
        rightIndex = paginator.num_pages +1

    custome_range = range(leftIndex,rightIndex)


    cate = blogCategoryTable.objects.all()
    context = {'post':post, 'cate':cate, 'search':search, 'paginator':paginator, 'range':custome_range} 
    return render(req, 'blog/home.html', context)

def singlePost(req, pk):
    post = blogPostTable.objects.get(post_id = pk)

    cate = blogCategoryTable.objects.all()
    context = {'post':post, 'cate':cate} 
    return render(req, 'blog/post.html', context)






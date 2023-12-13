from django.contrib import admin
from .models import blogPostTable, blogCommentTable, blogCategoryTable

admin.site.register(blogPostTable)
admin.site.register(blogCategoryTable)
admin.site.register(blogCommentTable)

# Register your models here.

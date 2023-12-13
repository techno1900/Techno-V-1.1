from django.db import models
import uuid

class blogPostTable(models.Model):
    post_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    post_title = models.CharField(max_length=200)
    post_description = models.TextField(null=True, blank=True)
    git_link = models.CharField(max_length=2000, null=True, blank=True)
    other_link = models.CharField(max_length=2000, null=True, blank=True)
    youtube_link = models.CharField(max_length=2000, null=True, blank=True)
    category = models.ForeignKey('blogCategoryTable', on_delete=models.CASCADE)
    post_image = models.ImageField(default='default.jpg', null=True, blank=True, upload_to='post/')
    adds = models.ImageField(default='default.jpg', null=True, blank=True, upload_to='adds/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title
    
    class Meta:
        ordering =['-created']


class blogCategoryTable(models.Model):
    cate_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    cate_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cate_name


class blogCommentTable(models.Model):
    email = models.EmailField(max_length=1000)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(blogPostTable, on_delete=models.CASCADE)
    comment_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)


    def __str__(self):
        return self.email
    

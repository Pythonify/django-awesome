import sys
from django.db import models

sys.path.append('../')
auth = __import__('my_auth', globals(), locals())


# Create your models here.


class Blogs(models.Model):
    user = models.ForeignKey(auth.models.Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(verbose_name='date created', auto_now_add=True)

    def __str__(self):
        return self.name

    __repr__ = __str__


class Comments(models.Model):
    user = models.ForeignKey(auth.models.Users, on_delete=models.PROTECT)
    blog = models.ForeignKey(Blogs, on_delete=models.PROTECT)
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return '%s:%s' % (self.blog.name, self.user.name)

    __repr__ = __str__


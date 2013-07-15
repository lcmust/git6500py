from django.db import models
from django.forms import ModelForm
import datetime

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=20, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' %(self.tag_name)


class Author(models.Model):
    name = models.CharField(max_length=30, unique=True)
    SEX_CHOICE = (
        ('1', 'boy'),
        ('2', 'girl'),
        )
    sex = models.CharField(max_length=1, choices=SEX_CHOICE, default=1)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class BlogManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(caption__icontains=keyword).count()

    def tag_count(self, keyword):
        return self.filter(tags__icontains=keyword).count()


class Blog(models.Model):
    caption = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    count_objects = BlogManager()
    taglist = []

    def save(self, *args, **kwargs):
        super(Blog, self).save()
        for i in self.taglist:
            p, created = Tag.objects.get_or_create(tag_name=i)
            self.tags.add(p)

    def __unicode__(self):
        return u'%s' % (self.caption)

    def was_published_recently(self):
        return self.publish_time >= datetime.datetime.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'publish_time'


class Weibo(models.Model):
    message = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    publish_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.message


class AuthorForm(ModelForm):
    class Meta:
        model = Author


class BlogForm(ModelForm):
    class Meta:
        model = Blog


class Abc():
    pass

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(upload_to='authors_photos')
    about = models.TextField()

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class category(models.Model):
    cat_name = models.CharField("Category", max_length=100)

    def __str__(self):
        return self.cat_name

@python_2_unicode_compatible
class post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(upload_to='blog_photos/%Y/%m/%d')
    pub_date = models.DateField()
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    category = models.ForeignKey(category)

    def __str__(self):
        return self.title

    def comments_number(self):
        return self.comment_set.count()

    def post_excerpt(self):
        return self.text[:300]

@python_2_unicode_compatible
class comment(models.Model):
    title = models.CharField("Comment Title", max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField()
    text = models.TextField()
    date = models.DateField()
    accept = models.BooleanField("Accepted?")
    comments = models.ForeignKey(post, on_delete=models.CASCADE)

    def __str__ (self):
        return self.title

    def accepted (self):
        return self.accept
    accepted.boolean = True

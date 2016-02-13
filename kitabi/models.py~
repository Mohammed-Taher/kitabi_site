from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class authors(models.Model):
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    no_books = models.IntegerField()
    about = models.TextField()
    image = models.ImageField()
    facebook = models.CharField(max_length=300)
    twitter = models.CharField(max_length=300)
    website = models.CharField(max_length=300)

    def __str__(self):
        return self.f_name + " " + self.l_name

@python_2_unicode_compatible
class book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(authors)
    cover = models.CharField(max_length=400)
    org_title = models.CharField(max_length=250)
    lang = models.CharField(max_length=250)
    pages = models.IntegerField(default=0)
    pub_date = models.DateField()
    publisher = models.CharField(max_length=250)
    rating = models.IntegerField(default=0)
    ratings = models.IntegerField(default=0)
    reviews = models.IntegerField(default=0)
    get_a_copy = models.CharField(max_length=250)
    genres = models.CharField(max_length=250)
    isbn = models.IntegerField(default=0)
    summery = models.TextField()

    def __str__(self):
        return self.title

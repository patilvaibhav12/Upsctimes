from django.db import models

# Create your models here.

class homepost(models.Model):
    title = models.CharField(max_length=150)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    slug = models.CharField(max_length=150, default='')
    def __str__(self):
        return self.title

class books(models.Model):
    title = models.CharField(max_length = 150)
    img = models.ImageField(upload_to='book')
    adminupload = models.FileField(upload_to = 'book')
    desc = models.TextField()

    def __str__(self):
        return self.title

class newspaper(models.Model):
    title = models.CharField(max_length = 150)
    adminupload = models.FileField(upload_to = 'newspaper')
    desc = models.TextField()

    def __str__(self):
        return self.title
    
class eml(models.Model):
    name = models.CharField(max_length = 50 , null = False , blank = False, default='')
    email = models.CharField(max_length = 150 , null = False , blank = False)

    def __str__(self):
        return self.name


class history(models.Model):
    qst = models.TextField(max_length=600)
    a = models.CharField(max_length = 250)
    b = models.CharField(max_length = 250)
    c = models.CharField(max_length = 250)
    d = models.CharField(max_length = 250)
    ans = models.CharField(max_length = 250)

class geography(models.Model):
    qst = models.TextField(max_length=600)
    a = models.CharField(max_length = 250)
    b = models.CharField(max_length = 250)
    c = models.CharField(max_length = 250)
    d = models.CharField(max_length = 250)
    ans = models.CharField(max_length = 250)

class polity(models.Model):
    qst = models.TextField(max_length=600)
    a = models.CharField(max_length = 250)
    b = models.CharField(max_length = 250)
    c = models.CharField(max_length = 250)
    d = models.CharField(max_length = 250)
    ans = models.CharField(max_length = 250)

class currentaffairs(models.Model):
    qst = models.TextField(max_length=600)
    a = models.CharField(max_length = 250)
    b = models.CharField(max_length = 250)
    c = models.CharField(max_length = 250)
    d = models.CharField(max_length = 250)
    ans = models.CharField(max_length = 250)

class generalscience(models.Model):
    qst = models.TextField(max_length=600)
    a = models.CharField(max_length = 250)
    b = models.CharField(max_length = 250)
    c = models.CharField(max_length = 250)
    d = models.CharField(max_length = 250)
    ans = models.CharField(max_length = 250)

class impupdates(models.Model):
    desc = models.CharField(max_length=300)

class gjobs(models.Model):
    title = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=350)
    description = models.TextField()
    slug = models.CharField(max_length=150)
    def __str__(self):
        return self.slug

class pjobs(models.Model):
    title = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=350)
    description = models.TextField()
    slug = models.CharField(max_length=150)
    def __str__(self):
        return self.slug
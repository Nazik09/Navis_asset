from django.db import models

class Partner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='partners/')

    def __str__(self):
        return self.title


class Zaiavka(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    recovery_type = models.CharField(max_length=100)
    wallet_type = models.CharField(max_length=100)
    wallet_amount = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Otzyvy(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='reviews/')

    def __str__(self):
        return self.name
    
class Price(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    percent = models.CharField(max_length=20)

    def __str__(self):
        return self.title


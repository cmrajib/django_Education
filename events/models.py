from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
        return self.name

class EventModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='event_category')
    cost = models.FloatField(default=0.0)

    image = models.ImageField(upload_to='events', default='no-name.jpg', null=True)
    time_from = models.TimeField()
    time_to = models.TimeField()
    date = models.DateField(auto_now=True)
    datetime = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=30)
    address = models.TextField()


    email = models.EmailField()
    phone = models.IntegerField()

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.name


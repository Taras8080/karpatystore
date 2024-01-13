from django.db import models
from django.utils import timezone
from django.contrib.gis.geos import Point


class Post(models.Model):
    CHOICES = (
        ('parking', 'Парковка'),
        ('mangal', 'Мангал'),
        ('sauna', 'Сауна'),
        ('tenis', 'Теніс'),
        ('WI-FI', 'WI-FI'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="Слаг")
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="photos")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=255, verbose_name="Адреса об'єкта")
    latitude = models.DecimalField(max_digits=10, decimal_places=6, verbose_name="Широта в градусах")
    longitude = models.DecimalField(max_digits=10, decimal_places=6, verbose_name="Довгота в градусах")
    relax = models.CharField(max_length=300, choices = CHOICES)
    is_highlighted = models.BooleanField(default=False)
    highlighted_until = models.DateTimeField(null=True, blank=True)


    def get_highlighted_html(self):
        if self.is_highlighted:
            return f'''<div class="highlighted-ad">
            {self.get_html()}
            </div>
            '''
        else:
            return self.get_html()


    def get_non_highlighted_html(self):
        if not self.is_highlighted:
            return f'''
            <div class="non-highlighted-ad">
            {self.get_html()}
            </div>
            '''
        else:
            return self.get_html()
        

    def is_highlighted_now(self):
        if self.is_highlighted and self.highlighted_until is None:
            return True
        elif self.is_highlighted and self.highlighted_until > timezone.now():
            return True
        else:
            return False


    def __str__(self):
        return self.title
    
    
    

    def get_coordinates(self):
        return Point(self.latitude, self.longitude)
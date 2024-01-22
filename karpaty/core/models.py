from django.db import models
from django.utils import timezone


class Post(models.Model):
    CHOICES = (
        ('Hotel', 'Готель'),
        ('Private', 'Приватний сектор'),
        
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Слаг", db_index=True)
    description = models.TextField(blank=False, null=False)
    price = models. DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="photos")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=255, verbose_name="Адреса об'єкта")
    relax = models.CharField(max_length=300, choices = CHOICES)
    is_highlighted = models.BooleanField(default=False)
    highlighted_until = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)


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
    
    class Meta:
        verbose_name = "Місце знаходження"
        verbose_name_plural = "Місця знаходження"
    
    
    
class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва категорії", unique=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Url", null=True)

    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "categories"
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
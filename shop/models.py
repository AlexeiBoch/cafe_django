from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='название')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='ссылка(оставить по умолчанию)')
    
    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='название')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='ссылка(оставить по умолчанию)')
    image = models.ImageField(upload_to='products', blank=False, verbose_name='изображение')
    description = models.TextField(blank=False, verbose_name='описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    created = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='обновлено')
    
    def __str__(self) -> str:
        return f'{self.category}:{self.name}'
    
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        index_together = (('id', 'slug'),)
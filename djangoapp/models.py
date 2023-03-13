from django.db import models
from django_extensions.db.fields import AutoSlugField
# Create your models here.

# Comics
class CategoryComic(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100) 
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('slug', 'parent')    
        verbose_name_plural = "comics categories"

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1]) 

class SubCategoryComic(models.Model):
    child = models.ForeignKey(CategoryComic, default=None, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255, null=False,)
    covers = models.CharField(max_length=2000)

    def __str__(self):
        return self.title

class DetailComic(models.Model):
    post = models.ForeignKey(SubCategoryComic, default=None, on_delete=models.CASCADE, blank=True, null=True)
    comics = models.CharField(max_length=2000)

    def __str__(self):
        return self.post.title
# =======================================================================================================================

# Movies
class CategoryMovie(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100) 
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    class Meta:
        unique_together = ('slug', 'parent')    
        verbose_name_plural = "movies categories"

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

class SubCategoryMovie(models.Model):
    child = models.ForeignKey(CategoryMovie, default=None, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    poster = models.CharField(max_length=2000)

    def __str__(self):
        return self.title

class DetailMovie(models.Model):
    upload = models.ForeignKey(SubCategoryMovie, default=None, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=1000, null=False)
    cast = models.CharField(max_length=300, null=False)
    poster = models.CharField(max_length=2000)
    videos = models.CharField(max_length=2000)

    def __str__(self):
        return self.upload.title
# ========================================================================================================================

# Series
class CategorySeries(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    poster = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
    
    class Meta:
        unique_together = ('slug', 'parent')    
        verbose_name_plural = "series categories"

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

class SubCategorySeries(models.Model):
    child = models.ForeignKey(CategorySeries, default=None, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255, null=False)
    thumbnail = models.CharField(max_length=2000)

    def __str__(self):
        return self.title

class DetailSeries(models.Model):
    uploads = models.ForeignKey(SubCategorySeries, default=None, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    cast = models.CharField(max_length=300) 
    poster = models.CharField(max_length=2000)
    videos = models.CharField(max_length=2000)

    def __str__(self):
        return self.uploads.title
# ========================================================================================================================

# Shop
class Shop(models.Model):
    title = models.CharField(max_length=2000, null=False)
    description = models.TextField()
    price = models.CharField(max_length=2000, null=False)
    cover = models.CharField(max_length=2000, null=False)

    def __str__(self):
        return self.title
    
class DetailShop(models.Model):
    items = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=2000, null=False)
    description = models.TextField()
    price = models.CharField(max_length=2000, null=False)
    photos = models.CharField(max_length=2000, null=False)

    def __str__(self):
        return self.items.title
# ========================================================================================================================

# Marvel Character
class MarvelHeroes(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=300, null=False, blank=True)
    images = models.CharField(max_length=300, null=False, blank=True)

    def __str__(self):
        return self.name

class MarvelVillain(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=300, null=False, blank=True)
    images = models.CharField(max_length=300, null=False, blank=True)

    def __str__(self):
        return self.name

class DetailHeroes(models.Model):
    char_heroes = models.ForeignKey(MarvelHeroes, default=None, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=300, null=False, blank=True)
    story = models.TextField(blank=True)
    multiverse = models.CharField(max_length=300, blank=True)
    images = models.CharField(max_length=300, null=False, blank=True)

    def __str__(self):
        return self.char_heroes.name
    
class DetailVillain(models.Model):
    char_villain = models.ForeignKey(MarvelVillain, default=None, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=300, null=False, blank=True)
    story = models.TextField(blank=True)
    multiverse = models.CharField(max_length=300, blank=True)
    images = models.CharField(max_length=300, null=False, blank=True)
    
    def __str__(self):
        return self.char_villain.name
# ====================================================================================================================
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
class CategoryShop(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100) 
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    photos = models.FileField(upload_to='media/shop/photos', blank=True, null=False)

    def __str__(self):
        return self.title
    
    class Meta:
        unique_together = ('slug', 'parent')    
        verbose_name_plural = "Shops categories"

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1]) 

class DetailShop(models.Model):
    add = models.ForeignKey(CategorySeries, default=None, on_delete=models.CASCADE, blank=True, null=True)
    items = models.FileField(upload_to='media/shop/items', null=False)

    def __str__(self):
        return self.add.title
# ========================================================================================================================
     
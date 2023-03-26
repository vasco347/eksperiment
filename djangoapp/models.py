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

class SubCategoryMovie(models.Model):
    child = models.ForeignKey(CategoryMovie, default=None, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    poster = models.CharField(max_length=2000)

    def __str__(self):
        return self.title

class DetailMovie(models.Model):
    upload = models.ForeignKey(SubCategoryMovie, default=None, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=300)
    release = models.CharField(max_length=100)
    cast = models.CharField(max_length=300)
    synopsis = models.TextField(max_length=2000)
    poster = models.CharField(max_length=2000)
    imdb_rating = models.CharField(max_length=100)
    rotten_rating = models.CharField(max_length=100)
    videos = models.CharField(max_length=2000)

    def __str__(self):
        return self.upload.title
# ========================================================================================================================

# Series
class Series(models.Model):
    parent = models.ForeignKey('self', related_name='series', on_delete=models.CASCADE, blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=2000)
    poster = models.CharField(max_length=2000)
    cast = models.CharField(max_length=2000)
    description = models.TextField()   
    release = models.CharField(max_length=2000)
    imdb_rating = models.CharField(max_length=2000)
    rotten_rating = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
    
class Season(models.Model):
    series = models.ForeignKey(Series, default=None, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=300)
    season = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title

class Episode(models.Model):
    season = models.ForeignKey(Season, default=None, on_delete=models.CASCADE, blank=True, null=True)
    episode = models.CharField(max_length=300)
    title = models.CharField(max_length=2000, blank=True)
    thumbnail = models.CharField(max_length=2000)
    videos = models.CharField(max_length=2000) 
    
    def __str__(self):
        return self.episode

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
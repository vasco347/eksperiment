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

class SubCategoryComic(models.Model):
    child = models.ForeignKey(CategoryComic, default=None, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    covers = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class DetailComic(models.Model):
    post = models.ForeignKey(SubCategoryComic, default=None, on_delete=models.CASCADE, blank=True, null=True)
    comics = models.CharField(max_length=1000)

    def __str__(self):
        return self.post.name
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
    name = models.CharField(max_length=100)
    poster = models.CharField(max_length=2000)
    imdb_rating = models.CharField(max_length=100)
    rotten_rating = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)

    def __str__(self):
        return self.name

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
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    poster = models.CharField(max_length=1000)
    cast = models.CharField(max_length=300)
    description = models.TextField()   
    release = models.CharField(max_length=100)
    imdb_rating = models.CharField(max_length=11)
    rotten_rating = models.CharField(max_length=11)
    num_season = models.CharField(max_length=11)

    def __str__(self):
        return self.title
    
class Season(models.Model):
    tag_series = models.ForeignKey(Series, default=None, on_delete=models.CASCADE, blank=True, null=True)
    season = models.IntegerField()

    def __str__(self):
        return self.tag_series.name

class Episode(models.Model):
    tag_season = models.ForeignKey(Season, default=None, on_delete=models.CASCADE, blank=True, null=True)
    episode = models.IntegerField()
    tmdb_id = models.IntegerField()
    season = models.IntegerField()
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=1000)
    videos = models.CharField(max_length=1000) 
    
    def __str__(self):
        return self.title

# ========================================================================================================================

# Shop
class Shop(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100)
    cover = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
    
class DetailShop(models.Model):
    items = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100)
    photos = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
# ========================================================================================================================

# Marvel Character
class MarvelHeroes(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    images = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class MarvelVillain(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    images = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class DetailHeroes(models.Model):
    char_heroes = models.ForeignKey(MarvelHeroes, default=None, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    story = models.TextField()
    multiverse = models.CharField(max_length=100)
    images = models.CharField(max_length=1000)

    def __str__(self):
        return self.char_heroes.name
    
class DetailVillain(models.Model):
    char_villain = models.ForeignKey(MarvelVillain, default=None, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    story = models.TextField()
    multiverse = models.CharField(max_length=100)
    images = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.char_villain.name
# ====================================================================================================================
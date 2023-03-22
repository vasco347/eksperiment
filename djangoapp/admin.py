from django.contrib import admin
from . models import CategoryComic, SubCategoryComic, DetailComic
from . models import CategoryMovie, SubCategoryMovie, DetailMovie
from . models import Series, Season, Episode
from . models import Shop, DetailShop
from . models import MarvelHeroes, MarvelVillain, DetailHeroes, DetailVillain
# Register your models here.


# Comics
class CategoryComicAdmin(admin.StackedInline):
    model = CategoryComic

class SubCategoryComicAdmin(admin.StackedInline):
    model = SubCategoryComic

class DetailComicAdmin(admin.StackedInline):
    model = DetailComic

@admin.register(SubCategoryComic)
class SubCategoryComicAdmin(admin.ModelAdmin):
    inlines = [DetailComicAdmin]

    class Meta:
       model = SubCategoryComic

@admin.register(DetailComic)
class DetailComicAdmin(admin.ModelAdmin):
    pass
@admin.register(CategoryComic)
class CategoryComicAdmin(admin.ModelAdmin):
    pass
# ===================================================================================================================

# Movies
class CategoryMovieAdmin(admin.StackedInline):
    model = CategoryMovie

class SubCategoryMovieAdmin(admin.StackedInline):
    model = SubCategoryMovie

class DetailMovieAdmin(admin.StackedInline):
    model = DetailMovie

@admin.register(SubCategoryMovie)
class SubCategoryMovieAdmin(admin.ModelAdmin):
    inlines = [DetailMovieAdmin]

    class Meta:
       model = SubCategoryMovie

@admin.register(DetailMovie)
class DetailMovieAdmin(admin.ModelAdmin):
    pass
@admin.register(CategoryMovie)
class CategoryMovieAdmin(admin.ModelAdmin):
    pass
# =====================================================================

# Series
class SeriesAdmin(admin.StackedInline):
    model = Series

class SeasonAdmin(admin.StackedInline):
    model = Season

class EpisodeAdmin(admin.StackedInline):
    model = Episode

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    inlines = [EpisodeAdmin]

    class Meta:
       model = Season

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    pass
@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass
# ======================================================================

# Shop
class ShopAdmin(admin.StackedInline):
    model = Shop

class DetailShopAdmin(admin.StackedInline):
    model = DetailShop

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = [DetailShopAdmin]

    class Meta:
       model = Shop

@admin.register(DetailShop)
class DetailShopAdmin(admin.ModelAdmin):
    pass
# =======================================================================

# Marvel Character
class MarvelVillainAdmin(admin.StackedInline):
    model = MarvelVillain

class DetailVillainAdmin(admin.StackedInline):
    model = DetailVillain

@admin.register(MarvelVillain)
class MarvelVillainAdmin(admin.ModelAdmin):
    inlines = [DetailVillainAdmin]

    class Meta:
       model = MarvelVillain

class MarvelHeroesAdmin(admin.StackedInline):
    model = MarvelHeroes

class DetailHeroesAdmin(admin.StackedInline):
    model = DetailHeroes

@admin.register(MarvelHeroes)
class MarvelHeroesAdmin(admin.ModelAdmin):
    inlines = [DetailHeroesAdmin]

    class Meta:
       model = MarvelHeroes

@admin.register(DetailHeroes)
class DetailHeroesAdmin(admin.ModelAdmin):
    pass

@admin.register(DetailVillain)
class DetailVillainAdmin(admin.ModelAdmin):
    pass
# ========================================================================
from django.contrib import admin
from . models import CategoryComic, SubCategoryComic, DetailComic
from . models import CategoryMovie, SubCategoryMovie, DetailMovie
from . models import CategorySeries, SubCategorySeries, DetailSeries
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
class CategorySeriesAdmin(admin.StackedInline):
    model = CategorySeries

class SubCategorySeriesAdmin(admin.StackedInline):
    model = SubCategorySeries

class DetailSeriesAdmin(admin.StackedInline):
    model = DetailSeries

@admin.register(SubCategorySeries)
class SubCategorySeriesAdmin(admin.ModelAdmin):
    inlines = [DetailSeriesAdmin]

    class Meta:
       model = SubCategorySeries

@admin.register(DetailSeries)
class DetailSeriesAdmin(admin.ModelAdmin):
    pass
@admin.register(CategorySeries)
class CategorySeriesAdmin(admin.ModelAdmin):
    pass
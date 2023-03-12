from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . models import CategoryComic, SubCategoryComic, DetailComic
from . models import CategoryMovie, SubCategoryMovie, DetailMovie
from . models import CategorySeries, SubCategorySeries, DetailSeries
from . models import CategoryShop, DetailShop
import random

def home(request):
    # Comic Views

    comic = [1, 2, 3, 4]
    comic_spiderman = SubCategoryComic.objects.filter(pk__in=comic)

    comic = [21, 22, 23, 24]
    comic_deadpool = SubCategoryComic.objects.filter(pk__in=comic)

    comic = [16, 17, 18, 19]
    comic_guardians = SubCategoryComic.objects.filter(pk__in=comic)


    # Shop Views
    marvel_shop = CategoryShop.objects.filter(parent=1)    
    
    return render(request, 'home.html', {'title':"Home", 'marvel_shop':marvel_shop, 'comic_spiderman':comic_spiderman, 'comic_deadpool':comic_deadpool, 'comic_guardians':comic_guardians})

def shop(request):
    marvel_shop = CategoryShop.objects.filter(parent=1) 
    return render(request, 'shop.html', {'title':"Shop", 'marvel_shop':marvel_shop})

def comic(request):
    SC = SubCategoryComic.objects.filter(child=2)
    FF = SubCategoryComic.objects.filter(child=4)
    LATPA = SubCategoryComic.objects.filter(child=1)
    MR = SubCategoryComic.objects.filter(child=6)
    DS = SubCategoryComic.objects.filter(child=7)
    DP = SubCategoryComic.objects.filter(child=3)
    GOTG = SubCategoryComic.objects.filter(child=5)

    items = [1, 2, 3, 4, 5]
    feature_comic = SubCategoryComic.objects.filter(pk__in=items)

    items = list(SubCategoryComic.objects.all())
    # change number to how many random items you want
    marvel_items = random.sample(items, 12)

    return render(request, 'comics.html', {'title':"Comics", 'SC':SC, 'LATPA':LATPA, 'FF':FF, 'MR':MR, 'DP':DP, 'DS':DS, 'GOTG':GOTG, 'feature_comic':feature_comic, 'marvel_items':marvel_items})

def movie(request):
    # Movie Views 
    AM = SubCategoryMovie.objects.filter(child=1)
    VU = SubCategoryMovie.objects.filter(child=2)

    # Series Views
    WV = SubCategorySeries.objects.filter(child=2)
    MM = SubCategorySeries.objects.filter(child=4)
    MK = SubCategorySeries.objects.filter(child=5)
    L = SubCategorySeries.objects.filter(child=1)
    H = SubCategorySeries.objects.filter(child=6)
    WI = SubCategorySeries.objects.filter(child=3)
    JJ = SubCategorySeries.objects.filter(child=7)
    IF = SubCategorySeries.objects.filter(child=8)
    

    # All Marvel Movies
    marvel_movies = SubCategoryMovie.objects.all()

    # Latest Marvel Movies
    videos = (4, 5, 8, 2)
    latest_movies = SubCategoryMovie.objects.filter(pk__in=videos)

    return render(request, 'movies.html', {'title':"Movies", 'AM':AM, 'VU':VU, 'WV':WV, 'MM':MM, 'JJ':JJ, 'MK':MK, 'IF':IF, 'WI':WI, 'L':L, 'H':H, 'latest_movies':latest_movies, 'marvel_movies':marvel_movies})

def detail_comics(request, id):
    # Random Comics Views
    items = list(SubCategoryComic.objects.all())
    # change 3 to how many random items you want
    random_items = random.sample(items, 8)

    post = get_object_or_404(SubCategoryComic, id=id)
    detail_comics = DetailComic.objects.filter(post=post)

    return render(request, 'detail_comic.html', {'title':"Comic", 'post':post, 'detail_comics':detail_comics, 'random_items':random_items})

def detail_movies(request, id):
    upload = get_object_or_404(SubCategoryMovie, id=id)
    detail_movies = DetailMovie.objects.filter(upload=upload)
    
    # Random Movies Views
    items = list(SubCategoryMovie.objects.all())
    # change 3 to how many random items you want
    more_movies = random.sample(items, 8)
    
    return render(request, 'detail_movie.html', {'title':"Movie", 'upload':upload, 'detail_movies':detail_movies, 'more_movies':more_movies})

def detail_series(request, id):
    uploads = get_object_or_404(SubCategorySeries, id=id)
    detail_series = DetailSeries.objects.filter(uploads=uploads)

    # Random Movies Views
    items = list(CategorySeries.objects.all())
    # change 3 to how many random items you want
    more_series = random.sample(items, 8)
    
    return render(request, 'detail_series.html', {'title':"Series", 'uploads':uploads, 'detail_series':detail_series, 'more_series':more_series})


def detail_shops(request, id):
    add = get_object_or_404(CategoryShop, id=id)
    detail_movies = DetailShop.objects.filter(add=add)

    items = list(CategoryShop.objects.all())
    # change 3 to how many random items you want
    random_items = random.sample(items, 5)

    items = list(CategoryShop.objects.all())
    # change 3 to how many random items you want
    random_items1 = random.sample(items, 5)
    return render(request, 'detail_shop.html', {'title':"Shop", 'add':add, 'detail_movies':detail_movies, 'items':items, 'random_items':random_items, 'random_items1':random_items1})


def about(request):
    return render(request, "about.html",{'title' : "About"})

def admin(request):
    return render(request, "error.html")
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . models import CategoryComic, SubCategoryComic, DetailComic
from . models import CategoryMovie, SubCategoryMovie, DetailMovie
from . models import Series, Season, Episode
from . models import Shop, DetailShop
from . models import MarvelHeroes, MarvelVillain, DetailHeroes, DetailVillain
import random

def home(request):
    # Comic Views

    comic = [1, 2, 3, 4, 5]
    comic_spiderman = SubCategoryComic.objects.filter(pk__in=comic)

    comic = [21, 22, 23, 24, 25]
    comic_deadpool = SubCategoryComic.objects.filter(pk__in=comic)

    comic = [16, 17, 18, 19, 20]
    comic_guardians = SubCategoryComic.objects.filter(pk__in=comic)   
    
    shop = list(Shop.objects.all())
    random_shop = random.sample(shop, 12)

    # All Marvel Heroes
    marvel_heroes = MarvelHeroes.objects.all()
    
    # All Marvel Villain
    marvel_villain = MarvelVillain.objects.all()

    return render(request, 'home.html', {'title':"Home", 'marvel_heroes':marvel_heroes, 'marvel_villain':marvel_villain, 'random_shop':random_shop, 'comic_spiderman':comic_spiderman, 'comic_deadpool':comic_deadpool, 'comic_guardians':comic_guardians})

def shop(request):

    shop_1 = Shop.objects.all().order_by('id')[0:12]
    shop_2 = Shop.objects.all().order_by('id')[12:20]

    return render(request, 'shop.html', {'title':"Shop", 'shop_1':shop_1, 'shop_2':shop_2})

def comic(request):
    SC = SubCategoryComic.objects.filter(child=2)
    FF = SubCategoryComic.objects.filter(child=4)
    LATPA = SubCategoryComic.objects.filter(child=1)
    MR = SubCategoryComic.objects.filter(child=6)
    DS = SubCategoryComic.objects.filter(child=7)
    DP = SubCategoryComic.objects.filter(child=3)
    GOTG = SubCategoryComic.objects.filter(child=5)

    items = [1, 6, 11, 16, 21]
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
    marvel_series = Series.objects.all()

    # All Marvel Heroes
    marvel_movies = SubCategoryMovie.objects.all()

    # Latest Marvel Movies
    videos = (3, 6, 8, 10)
    latest_movies = SubCategoryMovie.objects.filter(pk__in=videos)

    return render(request, 'movies.html', {'title':"Movies", 'marvel_movies':marvel_movies, 'marvel_series':marvel_series, 'latest_movies':latest_movies})

def character(request):
    
    # All Marvel Heroes
    marvel_heroes = MarvelHeroes.objects.all()
    
    # All Marvel Villain
    marvel_villain = MarvelVillain.objects.all()

    return render(request, 'char.html', {'title':"Characters", 'marvel_heroes':marvel_heroes, 'marvel_villain':marvel_villain})

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

def series(request, id):

    series = get_object_or_404(Series, id=id)

    season = Season.objects.filter(series=series)
    episode = Episode.objects.filter(season__in=season)

    items = list(Series.objects.all())
    # change 3 to how many random items you want
    more_series = random.sample(items, 8)

    return render(request, 'series.html', {'title':"Series", 'series':series, 'more_series':more_series, 'season':season, 'episode':episode})

def detail_series(request, id):

    uploads = get_object_or_404(Episode, id=id)

    items = list(Series.objects.all())
    # change 3 to how many random items you want
    more_series = random.sample(items, 8)

    return render(request, 'detail_series.html', {'title':"Episode", 'uploads':uploads, 'more_series':more_series })

def detail_shops(request, id):

    items = get_object_or_404(Shop, id=id)
    detail_shop = DetailShop.objects.filter(items=items)

    shop = list(Shop.objects.all())
    random_shop = random.sample(shop, 8) 

    return render(request, 'detail_shop.html', {'title':"Shop", 'items':items, 'random_shop':random_shop, 'detail_shop':detail_shop})

def detail_heroes(request, id):

    items = get_object_or_404(MarvelHeroes, id=id)
    detail_heroes = DetailHeroes.objects.filter(char_heroes=items)

    return render(request, 'detail_heroes.html', {'title':"Marvel Characters",  'char_heroes':items, 'detail_heroes':detail_heroes})

def detail_villain(request, id):

    items = get_object_or_404(MarvelVillain, id=id)
    detail_villain = DetailVillain.objects.filter(char_villain=items)

    return render(request, 'detail_villain.html', {'title':"Marvel Characters", 'char_villain':items, 'detail_villain':detail_villain})


def about(request):
    return render(request, "about.html",{'title' : "About"})

def admin(request):
    return render(request, "error.html")
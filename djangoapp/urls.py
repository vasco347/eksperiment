from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("", views.home, name="home"),

    path('comics/<title>', views.detail_comics, name='detail-comics'),
    path('films/movies/<title>', views.detail_movies, name='detail-movies'),
    path('shop/<title>', views.detail_shops, name='detail-shops'),
    path('films/series/<title>', views.series, name='series'),
    path('films/series/<id>/<tmdb_id>/season/<season>/episode/<episode>', views.detail_series, name='detail-series'),
    path('character/heroes/<title>', views.detail_heroes, name='detail-heroes'),
    path('character/villain/<title>', views.detail_villain, name='detail-villain'),

    path("comics/", views.comic, name="comics"),
    path("characters/", views.character, name="characters"),
    path("films/", views.movie, name="films"),
    path("shop/", views.shop, name="shop"),
    path("about/", views.about, name="about"),
    
]
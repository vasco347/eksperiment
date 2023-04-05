from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("", views.home, name="home"),

    path('comic/<title>', views.detail_comics, name='detail-comics'),
    path('film/movie/<title>', views.detail_movies, name='detail-movies'),
    path('shop/<title>', views.detail_shops, name='detail-shops'),
    path('film/series/<title>', views.series, name='series'),
    path('film/series/<season>/<title>', views.detail_series, name='detail-series'),
    path('character/heroes/<title>', views.detail_heroes, name='detail-heroes'),
    path('character/villain/<title>', views.detail_villain, name='detail-villain'),

    path("comic/", views.comic, name="comic"),
    path("character/", views.character, name="character"),
    path("film/", views.movie, name="movie"),
    path("shop/", views.shop, name="shop"),
    path("about/", views.about, name="about"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
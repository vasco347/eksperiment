from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("", views.home, name="home"),
    path("admin/", views.admin, name="admin"),

    path('detail-comic/<int:id>', views.detail_comics, name='detail-comics'),
    path('detail-movie/<int:id>', views.detail_movies, name='detail-movies'),
    path('detail-series/<int:id>', views.detail_series, name='detail-series'),
    path('detail-shop/<int:id>', views.detail_shops, name='detail-shops'),
    path('detail-characters/heroes/<int:id>', views.detail_heroes, name='detail-heroes'),
    path('detail-characters/villain/<int:id>', views.detail_villain, name='detail-villain'),

    path("comic/", views.comic, name="comic"),
    path("character/", views.character, name="character"),
    path("movie/", views.movie, name="movie"),
    path("shop/", views.shop, name="shop"),
    path("about/", views.about, name="about"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
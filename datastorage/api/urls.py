from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comments', views.comment_endpoint, name='comment_endpoint'),
    path('comment/<id>', views.retrieve_comment, name='retrieve_comment'),
    path('favsongs', views.create_favsongs_endpoint, name='create_favsongs_endpoint'),
    path('products', views.product_api_call, name='product_api_call'),
    # path('product/<id>', views.retrieve_product, name='retrieve_product'),
    path('api/songs', views.song_api_call, name='song_api_call'),
    path('movies', views.movie_api_call, name='movie_api_call'),
    path('product/<id>', views.rud_product, name='rud_product'),
]

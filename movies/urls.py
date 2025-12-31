from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('add-movie/', views.add_movie, name='add_movie'),
    path('movie-details/<int:movie_id>/',views.movie_details,name='movie_details'),
    path('edit-movie/<int:movie_id>/',views.edit_movie,name='edit_movie'),
    path('delete-movie/<int:movie_id>/',views.delete_movie,name='delete_movie'),
    path('add-actor/',views.add_actors,name='add_actors'),
    path('actors/', views.actors_list, name='actors_list'),
    path('actor-details/<int:actor_id>/', views.actor_details, name='actor_details'),
    path('edit-actor/<int:actor_id>/',views.edit_actor,name='edit_actor'),
    path('delete-actor/<int:actor_id>/',views.delete_actor,name='delete_actor'),
    path('people/', views.people_list, name='people_list'),
    path('person/<int:person_id>/', views.person_details, name='person_details'),

]
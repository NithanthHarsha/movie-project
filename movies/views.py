from django.shortcuts import render,redirect
from .models import Movie
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from . models import Person ,MovieCredit,Movie
from datetime import date


# Create your views here.
def home(request):
    query = request.GET.get('q')
    if query:
         movies = Movie.objects.filter(
            name__icontains=query
         )
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'movies':movies,'query':query} )

@login_required(login_url='login_user')
def add_movie(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to add a movie.")

    if request.method == "POST":
        name = request.POST.get('name')
        year = request.POST.get('year')
        description = request.POST.get('description')
        genre = request.POST.get('genre')
        cover = request.FILES.get('cover')
        trailer = request.POST.get('trailer')  

        movie = Movie(
            name=name,
            year=year,
            genre=genre,
            cover=cover,
            description=description,
            trailer=trailer
        )
        movie.save()

        return redirect('movie_details', movie_id=movie.id)

    return render(request, 'add-movies.html')


@login_required(login_url='login_user')
def movie_details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    cast = movie.credits.filter(role='Actor')
    directors = movie.credits.filter(role='Director')
    writers = movie.credits.filter(role='Writer')
    producers = movie.credits.filter(role='Producer')

    context = {
        'movie': movie,
        'cast': cast,
        'directors': directors,
        'writers': writers,
        'producers': producers,
    }
    return render(request, 'movie-details.html', context)



@login_required(login_url='login_user')
def edit_movie(request,movie_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to edit a movie.")
    movie = Movie.objects.get(id=movie_id)

    if request.method == 'POST':
        movie.name = request.POST.get('name')
        movie.year = request.POST.get('year')
        movie.genre = request.POST.get('genre')
        movie.description = request.POST.get('description')
        movie.trailer = request.POST.get('trailer')

        if request.FILES.get('cover'):
            movie.cover = request.FILES.get('cover')

        movie.save()
        return redirect('movie_details', movie_id=movie.id)

    return render(request, 'edit-movie.html', {'movie': movie})


@login_required(login_url='login_user')
def delete_movie(request,movie_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to delete a movie.")
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect('home')


@login_required(login_url='login_user')
def add_actors(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to add an actor.")

    if request.method == "POST":
        actor = Person(
            name=request.POST.get("name"),
            date_of_birth=request.POST.get("date_of_birth"),
            bio=request.POST.get("bio"),
            photo=request.FILES.get("photo"),
        )
        actor.save()

        messages.success(request, "Actor added successfully.")
        return redirect('actor_details', actor_id=actor.id)

    return render(request, "add-actors.html")


@login_required(login_url='login_user')
def actors_list(request):
    actors=Person.objects.all()
    return render(request,"actors-list.html",{"actors":actors})

@login_required(login_url='login_user')
def actor_details(request, actor_id):
    actor = Person.objects.get(id=actor_id)
    return render(request, "actor-details.html", {"actor": actor})


@login_required(login_url='login_user')
def edit_actor(request, actor_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to edit an actor.")

    actor = Person.objects.get(id=actor_id)

    if request.method == "POST":
        actor.name = request.POST.get("name")
        actor.date_of_birth = request.POST.get("date_of_birth")
        actor.bio = request.POST.get("bio")

        if request.FILES.get("photo"):
            actor.photo = request.FILES.get("photo")

        actor.save()
        return redirect('actor_details', actor_id=actor.id)

    return render(request, "edit-actors.html", {"actor": actor})

@login_required(login_url='login_user')
def delete_actor(request,actor_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to delete an actor.")
    actor=Person.objects.get(id=actor_id)
    actor.delete()
    messages.success(request,"Actor deleted successfully.")
    return redirect('actors_list')



def people_list(request):
    people = Person.objects.all()
    return render(request, 'people-list.html', {'people': people})



def person_details(request, person_id):
    person = Person.objects.get(id=person_id)
    credits = MovieCredit.objects.filter(person=person)

    return render(request, 'person-details.html', {
        'person': person,
        'credits': credits
    })






    
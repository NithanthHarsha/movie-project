from django.contrib import admin
from .models import Person, Movie, MovieCredit


# Person admin
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth')
    search_fields = ('name',)


# Inline for MovieCredit (Cast / Crew)
class MovieCreditInline(admin.TabularInline):
    model = MovieCredit
    extra = 1


# Movie admin with inline credits
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'genre')
    search_fields = ('name',)
    inlines = [MovieCreditInline]


# Optional: Register MovieCredit separately
@admin.register(MovieCredit)
class MovieCreditAdmin(admin.ModelAdmin):
    list_display = ('movie', 'person', 'role', 'character_name')
    list_filter = ('role',)

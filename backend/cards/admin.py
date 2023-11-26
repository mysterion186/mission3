"""Admin setup for cards app."""
from django.contrib import admin

from .models import Flashcard, Deck, Theme

admin.site.register(Flashcard)
admin.site.register(Theme)
admin.site.register(Deck)

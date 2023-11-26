"""urls conf for the cards app."""
from django.urls import path

from . import views

app_name = 'cards'

urlpatterns = [
    path("flashcard/list", view=views.FlashcardListView.as_view(), name="flashcard_list"),
    path("flashcard/create", view=views.FlashcardCreateView.as_view(), name="flashcard_create"),
    path("deck/list", view=views.DeckListView.as_view(), name="deck_list"),
    path("deck/create", view=views.DeckCreateView.as_view(), name="deck_create"),
    path("deck/<int:pk>", view=views.DeckDisplayView.as_view(), name="deck"),
    path("theme/list", view=views.ThemeListView.as_view(), name="theme_list"),
]

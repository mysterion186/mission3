"""Views for the cards app."""
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from . import models
from . import serialiazers
class FlashcardListView(ListAPIView):
    """View for listing all existing Flashcards"""
    serializer_class = serialiazers.FlashcardSerializer
    queryset = models.Flashcard.objects.all()
    permission_classes = [AllowAny]

class DeckListView(ListAPIView):
    """View for listing all Decks."""
    serializer_class = serialiazers.DeckSerializer
    queryset = models.Deck.objects.all()
    permission_classes = [AllowAny]

class ThemeListView(ListAPIView):
    """View for listing all the Theme."""
    serializer_class = serialiazers.ThemeSerializer
    queryset = models.Theme.objects.all()
    permission_classes = [AllowAny]

class DeckCreateView(CreateAPIView):
    """Create a Deck."""
    serializer_class = serialiazers.DeckSerializer
    permission_classes = [IsAuthenticated]

"""Serializer related to the cards application."""
from rest_framework import serializers

from accounts.models import MyUser
from .models import Flashcard, Deck, Theme

class ThemeSerializer(serializers.ModelSerializer):
    """Serializer for the Theme model."""
    class Meta:
        """Default meta class."""
        model = Theme
        fields = ["id", "theme"]

class DeckSerializer(serializers.ModelSerializer):
    """Serializer for the Deck model."""
    user_email = serializers.SerializerMethodField()
    class Meta:
        """Default meta class."""
        model = Deck
        fields = ["id", "owner", "user_email", "theme", "name"]

    def get_user_email(self, obj):
        """Return the user's email."""
        user = obj.owner
        return user.email

class FlashcardSerializer(serializers.ModelSerializer):
    """Serializer for the Flashcard model."""
    deck_name = serializers.SerializerMethodField()
    class Meta:
        """Default meta class."""
        model = Flashcard
        fields = ["deck", "deck_name", "question", "answer", "position"]

    def get_deck_name(self, obj):
        """Return the name of the Deck."""
        deck = obj.deck
        return deck.name

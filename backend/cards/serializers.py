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
        if isinstance(obj, dict):
            deck = obj.get("deck")
            if deck:
                return deck.name
        deck = obj.deck
        return deck.name

class DeckDisplaySerializer(serializers.ModelSerializer):
    """Serializer that will display all the Flashcard for a selected Deck."""
    flashcards = serializers.SerializerMethodField()

    class Meta:
        """Default class meta."""
        model = Deck
        fields = ['owner', 'theme', 'name', 'flashcards']

    def get_flashcards(self, obj):
        """Retrieve all flashcard for the specific deck."""
        flashcards = Flashcard.objects.filter(deck=obj)
        serializer = FlashcardSerializer(flashcards, many=True)
        return serializer.data

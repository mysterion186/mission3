"""Models for the cards application."""
from django.db import models
from django.core.validators import MinValueValidator

from accounts.models import MyUser

class Theme(models.Model):
    """This model represents a theme for a Decks."""
    theme = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.theme

class Deck(models.Model):
    """This model represents a Deck. It will contains a set of Flashcards."""
    owner = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    name = models.CharField(max_length=250) # name of the deck

    def __str__(self) -> str:
        return str(self.owner) + " | " + self.name

class Flashcard(models.Model):
    """This model represents a Flashcard. It will contains."""
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=500)
    position = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )

    def __str__(self) -> str:
        return str(self.deck) + " | " + str(self.position)

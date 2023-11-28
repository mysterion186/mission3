"""Views for the cards app."""
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView
)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from . import models
from . import serializers
from .permissions import IsDeckOwner

class FlashcardListView(ListAPIView):
    """View for listing all existing Flashcards"""
    serializer_class = serializers.FlashcardSerializer
    queryset = models.Flashcard.objects.all()
    permission_classes = [AllowAny]

class FlashcardCreateView(APIView):
    """View for creating flashcard (one or many)."""
    permission_classes = [IsDeckOwner]

    def post(self, request):
        """Handle Flashcard creation."""
        data = request.data
        if isinstance(data, list):
            response_list = []
            for elt in data:
                serializer = serializers.FlashcardSerializer(data=elt)
                if serializer.is_valid() :
                    serializer.save()
                    response_list.append(serializer.data)
                else:
                    return Response(
                        {
                            "error": serializer.errors,
                            "done" : response_list
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
            return Response(
                {
                    "success": response_list
                },
                status=status.HTTP_201_CREATED
            )
        if isinstance(data, dict):
            serializer = serializers.FlashcardSerializer(data=data)
            if serializer.is_valid():
                return Response({"success": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {"error":"Data format is not recognized"},
            status=status.HTTP_400_BAD_REQUEST
        )

class ThemeListView(ListAPIView):
    """View for listing all the Theme."""
    serializer_class = serializers.ThemeSerializer
    queryset = models.Theme.objects.all()
    permission_classes = [AllowAny]

class DeckListView(ListAPIView):
    """View for listing all Decks."""
    serializer_class = serializers.DeckSerializer
    queryset = models.Deck.objects.all()
    permission_classes = [AllowAny]

class DeckDisplayView(RetrieveAPIView):
    """View for getting all Flashcard for a specific Deck (based on id)."""
    serializer_class = serializers.DeckDisplaySerializer
    permission_classes = [AllowAny]

    def get_object(self):
        pk = self.kwargs.get('pk')
        try:
            return models.Deck.objects.get(pk=pk)
        except models.Deck.DoesNotExist:
            return None

    def retrieve(self, request, *args, **kwargs):
        """Override the method to display an error if the Deck does not exist."""
        instance = self.get_object()
        if not instance:
            return Response(
                {"error": "Deck does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class DeckCreateView(CreateAPIView):
    """Create a Deck."""
    serializer_class = serializers.DeckSerializer
    permission_classes = [IsAuthenticated]

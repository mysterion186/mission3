from rest_framework import permissions

from .models import Flashcard, Deck

class IsDeckOwner(permissions.BasePermission):
    """Check that the user is the Deck owner."""

    def has_permission(self, request, view, obj=None):
        """Check if the deck belongs to the user.

        If the obj is a Deck, we can directly check if the user is the Deck owner.

        In the case, we don't have this information, we look into the request
        for the deck in order to find the deck_id. Based on the owner we allow or not
        the permissions. If the deck does not exist, we don't allow the request.
        """
        if isinstance(obj, Deck):
            return obj.owner == request.user
        if request.method == "POST":
            # check data type
            if isinstance(request.data, list):
                has_perm = False
                for elt in request.data:
                    deck_id = elt.get("deck", None)
                    if deck_id:
                        try:
                            deck = Deck.objects.get(pk=deck_id)
                            has_perm = deck.owner == request.user
                        except Deck.DoesNotExist:
                            has_perm = False
                return has_perm
            if isinstance(request.data, dict):
                # check the deck id
                deck_id = request.data.get("deck", None)
                if not deck_id:
                    return False
                try:
                    deck = Deck.objects.get(pk=deck_id)
                    return deck.owner == request.user
                except Deck.DoesNotExist:
                    return False
        return False

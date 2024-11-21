from typing import List


class Service:
    """Represents a transportation service."""

    def __init__(self, name: str, departure_date: datetime.date):
        self.name = name
        self.departure_date = departure_date
        self._legs: List[Leg] = []  # Private list of legs
        self.ods: List[OD] = []

    # Property for legs with validation
    @property
    def legs(self) -> List["Leg"]:
        """Getter for legs."""
        return self._legs

    @legs.setter
    def legs(self, new_legs: List["Leg"]):
        """Setter for legs with validation."""
        validate_legs(new_legs)
        self._legs = new_legs
        self.update_itinerary()

    def add_leg(self, leg: "Leg"):
        """Add a leg with validation."""
        self.legs = self._legs + [leg]

    def remove_leg(self, leg: "Leg"):
        """Remove a leg with validation."""
        if leg not in self._legs:
            raise ValueError(f"Leg {leg} does not exist in the service.")
        self.legs = [l for l in self._legs if l != leg]

    def clear_legs(self):
        """Clear all legs."""
        self.legs = []

    # Property for itinerary (computed from legs)
    @property
    def itinerary(self) -> List["Station"]:
        """Computes the ordered list of stations based on legs."""
        if not self._legs:
            return []

        service_itinerary = []
        for leg in self._legs:
            if not service_itinerary or service_itinerary[-1] != leg.origin:
                service_itinerary.append(leg.origin)
            service_itinerary.append(leg.destination)
        return service_itinerary

    def update_itinerary(self):
        """Rebuild ODs when the legs change."""
        self.ods = []
        for i in range(len(self.itinerary) - 1):
            for j in range(i + 1):
                self.ods.append(OD(self, self.itinerary[j], self.itinerary[i + 1]))

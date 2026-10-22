from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Room:
    room_id: str
    capacity: int


@dataclass
class Booking:
    booking_id: int
    room_id: str
    booking_date: date
    guest_name: str
    guest_count: int


class RoomBookingService:
    def __init__(self, rooms: list[Room]):
        self._rooms = {room.room_id: room for room in rooms}
        self._bookings: list[Booking] = []
        self._next_booking_id = 1

    def get_available_rooms(self, booking_date: date, guest_count: int) -> list[Room]:
        # Return rooms with enough capacity that are not booked on this date.
        raise NotImplementedError

    def create_booking(
        self,
        room_id: str,
        booking_date: date,
        guest_name: str,
        guest_count: int,
    ) -> Booking:
        # Validate the request, create a booking, store it, and return it.
        raise NotImplementedError

    def cancel_booking(self, booking_id: int) -> None:
        # Remove the matching booking or raise ValueError if it does not exist.
        raise NotImplementedError
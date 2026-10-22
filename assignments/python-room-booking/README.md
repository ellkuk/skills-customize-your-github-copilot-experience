# 📘 Assignment: Python Room Booking Service

## 🎯 Objective

Build an in-memory room booking service using Python classes and dataclasses. Practice applying clean code principles by giving each method a clear responsibility, using descriptive names, and reusing booking rules instead of duplicating them.

## 📝 Tasks

### 🛠️ Find Available Rooms

#### Description
Complete the room and booking service in the starter code. Implement the logic that finds rooms suitable for a requested date and number of guests.

#### Requirements
Completed program should:

- Represent each room with a room ID and guest capacity
- Represent each booking with its ID, room, date, guest name, and guest count
- Return rooms that have enough capacity and are not already booked for the requested date
- Reject a guest count less than one with a clear `ValueError`
- Keep availability checking separate from booking creation


### 🛠️ Create and Cancel Bookings

#### Description
Implement booking creation and cancellation. A room can have only one booking per date, and invalid requests should fail clearly without changing the stored bookings.

#### Requirements
Completed program should:

- Create a booking with a unique ID when the room is available and has enough capacity
- Reject unknown room IDs, blank guest names, insufficient capacity, and duplicate bookings with a clear `ValueError`
- Cancel a booking using its ID and reject IDs that do not exist
- Reuse the availability logic rather than duplicating its rules
- Use descriptive names and small methods with one clear responsibility
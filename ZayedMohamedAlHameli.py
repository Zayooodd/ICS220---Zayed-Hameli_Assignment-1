# This is a Guest class with 8 attributes
# The class has a getter and setter method for each attribute
class Guest:
    def __init__(self, guestID, name, email, phoneNumber, address, nationality, gender, age):
        self.guestID = guestID
        self.name = name
        self.email = email #guests email address
        self.phoneNumber = phoneNumber #the phone number
        self.address = address # the residental adress of the guest (where he lives)
        self.nationality = nationality #the nationality of the guest
        self.gender = gender #whats the gender (male)
        self.age = age #the age of the guest

    # These are the Getter and setter methods
    #method to get the guestid
    def get_guestID(self):
        return self.guestID
#method to set the guest ID
    def set_guestID(self, guestID):
        self.guestID = guestID
#Method to get the name
    def get_name(self):
        return self.name
#method to set the name
    def set_name(self, name):
        self.name = name
# method to get the email
    def get_email(self):
        return self.email
# method to set email
    def set_email(self, email):
        self.email = email
# this is a method to get the phone number
    def get_phoneNumber(self):
        return self.phoneNumber
# set the phone number
    def set_phoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber
# this gets address
    def get_address(self):
        return self.address
# method to set adress
    def set_address(self, address):
        self.address = address
# to get nationality
    def get_nationality(self):
        return self.nationality
# to set nationality
    def set_nationality(self, nationality):
        self.nationality = nationality
#method to get gender
    def get_gender(self):
        return self.gender
# method to set gender
    def set_gender(self, gender):
        self.gender = gender
#method to get age
    def get_age(self):
        return self.age
#method to set age
    def set_age(self, age):
        self.age = age

    # The print_info method displays all guest details
    # using ifelse in print_info to display information
    def print_info(self):
        age_status = "Adult" if self.age > 18 else "Minor"
        salutation = "Mr." if self.gender == "Male" else "Ms."
        print(f"Guest ID: {self.guestID}, Name: {salutation} {self.name}, Age Status: {age_status}")
        print(f"Email: {self.email}, Phone: {self.phoneNumber}, Address: {self.address}")


# Room class with 8 attributes which represents details in the hotel
#  The class includes getter and setter methods for each attribute like the one above and print_info
class Room: #the constructer initializes room attributes
    def __init__(self, roomID, roomType, price, availability, bedType, view, floor, capacity):
        self.roomID = roomID #this is a unique identifier for the room
        self.roomType = roomType # type of room
        self.price = price #price per night for room
        self.availability = availability # if its true then its available, (status of the room)
        self.bedType = bedType #type of bed in room (king)
        self.view = view  #view from the room
        self.floor = floor #floor number where the room is usually located
        self.capacity = capacity #maximum number of people the room can accommodate

    # These are the Getter and setter methods
    def get_roomID(self):
        return self.roomID

    def set_roomID(self, roomID):
        self.roomID = roomID

    def get_roomType(self):
        return self.roomType

    def set_roomType(self, roomType):
        self.roomType = roomType

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_availability(self):
        return self.availability

    def set_availability(self, availability):
        self.availability = availability

    def get_bedType(self):
        return self.bedType

    def set_bedType(self, bedType):
        self.bedType = bedType

    def get_view(self):
        return self.view

    def set_view(self, view):
        self.view = view

    def get_floor(self):
        return self.floor

    def set_floor(self, floor):
        self.floor = floor

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity

    #The print_info method shows information about the room, including availability
    def print_info(self):
        availability_status = "Available" if self.availability else "Not Available" #checks if room is available
        print(f"Room ID: {self.roomID}, Type: {self.roomType}, Price: {self.price}")
        print(f"Availability: {availability_status}, Bed Type: {self.bedType}, View: {self.view}")


# Reservation class that links a guest and a room
# the class includes getter and setter methods for each attribute like the above classes and a print_info
class Reservation: # this sets a class reservation
    def __init__(self, reservationID, guest, room, checkInDate, checkOutDate, status, totalPrice, paymentStatus): #def __init__ function is used
        self.reservationID = reservationID #this is the resevation ID
        self.guest = guest  #guest object is linked to this reservation
        self.room = room    #room object linked
        self.checkInDate = checkInDate #check in date
        self.checkOutDate = checkOutDate # Check in date
        self.status = status #status of the reservation
        self.totalPrice = totalPrice #total price for the entire day
        self.paymentStatus = paymentStatus #payment status

    # Getter and setter methods for each
    def get_reservationID(self):
        return self.reservationID

    def set_reservationID(self, reservationID):
        self.reservationID = reservationID

    def get_guest(self):
        return self.guest

    def set_guest(self, guest):
        self.guest = guest

    def get_room(self):
        return self.room

    def set_room(self, room):
        self.room = room

    def get_checkInDate(self):
        return self.checkInDate

    def set_checkInDate(self, checkInDate):
        self.checkInDate = checkInDate

    def get_checkOutDate(self):
        return self.checkOutDate

    def set_checkOutDate(self, checkOutDate):
        self.checkOutDate = checkOutDate

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_totalPrice(self):
        return self.totalPrice

    def set_totalPrice(self, totalPrice):
        self.totalPrice = totalPrice

    def get_paymentStatus(self):
        return self.paymentStatus

    def set_paymentStatus(self, paymentStatus):
        self.paymentStatus = paymentStatus

    ##The print_info method displays reservation details (including guest&room&reservation status
    def print_info(self):
        status_message = "Reservation is confirmed." if self.status == "Confirmed" else "Reservation is pending."
        print(f"Reservation ID: {self.reservationID}, Guest ID: {self.guest.get_guestID()}, Room ID: {self.room.get_roomID()}")
        print(f"Check-In: {self.checkInDate}, Check-Out: {self.checkOutDate}")
        print(status_message)


# payment class with 8 attributes

class Payment: #sets class payment
    def __init__(self, paymentID, reservation, amount, method, status, date, transactionID): #def  __init__ function is used
        self.paymentID = paymentID #unique identifier for payment
        self.reservation = reservation  #reference to Reservation object
        self.amount = amount #total amount of payment
        self.method = method #payment method
        self.status = status #status of payment
        self.date = date #date of payment
        self.transactionID = transactionID #transaction ID for payment

    # Getter and setter methods
    def get_paymentID(self):
        return self.paymentID

    def set_paymentID(self, paymentID):
        self.paymentID = paymentID

    def get_reservation(self):
        return self.reservation

    def set_reservation(self, reservation):
        self.reservation = reservation

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_method(self):
        return self.method

    def set_method(self, method):
        self.method = method

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_transactionID(self):
        return self.transactionID

    def set_transactionID(self, transactionID):
        self.transactionID = transactionID

    # using print_info to show payment status
    def print_info(self):
        payment_status = "Payment Accepted" if self.status == "Accepted" else "Payment Pending"
        print(f"Payment ID: {self.paymentID}, Reservation ID: {self.reservation.get_reservationID()}, Amount: {self.amount}")
        print(f"Method: {self.method}, Status: {payment_status}, Date: {self.date}")


#hotel class to manage rooms and reservations
class Hotel:
    def __init__(self, hotelID, name, address, rooms, reservations, totalRooms, availableRooms, rating): #the __innit function is used
        self.hotelID = hotelID #identifier for the hotel
        self.name = name # the name of hotel
        self.address = address #physical address of hotel
        self.rooms = rooms  # list of Room objects in hotel
        self.reservations = reservations  # list of Reservation objects
        self.totalRooms = totalRooms #total number of rooms
        self.availableRooms = availableRooms #number of rooms available
        self.rating = rating #the rating of hotel out of 5

    # Getter and setter methods
    def get_hotelID(self):
        return self.hotelID

    def set_hotelID(self, hotelID):
        self.hotelID = hotelID

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_rooms(self):
        return self.rooms

    def set_rooms(self, rooms):
        self.rooms = rooms

    def get_reservations(self):
        return self.reservations

    def set_reservations(self, reservations):
        self.reservations = reservations

    def get_totalRooms(self):
        return self.totalRooms

    def set_totalRooms(self, totalRooms):
        self.totalRooms = totalRooms

    def get_availableRooms(self):
        return self.availableRooms

    def set_availableRooms(self, availableRooms):
        self.availableRooms = availableRooms

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        self.rating = rating

    # Using if-else in print_info to display rating message
    def print_info(self):
        rating_message = "Highly rated" if self.rating >= 4.0 else "Moderately rated"
        print(f"Hotel ID: {self.hotelID}, Name: {self.name}, Address: {self.address}")
        print(f"Total Rooms: {self.totalRooms}, Available Rooms: {self.availableRooms}, Rating: {rating_message}")


# these are instances of each class

#a guest
guest1 = Guest("G001", "Saeed", "Saeedalhameli@gmail.com", "+971502124144", "Rabdan st, Abu Dhabi", "Emirati", "Male", 24)
guest1.print_info()

# a room
room1 = Room("R001", "Deluxe", 500, True, "King Bed", "Sea View", "23rd", 2)
room1.print_info()

# a reservation
reservation1 = Reservation("RESID212", guest1, room1, "2024-10-10", "2024-10-15", "Confirmed", 2500, "Paid")
reservation1.print_info()

#a payment
payment1 = Payment("PAY001", reservation1, 2500, "Credit Card", "Accepted", "2024-10-01", "TID121")
payment1.print_info()

#a hotel
hotel1 = Hotel("H001", "Rabdan Hotel", "Al Maqta Rd, Abu Dhabi", [room1], [reservation1], 100, 80, 4.5)
hotel1.print_info()

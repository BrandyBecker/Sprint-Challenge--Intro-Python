# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle():
    """Base Class"""
    pass

class FlightVehicle(Vehicle):
    """Stems from Vehicle Class"""
    pass

class Starship(FlightVehicle):
    """Stems From FlightVehicle which stems from Vehicle"""
    pass

class GroundVehicle(Vehicle):
    """Stems from Vehicle"""
    pass

class Car(GroundVehicle):
    '''Stems from Ground Vehicle, which stems from Vehicle'''
    pass


class Motorcycle(GroundVehicle):
    '''stems from Ground Vehicle, which stems from Vehicle'''
    pass


class Airplane(FlightVehicle):
    '''Stems from Flight Vehicle, which stems from vehicle'''
    pass
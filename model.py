"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730622857"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Calculate the distance bewteen self and another point."""
        distance_between: float = ((self.x - other.x)**2) + ((self.y - other.y)**2) 
        distance_between = sqrt(distance_between)
        return distance_between


class Cell:
    """An individual subject in the simulation."""
    
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.

    def tick(self) -> None:
        """Increments the time in the simulation and enables immunization."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True:
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
    
    def contract_disease(self) -> None:
        """Will cause a cell to become infected."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Will cause a cell to become vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Check a cell for infection."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def color(self) -> str:
        """Colors a cell based on its health, infection, or immunity."""
        if self.sickness == constants.VULNERABLE:
            return "gray"
        if self.is_immune():
            return "green"
        else:
            return "red"

    def contact_with(self, contact_cell: Cell) -> None:
        """Allow a cell to become infected with eachother."""
        if self.is_vulnerable() and contact_cell.is_infected():
            self.contract_disease()
        if contact_cell.is_vulnerable() and self.is_infected():
            contact_cell.contract_disease()

    def immunize(self) -> None:
        """Allow a cell to become immune."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Check a cell for immunity."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0
    infected_start: int = 1
    immune_start: int = 2

    def __init__(self, cells: int, speed: float, infected_start: int, immune_start: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected_start <= 0 or infected_start >= cells:
            raise ValueError("Your infection start count must be greater than 0 and less than the number of cells.")
        if immune_start < 0 or immune_start >= cells:
            raise ValueError("Your immune start count must be greater than 0 and less than the number of cells.")
        if Model.infected_start >= cells or Model.infected_start == 0:
            raise ValueError("You must start with at least one infected cell!")
        for _ in range(infected_start):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.contract_disease()
            self.population.append(cell)
        for _ in range(cells - infected_start):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for _ in range(immune_start):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.immunize()
            self.population.append(cell)    

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
        for cell in self.population:
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle * speed)
        direction_y: float = sin(random_angle * speed)
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
            
    def is_complete(self) -> bool:
        """Indicate when the simulation is complete."""
        for _ in range(len(self.population) -1):
            if self.population[_].is_vulnerable or self.population[_].is_immune:
                return False
        else:
            return True

    def check_contacts(self) -> None:
        """If a cell collides with another cell, it is detected and a method call to contact_with is made to change the sickness attribute."""
        for first_set in range(len(self.population)):
            for second_set in range(first_set + 1, len(self.population)):
                cell_distance = self.population[first_set].location.distance(self.population[second_set].location)
                if cell_distance < constants.CELL_RADIUS:
                    self.population[first_set].contact_with(self.population[second_set])
        return None

import abc
import enum


class Color(enum.Enum):
    RED = enum.auto()
    GREEN = enum.auto()
    BLUE = enum.auto()
    WHITE = enum.auto()


class DriveType(enum.Enum):
    FULL = enum.auto()
    BACK = enum.auto()
    FRONT = enum.auto()


class Car(abc.ABC):

    def __init__(
        self,
        color: Color,
        model: str,
        year: int,
        drive_type: DriveType,
    ) -> None:
        self.color = color
        self.model = model
        self.year = year
        self.drive_type = drive_type

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.model} {self.color} {self.year})'

    @abc.abstractmethod
    def fuel(self) -> None:
        pass


class PetrolCar(Car):

    def fuel(self) -> None:
        print(f"Fueled by petrol {self}")


class DieselCar(Car):

    def fuel(self) -> None:
        print(f"Fueled by diesel {self}")


class GasCar(Car):

    def fuel(self) -> None:
        print(f"Fueled by gas {self}")


class ElectroCar(Car):

    def fuel(self) -> None:
        print(f"Charged {self}")


class PetrolPrivateCar(PetrolCar):

    def pass_exam(self) -> None:
        print(f"Passed exam on petrol car for B1")


class PetrolTruck(PetrolCar):

    def pass_exam(self) -> None:
        print(f"Passed exam on petrol car for C1")


class PetrolBus(PetrolCar):

    def pass_exam(self) -> None:
        print(f"Passed exam on petrol car for D1")


class ElectroPrivateCar(PetrolCar):

    def pass_exam(self) -> None:
        print(f"Passed exam on electro car for B1")




class FuelPolicy(abc.ABC):

    @abc.abstractmethod
    def fuel(self):
        pass


class ElectricFuelPolicy(FuelPolicy):

    def fuel(self):
        print("Fueled by electric")


class PetrolFuelPolicy(FuelPolicy):

    def fuel(self):
        print("Fueled by petrol")


class GasFuelPolicy(FuelPolicy):

    def fuel(self):
        print("Fueled by gas")


class DieselFuelPolicy(FuelPolicy):

    def fuel(self):
        print("Fueled by diesel")



class TransportCategory(abc.ABC):

    @abc.abstractmethod
    def pass_exam(self):
        pass


class PrivateTransportCategory(TransportCategory):

    def pass_exam(self):
        print("Passed exam on B1")


class TruckTransportCategory(TransportCategory):

    def pass_exam(self):
        print("Passed exam on C1")


class BusTransportCategory(TransportCategory):

    def pass_exam(self):
        print("Passed exam on D1")



class Car(abc.ABC):

    def __init__(
        self,
        color: Color,
        model: str,
        year: int,
        drive_type: DriveType,
    ) -> None:
        self.color = color
        self.model = model
        self.year = year
        self.drive_type = drive_type

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.model} {self.color} {self.year})'


class ElectroBus(Car, ElectricFuelPolicy, BusTransportCategory):
    pass


class ElectroPrivateCar(Car, ElectricFuelPolicy, PrivateTransportCategory):
    pass


class ElectroTruck(Car, ElectricFuelPolicy, TruckTransportCategory):
    pass


class PetrolCar2(PetrolCar, PetrolFuelPolicy):

    def __init__(
        self,
        color: Color,
        model: str,
        year: int,
        drive_type: DriveType,
        displacement: int,
    ) -> None:
        super().__init__(color, model, year, drive_type)
        super(PetrolFuelPolicy, self).__init__()


        print(f"{super(PetrolFuelPolicy, self).__init__ = }")
        print(f"{super().fuel = }")

        #super().__init__()
        # Car.__init__(self, color, model, year, drive_type)
        self.displacement = displacement


bmw_x5 = PetrolCar2(Color.GREEN, "X5", 2019, DriveType.FULL, 4.4)
# print(f"{bmw_x5.color = }, {bmw_x5.model = }")

# Method resolution order
print(f"{PetrolCar2.mro() = }")

exit()






class Plane:
    """
    Implements IVehicle interface.

    attrs: model, year
    methods: fuel()
    """

    def __init__(self, model: str, year: int) -> None:
        self.model = model
        self.year = year

    def fuel(self) -> None:
        print(f"Fueld {self.model} by aviapetrol")


class GasStation:

    def fuel_vehicles(self, *vehicles: "IVehicle") -> None:
        for vehicle in vehicles:
            print("----------------")
            print(f'Fueling vehicle ("{vehicle.model}" of {vehicle.year})')
            vehicle.fuel()


class Police:

    def issue_license(self, *vehicles) -> None:
        for vehicle in vehicles:
            print(f'Issuing license to {vehicle.model}')
            vehicle.pass_exam()


tesla = ElectroCar(Color.RED, "Tesla Model X", 2016, DriveType.FULL)
bmw = PetrolCar(Color.GREEN, "BMW M4", 2018, DriveType.BACK)
opel = GasCar(Color.BLUE, "Opel Astra", 2002, DriveType.FRONT)

plane = Plane("Cessna 174", 1975)

wog_station = GasStation()
wog_station.fuel_vehicles(tesla, bmw, opel, plane)











"""
red_car = Car(Color.RED, 'VW', 2018, DriveType.FRONT)
blue_car = Car(Color.BLUE, 'Mazda', 2018, DriveType.BACK)
green_fulldrive_car = Car(Color.GREEN, 'BMW', 2018, DriveType.FULL)


print(red_car)
print(blue_car)
print(green_fulldrive_car)
print(isinstance(Car, object))

print(f"{blue_car.color = }, {blue_car.__dict__ = }")
print(f"{blue_car.default_color = }")

# Error - absent in object and class
# print(f"{blue_car.default_metallic_color = }")

print(f"{Car.default_color = }, {Car.__dict__ = }")
"""

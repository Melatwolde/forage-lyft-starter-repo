import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex
from engine.model.tire import CarriganTire, OctoprimeTire

class TestCar(unittest.TestCase):

    def test_car_with_carrigan_tires_needs_service_when_one_or_more_tires_are_worn_down_to_90_or_more(self):
        tires = [CarriganTire(), CarriganTire(), CarriganTire(), CarriganTire()]
        tires[0].tire_wear = 0.9
        car = Car(datetime.today(), 0, 0, tires)

        self.assertTrue(car.needs_service())

    def test_car_with_carrigan_tires_does_not_need_service_when_all_tires_are_worn_down_to_less_than_90(self):
        tires = [CarriganTire(), CarriganTire(), CarriganTire(), CarriganTire()]
        tires[0].tire_wear = 0.8
        tires[1].tire_wear = 0.7
        tires[2].tire_wear = 0.6
        tires[3].tire_wear = 0.5
        car = Car(datetime.today(), 0, 0, tires)

        self.assertFalse(car.needs_service())

    def test_car_with_octoprime_tires_needs_service_when_the_total_wear_of_all_four_tires_is_3_or_more(self):
        tires = [OctoprimeTire(), OctoprimeTire(), OctoprimeTire(), OctoprimeTire()]
        tires[0].tire_wear = 0.75
        tires[1].tire_wear = 0.75
        tires[2].tire_wear = 0.75
        tires[3].tire_wear = 0.75
        car = Car(datetime.today(), 0, 0, tires)

        self.assertTrue(car.needs_service())

    def test_car_with_octoprime_tires_does_not_need_service_when_the_total_wear_of_all_four_tires_is_less_than_3(self):
        tires = [OctoprimeTire(), OctoprimeTire(), OctoprimeTire(), OctoprimeTire()]
        tires[0].tire_wear = 0.6
        tires[1].tire_wear = 0.5
        tires[2].tire_wear = 0.4
        tires[3].tire_wear = 0.3
        car = Car(datetime.today(), 0, 0, tires)

        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()

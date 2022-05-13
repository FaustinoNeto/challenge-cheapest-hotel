from unittest import TestCase
from datetime import datetime
from src import my_module

class MyTest(TestCase):

    def test_hotel_maisbarato_1(self):
        result = my_module.get_cheapest_hotel('regular',
                                              [datetime(2009, 3, 16), datetime(2009, 3, 17), datetime(2009, 3, 18)])
        self.assertEqual(result, 'Lakewood')

    def test_hotel_maisbarato_2(self):
        result = my_module.get_cheapest_hotel('regular',
                                              [datetime(2009, 3, 20), datetime(2009, 3, 21), datetime(2009, 3, 22)])
        self.assertEqual(result, 'Bridgewood')

    def test_hotel_maisbarato_3(self):
        result = my_module.get_cheapest_hotel('reward',
                                              [datetime(2009, 3, 26), datetime(2009, 3, 27), datetime(2009, 3, 28)])
        self.assertEqual(result, 'Ridgewood')

#!/usr/bin/python3
"""Defines unittests for models/city.py."""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City

class TestCity_instantiation(unittest.TestCase):
    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_two_cities_unique_ids(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

#!/usr/bin/python3
"""Test suite for Amenity class of the models.amenity module"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity

class TestAmenity_instantiation(unittest.TestCase):
    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_two_amenities_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_args_unused(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

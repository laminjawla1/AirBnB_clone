#!/usr/bin/env python3
"""
This module implements a test
for the city model
"""
import unittest
from datetime import datetime
from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    """
    Test the City class
    """

    def setUp(self):
        self.obj = City()
        self.obj.name = "Serekunda"
        self.state = State()
        self.obj.state_id = self.state.id

    # Testing formats
    def test_date_time_format_valid(self):
        self.assertEqual(City.DATE_TIME_FORMAT, r"%Y-%m-%dT%H:%M:%S.%f")

    def test_date_time_format_invalid(self):
        format = City.DATE_TIME_FORMAT
        self.assertNotEqual(format, r"my_wrong_date_time_format")

    def test_created_at_format(self):
        created_at = self.obj.to_dict().get("created_at")
        self.assertEqual(created_at, self.obj.created_at.isoformat())

    def test_updated_at_format(self):
        updated_at = self.obj.to_dict().get("updated_at")
        self.assertEqual(updated_at, self.obj.updated_at.isoformat())

    # Testing types
    def test_typeof_City_model_instance_id(self):
        self.assertEqual(type(self.obj.id), str)

    def test_typeof_City_model_instance_created_at(self):
        self.assertEqual(type(self.obj.created_at), datetime)

    def test_typeof_City_model_instance_updated_at(self):
        self.assertEqual(type(self.obj.updated_at), datetime)

    def test_typeof_City_model_instance_name(self):
        self.assertEqual(type(self.obj.name), str)

    def test_typeof_City_model_instance_state_id(self):
        self.assertEqual(type(self.obj.state_id), str)

    def test_typeof_City_model_instance_to_dict_equal(self):
        self.assertIsInstance(self.obj.to_dict(), dict)

    def test_typeof_City_model_instance_to_dict_not_equal(self):
        self.assertNotIsInstance(self.obj.to_dict(), str)

    # Testing values
    def test_value_of_City_model_instance_id(self):
        id = self.obj.id
        self.assertEqual(id, self.obj.id)

    def test_value_of_City_model_instance_created_at(self):
        created_at = self.obj.created_at
        self.assertEqual(created_at, self.obj.created_at)

    def test_value_of_City_model_instance_updated_at(self):
        updated_at = self.obj.updated_at
        self.assertEqual(updated_at, self.obj.updated_at)

    def test_value_of_City_model_instance_state_id(self):
        state_id = self.obj.state_id
        self.assertEqual(state_id, self.obj.state_id)

    def test_value_of_City_model_instance_name(self):
        name = self.obj.name
        self.assertEqual(name, self.obj.name)

    # Testing saving
    def test_saving_instance(self):
        old_updated_at = self.obj.updated_at
        self.obj.save()
        new_updated_at = self.obj.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    # Test string representation
    def test_string_representation(self):
        class_name = self.obj.__class__.__name__
        self.assertEqual(
            str(self.obj),
            f"[{class_name}] ({self.obj.id}) {self.obj.__dict__}",
        )

    # Testing instance created from a dict
    def test_create_instance_from_dict(self):
        dict_items = self.obj.to_dict()
        new_obj = City(**dict_items)
        self.assertEqual(new_obj.id, self.obj.id)
        self.assertEqual(new_obj.created_at, self.obj.created_at)
        self.assertEqual(new_obj.updated_at, self.obj.updated_at)


if __name__ == "__main__":
    unittest.main()

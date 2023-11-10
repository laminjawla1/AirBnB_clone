#!/usr/bin/env python3
"""
This module implements a test for the
base model
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test the BaseModel class
    """

    def setUp(self):
        self.obj = BaseModel()
        self.obj.dev1 = "Lamin"
        self.obj.dev2 = "RadouaneBaba"
        self.obj.number = 10

    # Testing formats
    def test_date_time_format_valid(self):
        self.assertEqual(BaseModel.DATE_TIME_FORMAT, r"%Y-%m-%dT%H:%M:%S.%f")

    def test_date_time_format_invalid(self):
        format = BaseModel.DATE_TIME_FORMAT
        self.assertNotEqual(format, r"my_wrong_date_time_format")

    def test_created_at_format(self):
        created_at = self.obj.to_dict().get("created_at")
        self.assertEqual(created_at, self.obj.created_at.isoformat())

    def test_updated_at_format(self):
        updated_at = self.obj.to_dict().get("updated_at")
        self.assertEqual(updated_at, self.obj.updated_at.isoformat())

    # Testing types
    def test_typeof_base_model_instance_id(self):
        self.assertEqual(type(self.obj.id), str)

    def test_typeof_base_model_instance_created_at(self):
        self.assertEqual(type(self.obj.created_at), datetime)

    def test_typeof_base_model_instance_updated_at(self):
        self.assertEqual(type(self.obj.updated_at), datetime)

    def test_typeof_base_model_instance_dev1(self):
        self.assertEqual(type(self.obj.dev1), str)

    def test_typeof_base_model_instance_dev2(self):
        self.assertEqual(type(self.obj.dev2), str)

    def test_typeof_base_model_instance_number(self):
        self.assertEqual(type(self.obj.number), int)

    def test_typeof_base_model_instance_to_dict_equal(self):
        self.assertIsInstance(self.obj.to_dict(), dict)

    def test_typeof_base_model_instance_to_dict_not_equal(self):
        self.assertNotIsInstance(self.obj.to_dict(), str)

    # Testing values
    def test_value_of_base_model_instance_id(self):
        id = self.obj.id
        self.assertEqual(id, self.obj.id)

    def test_value_of_base_model_instance_created_at(self):
        created_at = self.obj.created_at
        self.assertEqual(created_at, self.obj.created_at)

    def test_value_of_base_model_instance_updated_at(self):
        updated_at = self.obj.updated_at
        self.assertEqual(updated_at, self.obj.updated_at)

    def test_value_of_base_model_instance_dev1(self):
        dev1 = self.obj.dev1
        self.assertEqual(dev1, self.obj.dev1)

    def test_value_of_base_model_instance_dev2(self):
        dev2 = self.obj.dev2
        self.assertEqual(dev2, self.obj.dev2)

    def test_value_of_base_model_instance_number(self):
        number = self.obj.number
        self.assertEqual(number, self.obj.number)

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


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""
This module implements a test
for the Place model
"""
import unittest
from models.city import City
from models.user import User
from datetime import datetime
from models.place import Place
from models.amenity import Amenity


class TestPlace(unittest.TestCase):
    """
    Test the Place class
    """

    def setUp(self):
        self.city = City()
        self.obj = Place()
        self.user = User()
        self.amenity_1 = Amenity()
        self.amenity_2 = Amenity()
        self.amenity_3 = Amenity()

        self.obj.city_id: str = self.city.id
        self.obj.user_id: str = self.user.id
        self.obj.name: str = "African Princes"
        self.obj.description: str = "Cool resort for passing time"
        self.obj.number_rooms: int = 5
        self.obj.number_bathrooms: int = 3
        self.obj.max_guest: int = 7
        self.obj.price_by_night: int = 239
        self.obj.latitude: float = 1.2
        self.obj.longitude: float = 3.4
        self.obj.amenity_ids: list = [
            self.amenity_1.id,
            self.amenity_2.id,
            self.amenity_3.id,
        ]

    # Testing formats
    def test_date_time_format_valid(self):
        self.assertEqual(Place.DATE_TIME_FORMAT, r"%Y-%m-%dT%H:%M:%S.%f")

    def test_date_time_format_invalid(self):
        format = Place.DATE_TIME_FORMAT
        self.assertNotEqual(format, r"my_wrong_date_time_format")

    def test_created_at_format(self):
        created_at = self.obj.to_dict().get("created_at")
        self.assertEqual(created_at, self.obj.created_at.isoformat())

    def test_updated_at_format(self):
        updated_at = self.obj.to_dict().get("updated_at")
        self.assertEqual(updated_at, self.obj.updated_at.isoformat())

    # Testing types
    def test_typeof_Place_model_instance_id(self):
        self.assertIsInstance(self.obj.id, str)

    def test_typeof_Place_model_instance_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_typeof_Place_model_instance_updated_at(self):
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_typeof_Place_model_instance_name(self):
        self.assertIsInstance(self.obj.name, str)

    def test_typeof_Place_model_instance_city_id(self):
        self.assertIsInstance(self.obj.city_id, str)

    def test_typeof_Place_model_instance_user_id(self):
        self.assertIsInstance(self.obj.user_id, str)

    def test_typeof_Place_model_instance_description(self):
        self.assertIsInstance(self.obj.description, str)

    def test_typeof_Place_model_instance_number_rooms(self):
        self.assertIsInstance(self.obj.number_rooms, int)

    def test_typeof_Place_model_instance_number_bathrooms(self):
        self.assertIsInstance(self.obj.number_bathrooms, int)

    def test_typeof_Place_model_instance_max_guest(self):
        self.assertIsInstance(self.obj.max_guest, int)

    def test_typeof_Place_model_instance_price_by_night(self):
        self.assertIsInstance(self.obj.price_by_night, int)

    def test_typeof_Place_model_latitude(self):
        self.assertIsInstance(self.obj.latitude, float)

    def test_typeof_Place_model_longitude(self):
        self.assertIsInstance(self.obj.longitude, float)

    def test_typeof_Place_model_amenity_ids(self):
        self.assertIsInstance(self.obj.amenity_ids, list)

    def test_typeof_Place_model_instance_to_dict_equal(self):
        self.assertIsInstance(self.obj.to_dict(), dict)

    def test_typeof_Place_model_instance_to_dict_not_equal(self):
        self.assertNotIsInstance(self.obj.to_dict(), str)

    # Testing values
    def test_value_of_Place_model_instance_id(self):
        id = self.obj.id
        self.assertEqual(id, self.obj.id)

    def test_value_of_Place_model_instance_created_at(self):
        created_at = self.obj.created_at
        self.assertEqual(created_at, self.obj.created_at)

    def test_value_of_Place_model_instance_updated_at(self):
        updated_at = self.obj.updated_at
        self.assertEqual(updated_at, self.obj.updated_at)

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
        new_obj = Place(**dict_items)
        self.assertEqual(new_obj.id, self.obj.id)
        self.assertEqual(new_obj.created_at, self.obj.created_at)
        self.assertEqual(new_obj.updated_at, self.obj.updated_at)


if __name__ == "__main__":
    unittest.main()

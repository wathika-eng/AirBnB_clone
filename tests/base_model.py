import unittest
""" Test BaseModel """

from models.base_model import BaseModel

class MyTestCase(unittest.TestCase):
    """ Test BaseModel """
    def test_id(self):
        """ Test id """
        base = BaseModel()
        self.assertEqual(type(base.id), str)

    def test_created_at(self):
        """ Test created_at """
        base = BaseModel()
        self.assertEqual(type(base.created_at).__name__, "datetime")

    def test_updated_at(self):
        """ Test updated_at """
        base = BaseModel()
        self.assertEqual(type(base.updated_at).__name__, "datetime")

    def test_save(self):
        """ Test save """
        base = BaseModel()
        old = base.updated_at
        base.save()
        new = base.updated_at
        self.assertNotEqual(old, new)

    def test_str(self):
        """ Test __str__ """
        base = BaseModel()
        string = "[{}] ({}) {}".format(base.__class__.__name__, base.id,
                                       base.__dict__)
        self.assertEqual(string, str(base))

    def test_to_dict(self):
        """ Test to_dict """
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(type(base_dict), dict)
        self.assertTrue("__class__" in base_dict)
        self.assertTrue("created_at" in base_dict)
        self.assertTrue("updated_at" in base_dict)
        self.assertTrue("id" in base_dict)

    def test_kwargs(self):
        """ Test kwargs """
        base = BaseModel()
        base.name = "Holberton"
        base.my_number = 89
        base_dict = base.to_dict()
        new_base = BaseModel(**base_dict)
        self.assertEqual(base.id, new_base.id)
        self.assertEqual(base.created_at, new_base.created_at)
        self.assertEqual(base.updated_at, new_base.updated_at)
        self.assertEqual(base.name, new_base.name)
        self.assertEqual(base.my_number, new_base.my_number)
        self.assertNotEqual(base, new_base)

    def test_type(self):
        """ Test type """
        base = BaseModel()
        self.assertEqual(type(base).__name__, "BaseModel")
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))


if __name__ == '__main__':
    unittest.main()

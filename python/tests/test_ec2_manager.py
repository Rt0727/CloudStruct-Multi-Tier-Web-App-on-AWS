import unittest
from ec2_manager import create_ec2_instance

class TestEC2Manager(unittest.TestCase):
    def test_create_ec2_instance(self):
        instance = create_ec2_instance()
        self.assertIsNotNone(instance.id)

if __name__ == '__main__':
    unittest.main()
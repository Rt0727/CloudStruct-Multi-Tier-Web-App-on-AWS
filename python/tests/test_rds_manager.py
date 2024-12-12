import unittest
from rds_manager import create_rds_instance

class TestRDSManager(unittest.TestCase):
    def test_create_rds_instance(self):
        response = create_rds_instance()
        self.assertEqual(response['DBInstance']['DBInstanceIdentifier'], 'yourdbinstance')

if __name__ == '__main__':
    unittest.main()
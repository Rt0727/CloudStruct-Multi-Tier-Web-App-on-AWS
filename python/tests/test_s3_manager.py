import unittest
from s3_manager import create_s3_bucket

class TestS3Manager(unittest.TestCase):
    def test_create_s3_bucket(self):
        create_s3_bucket('your-app-bucket')
        # Additional assertions to verify bucket creation

if __name__ == '__main__':
    unittest.main()
from bucky import app
from bucky import bucket_activities
import unittest


class FlaskTestsCase(unittest.TestCase):
    # Ensure that flask was set correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the page loads correctly
    def test_index_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Live A Life You Will Remember' in response.data)

    # Ensure login loads correctly with the right credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="user", password="user"), follow_redirects=True)
        self.assertTrue(b'My Profile' in response.data)

    # Ensure login sign up loads correctly
    def test_sign_up_loads_correct(self):
        tester = app.test_client(self)
        response = tester.post('/register', content_type='html/text')
        self.assertTrue(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()


class BucketlistTests(unittest.TestCase):
    # Ensures that add activity is working correctly
    def test_add_activity(self):
        tester = app.test_client(self)
        response = tester.post('/bucket', data=dict(title="Andela", activity="lorem"), follow_redirects=True)
        self.assertTrue(b'My Profile' in response.data)

    # confirms if the activity is stored in the bucket list
    def confirm_activity_is_stored(self, title):
        for title in bucket_activities:
            if title in bucket_activities:
                return True
        return False


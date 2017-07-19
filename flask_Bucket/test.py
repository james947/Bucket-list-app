from app import app
import unittest

class FlaskTestsCase(unittest.TestCase):

    #Ensure that flask was set correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    
    #Ensure that the page loads correctly
    def test_index_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Live A Life You Will Remember' in response.data)

        
    #Ensure login loads correctly with the right credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data = dict(username="user", password="user"), follow_redirects=True)
        self.assertIn(b'My Profile' in response.data)
    
if __name__== '__main__':
    unittest.main()

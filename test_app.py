import unittest
from requests.structures import CaseInsensitiveDict
from app import app
from io import BytesIO
import os


class AppTestCase(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"

    def test_home_page(self):
        """homepage get request"""
        request = app.test_client(self)
        response = request.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

    def test_home_page_again(self):
        """homepage get request"""
        request = app.test_client(self)
        response = request.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Apply Sobel Filter !!!', response.data)

    def test_upload_page(self):
        """uploading page get request"""
        request = app.test_client(self)
        response = request.get('/upload_page', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your Sobel Image will be shown here!', response.data)

    def test_sobel_success(self):
        """sobel filter success post request"""
        filename = os.path.join(app.root_path, 'Images', '123.jpg')
        with open(filename, 'rb') as img1:
            imgStringIO1 = BytesIO(img1.read())
        request = app.test_client(self)
        response = request.post(self.API_URL+'/upload_page', content_type='multipart/form-data',
                                data={
                                    'pic': (imgStringIO1, 'img1.jpg')})
        self.assertEqual(response.status, "200 OK")
        self.assertIn(b'Your Sobel Image!', response.data)


if __name__ == '__main__':
    unittest.main()

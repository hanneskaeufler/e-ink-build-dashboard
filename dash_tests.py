import unittest
from PIL import Image
import dash

class DashTests(unittest.TestCase):
    def test_render_returns_image(self):
        self.assertIsInstance(dash.Dash().render(), Image.Image)

if __name__ == '__main__':
    unittest.main()

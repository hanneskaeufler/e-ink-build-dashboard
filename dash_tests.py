from PIL import Image
import dash
import os
import unittest

class DashTests(unittest.TestCase):
    def test_render_returns_image(self):
        projects = [
            ('MyProject', dash.BuildStatus.failed)
        ]
        self.assertIsInstance(dash.Dash(projects, os.getcwd()).render(), Image.Image)

if __name__ == '__main__':
    unittest.main()

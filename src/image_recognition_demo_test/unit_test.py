import unittest
from unittest.mock import MagicMock

from image import Image
from recognition import Recognition
from facade import ImageFacade


class TestImage(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_image_instance_is_singleton(self):
        image_instance1 = Image()
        image_instance2 = Image()

        self.assertIs(image_instance1, image_instance2)


class TestRecognition(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_recognition_process_text_extraction(self):
        mock_image_facade = MagicMock(spec=ImageFacade)
        recognition = Recognition('src/image_recognition_demo_test/edit.jpg')
        recognition.image_facade = mock_image_facade

        mock_image_facade.process_image.return_value = 'Edit Recordings'

        result = recognition.process_text_extraction(language='eng')

        self.assertEqual(result, 'Edit Recordings')


if __name__ == '__main__':
    unittest.main()

import unittest
import test_sound_timer.py

class SoundTests(unittest.TestCase):

    def test_ring(self):
        assert output == "ringgg!"

    def test_ding(self):
        assert output == "Ding!"

if __name__ == '__main__':
    unittest.main()

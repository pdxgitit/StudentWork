import unittest

import dd_game

class GameTests(unittest.TestCase):
    def test_build_cells(self):
        assert len(dd_game.build_cells(2, 2)) == 4
    def test_get_locations(self):
        monster, door, player = dd_game.get_locations(dd_game.build_cells(2, 2))
        assert not monster == player == door

if __name__ == '__main__':
    unittest.main()

import unittest

from initialization.load_defaults import load_defaults


class TestMappingMethods(unittest.TestCase):

    def test_mapping(self):
        actual_defaults = load_defaults("defaultsTest.json")
        self.assertEqual(actual_defaults.agents, [{'position': {'x': 1, 'y': 1}}])
        self.assertEqual(actual_defaults.obstacles, [{'position': {'x': 1, 'y': 1}, 'type': 'LAKE'}])


if __name__ == '__main__':
    unittest.main()

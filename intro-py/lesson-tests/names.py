import unittest
from test_func import getname

"""
print("Enter 'q' for quit")
while True:
    f = input('Your name: ')
    if f == 'q':
        break
    l = input('Your lastname: ')
    if l == 'q':
        break
    full = getname(f, l)
    print(full)
"""
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = getname('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    def test_first_last_middle_name(self):
        formatted_name = getname('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
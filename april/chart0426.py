import json
import os
import unittest
from typing import Dict


def error_handle():
    try:
        10 / 0
    except ZeroDivisionError as e:
        print("except", e)
    finally:
        print("finally")

error_handle()


# class TestDict(unittest.TestCase):
#     def test_init(self):
#         d = {}
#         self.assertEqual(len(d),0)
#         self.assertFalse('a' in d)

# file operate
f = open(r'E:\Code\Python\daily-algo-python\env.json','r')
s = f.read()
user = json.loads(s)
print(user['age'])

print(os.name)
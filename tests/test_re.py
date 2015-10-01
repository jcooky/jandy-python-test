import unittest
import re


class TestRegularExpression(unittest.TestCase):
    def testCompile(self):
        r = re.compile('foo|bar')
        self.assertTrue(r.match('foo'))

import sys
import unittest
from unittest import IsolatedAsyncioTestCase
import re
import os


# Comment
#

class _private_class:
    pass


'''
Multiline 
comment
'''
"""
Multiline 
comment
"""
''' Comment '''
""" Comment """


class Human:
    def __init__(self):
        self.name = 'Guido'
        self.head = self.createHead()

    def createHead(self):
        return Human.Head(self)

    async def asyncCreateHead(self):
        return Human.Head(self)

    class Head:
        def __init__(self, human):
            self.human = human

        def talk(self):
            return 'talking...', self.human.name

        def error(self):
            raise


human = Human()
print(human.name)

import pathlib
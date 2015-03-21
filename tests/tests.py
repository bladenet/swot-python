from __future__ import absolute_import

import os
import sys
import unittest

from swot import Swot

class TestSwot(unittest.TestCase):
    def test_swot(self):
        assert Swot.is_academic('lreilly@stanford.edu')
        assert Swot.is_academic('LREILLY@STANFORD.EDU')
        assert Swot.is_academic('Lreilly@Stanford.Edu')
        assert Swot.is_academic('lreilly@slac.stanford.edu')
        assert Swot.is_academic('lreilly@strath.ac.uk')
        assert Swot.is_academic('lreilly@soft-eng.strath.ac.uk')
        assert Swot.is_academic('lee@ugr.es')
        assert Swot.is_academic('lee@uottawa.ca')
        assert Swot.is_academic('lee@mother.edu.ru')
        assert Swot.is_academic('lee@ucy.ac.cy')

        assert Swot.is_academic('lee@leerilly.net') is False
        assert Swot.is_academic('lee@gmail.com') is False
        assert Swot.is_academic('lee@stanford.edu.com') is False
        assert Swot.is_academic('lee@strath.ac.uk.com') is False

        assert Swot.is_academic('stanford.edu')
        assert Swot.is_academic('slac.stanford.edu')
        assert Swot.is_academic('www.stanford.edu')
        assert Swot.is_academic('http://www.stanford.edu')
        assert Swot.is_academic('http://www.stanford.edu:9393')
        assert Swot.is_academic('strath.ac.uk')
        assert Swot.is_academic('soft-eng.strath.ac.uk')
        assert Swot.is_academic('ugr.es')
        assert Swot.is_academic('uottawa.ca')
        assert Swot.is_academic('mother.edu.ru')
        assert Swot.is_academic('ucy.ac.cy')

        assert Swot.is_academic('leerilly.net') is False
        assert Swot.is_academic('gmail.com') is False
        assert Swot.is_academic('stanford.edu.com') is False
        assert Swot.is_academic('strath.ac.uk.com') is False

        assert Swot.is_academic(None) is False
        assert Swot.is_academic('') is False
        assert Swot.is_academic('the') is False

        assert Swot.is_academic(' stanford.edu')
        assert Swot.is_academic('lee@strath.ac.uk ')
        assert Swot.is_academic(' gmail.com ') is False

        assert Swot.is_academic('lee@stud.uni-corvinus.hu')

        # overkill
        assert Swot.is_academic('lee@harvard.edu')
        assert Swot.is_academic('lee@mail.harvard.edu')


if __name__ == '__main__':

    unittest.main()
"""Tests mapped methods for errors"""
import logging
import unittest
import lciafmt
from lciafmt.util import read_method
logger = logging.getLogger(__name__)
class TestInputFiles(unittest.TestCase):

    def test_duplicate_flows(self):
        """Tests whether a target flow maps to more than one characterization
        factor for a given indicator"""
        method_list = lciafmt.supported_methods()
        total_duplicates = 0
        for m in method_list:
            method = read_method(lciafmt.Method.get_class(m['id']))
            if method is not None:
                dup_flowables = method[method[['Method', 'Indicator', 'Flow UUID']].duplicated(keep=False)]
                duplicates = len(dup_flowables)
                if duplicates > 0:
                    logger.warning('duplicate factors in method %s', m['name'])
                total_duplicates += duplicates
        self.assertTrue(total_duplicates == 0, 'Duplicate factors in one or more methods')


if __name__ == "__main__":
    unittest.main()

'''
Created on 11.06.2015

@author: marscher
'''
import warnings
import unittest
import os

from pyemma.util.config import readConfiguration
from pyemma.util.files import TemporaryDirectory


class TestConfig(unittest.TestCase):

    def test_can_not_create_cfg_dir(self):
        os.environ['HOME'] = '/dev/null'

        exp_homedir = os.path.expanduser('~')
        assert exp_homedir == '/dev/null'

        with warnings.catch_warnings(record=True) as w:
            # Cause all warnings to always be triggered.
            warnings.simplefilter("always")
            # Trigger a warning.
            readConfiguration()
            assert len(w) == 1
            assert issubclass(w[-1].category, UserWarning)
            assert "could not create" in str(w[-1].message)

    def test_non_writeable_cfg_dir(self):

        with TemporaryDirectory() as tmp:
            cfg_dir = os.path.join(tmp, '.pyemma')
            os.mkdir(cfg_dir)
            os.environ['HOME'] = tmp
            # make cfg dir non-writeable
            os.chmod(cfg_dir, 444)

            exp_homedir = os.path.expanduser('~')
            assert exp_homedir == tmp

            with warnings.catch_warnings(record=True) as w:
                # Cause all warnings to always be triggered.
                warnings.simplefilter("always")
                # Trigger a warning.
                readConfiguration()
                assert len(w) == 1
                assert issubclass(w[-1].category, UserWarning)
                assert "is not writeable" in str(w[-1].message)

if __name__ == "__main__":
    unittest.main()

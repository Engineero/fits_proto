#*******************************************************************************
#                                UNCLASSIFIED
#*******************************************************************************
#*******************************************************************************
# Filename: test_fits_proto.py
# Language: Python
# Author: ntoner
# Created: 2018-05-10
#
# Description:
# Tests for the FITS protobuf. Basically verify that I can translate a real
# FITS file into my protobuf and back again without losing any of the
# information in the original file.
#
#*******************************************************************************

import unittest
from astropy.io import fits
from .. import fits_pb2 as fp


class TestFitsProto(unittest.TestCase):
    """ Tests for the FITS protobuf. """
    def setUp(self):
        self.fname = fits.util.get_testdata_filepath('test0.fits')
        self.hdul = fits.open(fits_image_filename)

    def test_


#*******************************************************************************
#                                UNCLASSIFIED
#*******************************************************************************

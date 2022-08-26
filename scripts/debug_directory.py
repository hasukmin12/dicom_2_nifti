# -*- coding: utf-8 -*-
"""
dicom2nifti

@author: abrys
"""

import shutil
import tempfile
import unittest

import dicom2nifti.convert_dir as convert_directory
from dicom2nifti import settings


class TestConversionDirectory(unittest.TestCase):
    def test_convert_directory(self):

        tmp_output_dir = tempfile.mkdtemp()
        try:
            settings.enable_resampling()
            settings.set_resample_spline_interpolation_order(1)
            settings.set_resample_padding(-1000)
            settings.disable_validate_slice_increment()
            # settings.enable_validate_instance_number()
            settings.disable_validate_orthogonal()
            convert_directory.convert_directory("/Users/abrys/Downloads/scans",
                                                "/Users/abrys/Downloads/scans")

        finally:
            shutil.rmtree(tmp_output_dir)

    def test_convert_directory2(self):

        tmp_output_dir = tempfile.mkdtemp()
        try:
            import pydicom
            # headers = pydicom.read_file("/Users/abrys/Downloads/failing_cases/test.dcm")
            convert_directory.convert_directory("/Users/abrys/Downloads/Agfa",
                                                "/Users/abrys/Downloads/Agfa")

        finally:
            shutil.rmtree(tmp_output_dir)

    def test_convert_directory3(self):

        tmp_output_dir = tempfile.mkdtemp()
        try:
            import pydicom
            settings.disable_validate_slicecount()
            convert_directory.convert_directory("/Users/abrys/Downloads/single_slice",
                                                "/Users/abrys/Downloads/single_slice")

        finally:
            shutil.rmtree(tmp_output_dir)


if __name__ == '__main__':
    convert_directory.convert_directory("/Users/abrys/Downloads/Agfa",
                                        "/Users/abrys/Downloads/Agfa")

    # unittest.main()

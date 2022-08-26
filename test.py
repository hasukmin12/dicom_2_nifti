import os
import dicom2nifti

input_path= '/home/has/Datasets/211101_3D_AVIEW_CT/DICOM/abdomen_0001/5816_20181105/0201_20181105_101027'
output_path = '/home/has/Datasets/211101_3D_AVIEW_CT/DICOM/abdomen_0001'

dicom2nifti.convert_directory(input_path, output_path, compression=True, reorient=True)
import dicom2nifti
import os

# dicom2nifti.convert_directory(dicom_directory, output_folder, compression=True, reorient=True)


# dicom_directory = '/home/has/Results/dcm_list/case_000/ANO_0087'
path = '/home/has/Datasets/_has_CT3/case_00000'

dicom2nifti.settings.set_gdcmconv_path(path)
# dicom_directory = '/home/has/Datasets/CV_CT/slice_5'


# dicom_folder = next(os.walk(dicom_directory))[1]
# dicom_folder.sort()
# print(dicom_folder)

# dicom_directory2 = '/home/has/Datasets/(has)CT3/case_00004'

output_path = '/home/has/Datasets/rst'
if os.path.isdir(output_path) == False:
    os.makedirs(output_path)

dicom2nifti.convert_directory(path, output_path, compression=True, reorient=True)



# for dicom_list in dicom_folder:
#     print(dicom_list)
#     output_path = '/home/has/Datasets/CT_nifti/case_' + '{0:05d}'.format(dicom_folder.index(dicom_list))
#     os.makedirs(output_path)
#     dicom2nifti.convert_directory(dicom_directory + '/' + dicom_list, output_path, compression=True, reorient=True)
#     # dicom2nifti.convert_directory(dicom_directory, output_path, compression=True, reorient=True)
#     # icom2nifti.dicom_series_to_nifti(dicom_directory +'/'+dicom_list, output_path, reorient_nifti=True)
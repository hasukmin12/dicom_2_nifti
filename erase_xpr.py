import dicom2nifti
import os
import shutil

dicom_directory = '/home/has/Datasets/CT2'

dicom_list = next(os.walk(dicom_directory))[1]
dicom_list.sort()
print(dicom_list)

for case in dicom_list:
    path = os.path.join(dicom_directory,case)
    # print(path)
    case_list = next(os.walk(path))[2]
    for list in case_list:
        if list[-3:]!='dcm':
            # print(list)
            erase_path = os.path.join(path, list)
            print(erase_path)
            os.remove(erase_path)









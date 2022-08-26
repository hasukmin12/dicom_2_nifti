import dicom2nifti
import os
import shutil

dicom_directory = '/home/has/Datasets/CT'

dicom_list = next(os.walk(dicom_directory))[1]
dicom_list.sort()

print(dicom_list)
print(dicom_list[3][7:-1])

aim_path = '/home/has/Datasets/CT2'

for dicom in dicom_list:
    # os.makedirs(aim_path+'/'+dicom)
    print(dicom)
    shutil.copytree(dicom_directory +'/' + dicom, aim_path+'/'+"case_{0:05}".format(int(dicom[7:-1])-1))




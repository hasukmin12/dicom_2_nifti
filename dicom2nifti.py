import dicom2nifti
import os
import shutil

# dicom2nifti.convert_directory(dicom_directory, output_folder, compression=True, reorient=True)


# dicom_directory = '/home/has/Results/dcm_list/case_000/ANO_0087'
dicom_directory = '/home/has/Datasets/211126_3D_AVEW_CT/DICOM'
# dicom_directory = '/home/has/Datasets/CV_CT/slice_5'
dicom_folder = next(os.walk(dicom_directory))[1]
dicom_folder.sort()
print(dicom_folder)

rst_path = '/home/has/Datasets/_has_Task176_AVIEW_1mm_reverse'
if os.path.isdir(rst_path) == False:
    os.makedirs(rst_path)

for case in dicom_folder:
    print(case)
    dicom_f1_n = next(os.walk(os.path.join(dicom_directory, case)))[1]
    dicom_f1 = os.path.join(dicom_directory, case, dicom_f1_n[0])

    dicom_f2_n = next(os.walk(dicom_f1))[1]
    if len(dicom_f2_n) == 1:
        dicom_f2 = os.path.join(dicom_f1,dicom_f2_n[0])
    elif len(dicom_f2_n) == 2:
        if dicom_f2_n[0][0] == '4':
            dicom_f2 = os.path.join(dicom_f1, dicom_f2_n[0])
            print("5mm exist")
            print(dicom_f2_n[0])
        elif dicom_f2_n[1][0] == '4':
            dicom_f2 = os.path.join(dicom_f1, dicom_f2_n[1])
            print("5mm exist")
            print(dicom_f2_n[0])

    # trash_list = next(os.walk(dicom_f2))[1]
    # trash_list.sort()
    #
    # erase_path = os.path.join(dicom_f2, trash_list[0])
    # print(erase_path)
    # shutil.rmtree(erase_path)


    input_path = dicom_f2
    print(input_path)

    output_f_path = os.path.join(rst_path,'case_{0:05d}'.format(dicom_folder.index(case)+1))
    print(output_f_path)
    if os.path.isdir(output_f_path)==False:
        os.makedirs(output_f_path)

    # output_path = os.path.join(output_f_path, 'imaging.nii.gz')
    # print(output_path)
    dicom2nifti.convert_directory(input_path, output_f_path, compression=True, reorient=True)
    # dicom2nifti.convert_directory(dicom_directory, output_path, compression=True, reorient=True)
    # icom2nifti.dicom_series_to_nifti(dicom_directory +'/'+dicom_list, output_path, reorient_nifti=True)

    output_before = next(os.walk(output_f_path))[2]
    output_before_path = os.path.join(output_f_path, output_before[0])
    # print(output_before_path)
    os.rename(output_before_path, os.path.join(output_f_path,'imaging.nii.gz'))
    # print(output_f_path)
    print("")





# for dicom_list in dicom_folder:
#     print(dicom_list)
#     output_path = '/home/has/Datasets/(has)CT_nii/case_' + '{0:05d}'.format(dicom_folder.index(dicom_list))
#     os.makedirs(output_path)
#     input_path = dicom_directory + '/' + dicom_list
#     print(input_path)
#     dicom2nifti.convert_directory(input_path, output_path, compression=True, reorient=True)
#     # dicom2nifti.convert_directory(dicom_directory, output_path, compression=True, reorient=True)
#     # icom2nifti.dicom_series_to_nifti(dicom_directory +'/'+dicom_list, output_path, reorient_nifti=True)
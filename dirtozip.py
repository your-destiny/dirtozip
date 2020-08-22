import zipfile
import os
import sys


def createZip():
    script_name = str(sys.argv[0]).split('/')[-1]
    zip_file_name = script_name.split('.')[0] + '.zip'
    path = str(os.path.dirname(os.path.abspath(__file__)))
    output_path = path
    skip = None
    skip_script_name_and_zip_file_name = True
    arg_warning_1 = "The output file name was not found, the name of the script will be used as the name"
    arg_warning_2 = "The directory used to create the archive was not found, the directory with the script will be " \
                    "taken as the path "
    arg_warning_3 = "The directory for the output file was not found, the directory with the script will be taken as " \
                    "the path "

    if len(sys.argv) == 2:
        zip_file_name = sys.argv[1] + '.zip'
        printWarning(arg_warning_2)
        printWarning(arg_warning_3)
    elif len(sys.argv) == 3:
        zip_file_name = sys.argv[1] + '.zip'
        path = str(sys.argv[2])
        printWarning(arg_warning_3)
    elif len(sys.argv) >= 4:
        zip_file_name = sys.argv[1] + '.zip'
        path = str(sys.argv[2])
        output_path = str(sys.argv[3])
        if len(sys.argv) >= 5:
            if sys.argv[4] != '' and sys.argv[4].find(';') != -1:
                skip = sys.argv[4].split(';')
        if len(sys.argv) >= 6:
            skip_script_name_and_zip_file_name_list = ['No', 'no', 'Not', 'not', 'N', 'n', '0', 'false', 'False',
                                                       'FALSE',
                                                       'f', 'F']
            if sys.argv[5] in skip_script_name_and_zip_file_name_list:
                skip_script_name_and_zip_file_name = False
    else:
        printWarning(arg_warning_1)
        printWarning(arg_warning_2)
        printWarning(arg_warning_3)

    if os.path.exists(path):
        out_zipfile = zipfile.ZipFile(output_path + '/' + zip_file_name, 'w', zipfile.ZIP_DEFLATED)
        for dir_path, dir_names, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dir_path, filename)
                parent_path = os.path.relpath(file_path, path)
                if skip_script_name_and_zip_file_name and (parent_path == zip_file_name or parent_path == script_name):
                    continue
                check = False
                if skip:
                    for elem in skip:
                        if parent_path.find(elem) != -1:
                            check = True
                            break
                if check:
                    continue
                out_zipfile.write(file_path, parent_path)
        out_zipfile.close()


def printWarning(warning):
    print(warning)


if __name__ == "__main__":
    createZip()

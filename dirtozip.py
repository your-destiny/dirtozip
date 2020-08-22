import zipfile
import os
import sys


def createZip():
    array_argv = sys.argv[1:]
    script_name = str(array_argv[0]).split('/')[-1]
    zip_file_name = script_name.split('.')[0] + '.zip'
    path = str(os.path.dirname(os.path.abspath(__file__)))
    output_path = path
    skip = None
    skip_script_name_and_zip_file_name = False
    ofn_warning_1 = "The output file name was not found, the name of the script will be used as the name"
    idp_warning_2 = "The directory used to create the archive was not found, the directory with the script will be " \
                    "taken as the path "
    odp_warning_3 = "The directory for the output file was not found, the directory with the script will be taken as " \
                    "the path "
    if not checkIfExistArgv(array_argv, 'ofn'):
        printWarning(ofn_warning_1)
    else:
        zip_file_name = getArgvValue(array_argv, 'ofn') + '.zip'

    if not checkIfExistArgv(array_argv, 'idp'):
        printWarning(idp_warning_2)
    else:
        path = str(getArgvValue(array_argv, 'idp'))

    if not checkIfExistArgv(array_argv, 'odp'):
        printWarning(odp_warning_3)
    else:
        output_path = str(getArgvValue(array_argv, 'odp'))

    if checkIfExistArgv(array_argv, 'sfs'):
        if getArgvValue(array_argv, 'sfs') != '' and getArgvValue(array_argv, 'sfs').find(';') != -1:
            skip = getArgvValue(array_argv, 'sfs').split(';')

    if checkIfExistArgvWithoutValue(array_argv, 'sofs'):
        skip_script_name_and_zip_file_name = True

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


def getArgvValue(array_argv, elem):
    return list(map(lambda x: x[1],
                    [inner_arg for inner_arg in list(map(lambda x: x.split('--')[1].split('='), array_argv)) if
                     len(inner_arg) > 1]))[list(map(lambda x: x.split('=')[0],[arg for arg in list(map(lambda x: x.split('--')[1], array_argv)) if arg.find('=') != -1])).index(elem)]


def checkIfExistArgv(array_argv, elem):
    return elem in list(map(lambda x: x.split('--')[1].split('=')[0], array_argv))


def checkIfExistArgvWithoutValue(array_argv, elem):
    return elem in [arg for arg in list(map(lambda x: x.split('--')[1], array_argv)) if arg.find('=') == -1]


if __name__ == "__main__":
    createZip()

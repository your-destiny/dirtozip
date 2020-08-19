from zipfile import ZipFile
import os
import sys

def createZip():
    script_name = str(sys.argv[0]).split('/')[-1]
    zip_file_name = script_name.split('.')[0] + '.zip'
    path = str(os.path.dirname(os.path.abspath(__file__)))
    output_path = path
    arg_warning_1 = "The output file name was not found, the name of the script will be used as the name"
    arg_warning_2 = "The directory used to create the archive was not found, the directory with the script will be taken as the path"
    arg_warning_3 = "The directory for the output file was not found, the directory with the script will be taken as the path"

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
    else:
        printWarning(arg_warning_1)
        printWarning(arg_warning_2)
        printWarning(arg_warning_3)

    with ZipFile(output_path + '/' + zip_file_name, 'w') as zipObj:
        for folderName, subfolders, filenames in os.walk(path):
            for filename in filenames:
                if filename == script_name or filename == script_name.split('.')[0] + '.bat' or filename == zip_file_name:
                    continue
                filePath = os.path.join(folderName, filename)
                zipObj.write(filePath, os.path.basename(filePath))

def printWarning(warning):
    print(warning)

if __name__ == "__main__":
    createZip()
# DIRTOZIP

Python console application for archive a directory. ***You can pass 5 optional  parameters, parameters can be in different order*** : 

  1) **-ofn=value** or **--output_filename=value**. Output file name. <br> 
  If the output file name was not found, the name of the script will be used as the name. <br><br>
  2) **-idp=value** or **--input_dir_path=value**. Input directory path <br>
  If the directory used to create the archive was not found, the directory with the script will be taken as the path <br><br>
  3) **-odp=value** or **--output_dir_path=value**. Output directory path <br>
  If the directory for the output file was not found, the directory with the script will be taken as the path <br><br>
  4) **-sfs=value** or **--skip_files_subdir=value**. Skip files and subdirectories <br>
  If you need not to include some subdirectories or files in the archive. Must be listed separated by commas <br><br>
  5) **-sofs** or **--skip_output_file_script**. Skip output filename and script name <br>
  Not skipped by default, if you need to be skipped, then type 


### Installation

Dirtozip requires [Python](https://www.python.org/downloads/) v3+
You need to download the file and run it.
### Run
#### Parameters can be in different order.

##### Open cmd or powershell and type in the command line:

```sh
python ./script_name.py -ofn=NameArchive -idp=InputDirPath -odp=OutputDirPath -sfs=SkipFilesSubdir -sofs
```
or
```sh
python ./script_name.py --output_filename=NameArchive --input_dir_path=InputDirPath --output_dir_path=OutputDirPath --skip_files_subdir=SkipFilesSubdir --skip_output_file_script
```
##### Open bash and type in the command line:

```sh
python3 ./script_name.py -ofn=NameArchive -idp=InputDirPath -odp=OutputDirPath -sfs=SkipFilesSubdir -sofs
```
or
```sh
python3 ./script_name.py --output_filename=NameArchive --input_dir_path=InputDirPath --output_dir_path=OutputDirPath --skip_files_subdir=SkipFilesSubdir --skip_output_file_script
```

##### Example

```sh
python ./dirtozip.py --output_filename=App --input_dir_path=%cd% --output_dir_path=%cd% --skip_files_subdir=dirtozip.bat;.idea;.vscode --skip_output_file_script
```
```sh
python ./dirtozip.py -ofn=App -idp=%cd% -odp=%cd% -sfs=dirtozip.bat;.idea;.vscode -sofs
```

License
----

MIT
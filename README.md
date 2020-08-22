# DIRTOZIP

Python console application for zip directory archiving. You can pass 5 optional  parameters: 

  1) Output file name. <br> 
  If the output file name was not found, the name of the script will be used as the name
  2) Input directory path <br>
  If the directory used to create the archive was not found, the directory with the script will be taken as the path
  3) Output directory path <br>
  If the directory for the output file was not found, the directory with the script will be taken as the path
  4) Skip files and subdirectories <br>
  If you need not to include some subdirectories or files in the archive. Must be listed separated by commas
  5) Skip output filename and script name <br>
  Skipped by default, if you need not to be skipped, then type ['No', 'no', 'Not', 'not', 'N', 'n', '0', 'false', 'False',
'FALSE',
                                                       'f', 'F']


### Installation

Dirtozip requires [Python](https://www.python.org/downloads/) v3+
You need to download the file and run it.
### Run
Open cmd or powershell and type in the command line:
```sh
python ./name_file.py NameArchive InputPath OutputPath SkipFiles SkipOutputFilenameAndScriptName
```
Open bash and type in the command line:
```sh
python3 ./name_file.py NameArchive InputPath OutputPath SkipFiles SkipOutputFilenameAndScriptName
```

##### Example

```sh
python ./dirtozip.py App %cd% %cd% dirtozip.bat;.idea;.vscode n
```

Also you can create a .bat file and type in the command line for example:
```sh
python ./name_file.py App %cd% %cd%
```

License
----

MIT
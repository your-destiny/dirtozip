# DIRTOZIP

Python console application for zip directory archiving. You can pass 3 optional  parameters: 

  1) Output file name. 
  If the output file name was not found, the name of the script will be used as the name
  2) Input directory path
  If the directory used to create the archive was not found, the directory with the script will be taken as the path
  3) Output directory path
  If the directory for the output file was not found, the directory with the script will be taken as the path


### Installation

Dirtozip requires [Python](https://www.python.org/downloads/) v3+
You need to download the file and run it.
### Run
Open cmd or powershell and type in the command line:
```sh
python ./name_file.py NameArchive InputPath OutputPath
```
Open bash and type in the command line:
```sh
python3 ./name_file.py NameArchive InputPath OutputPath
```
Also you can create a .bat file and type in the command line for example:
```sh
python ./name_file.py App %cd% %cd%
```

License
----

MIT
# SimMissingDataGenepop
Simulate missing data for Genepop format data

<b>Description</b>

Randomly replace alleles with null alleles (e.g., 0000 in 4 digit data) across overall data set. You can determine how many percent of data to be missing. For example, if a data set includes a total of 10,000 loci given from 50 individuals and 200 loci, and 5% of missing data is determined, then 500 out of 10,000 loci will become null in the data set.

<b>How to use this function</b>

1. Get your GENEPOP format file ready.
2. Download "SimMissingDataGenepop.py" and save it with your Genepop file under the same folder.
3. Open a command prompt (or terminal) and change the path to the folder (>cd YOUR_FOLDER_PATH)
4. When command prompt is under the folder, type "python SimMissingDataGenepop.py [Your file] -m [an integer]", and enter
5. Note that the integer after "-m" is the percentage of loci to be missing. If you type "5", it means 5% of loci will become null. Also make sure there is a space between each word.
6. While the program is running, it prints out some data information in the command prompt window. 
7. The program will create a new file (it will not overwrite your input file) that has an extended file name. [Your file name]_95.txt means 95% of data are not missing in the file.
8. Also note that the program does not recognize any existing missing data in your input file. It treats your input file as a complete data set and randomly replace data with null alleles.

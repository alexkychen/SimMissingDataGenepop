# SimMissingDataGenepop
Simulate missing data for Genepop format data

Description
Randomly replace alleles with null alleles (e.g., 0000 in 4 digit data) across overall data set. You can determine how many percent of data to be missing. For example, if a data set includes a total of 10,000 loci given from 50 individuals and 200 loci, and 5% of missing data is determined, then 500 out of 10,000 loci will become null in the data set.

How to use this function
1. Get your GENEPOP format file ready.
2. Download "SimMissingDataGenepop.py" and save it with your Genepop file under the same folder.
3. Open a command prompt (or terminal) and change the path to the folder (>cd YOUR_FOLDER_PATH)
4. When command prompt is under the folder, type "python SimMissingDataGenepop.py [Your file] -m [an integer]", and enter
5. Note that the integer after "-m" is the percentage of loci to be missing. If you type "5", it means 5% of loci will become null. 

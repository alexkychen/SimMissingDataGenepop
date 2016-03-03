#!/usr/bin/env python
from __future__ import division
import argparse, random

parser = argparse.ArgumentParser(prog='Genepop Missing Data Simulator',description='Replace alleles with missing data (0000) for Genepop format')
parser.add_argument('input', help='Enter Genepop format file',metavar='input')
parser.add_argument('-m','--missing', type=int, default=5, choices=range(1,100), help='Enter percentage of dataset to be missing. e.g., 10 means 10% of missing data', metavar='')
args = parser.parse_args()

genepop = args.input
misPerc = args.missing/100
remain = 100 - args.missing

#Read entire file and save each line into a list
entireFile = []
with open(genepop, 'r') as gf:
	for line in gf:
		line = line.strip()
		entireFile.append(line)

#Parse locus name
locus_ls = []
count1stPOP = 0
for item in entireFile[1:]: #skip the 1st line of file title
	count1stPOP = count1stPOP + 1
	if not item.lower() == 'pop':
		locusList = item.split(',')
		for locus in locusList:
			locus = locus.strip()
			locus_ls.append(locus)
	elif item.lower() == 'pop':
		break
locusQty = len(locus_ls)
print('Number of loci: '+str(locusQty))

#Parse sample ID and allele data
sampleID_ls = []
alleleData = []	
popLabel = [] #a list of pop label for each individual
popCount = 0
for ind in entireFile[count1stPOP:]: #start counting with 1st 'pop'
	if ind.lower() == 'pop':
		popCount = popCount + 1
	elif not ind.lower() == 'pop':
		popLabel.append(popCount)
		IDandAlleles = ind.split(',')
		ID = IDandAlleles[0].strip()
		sampleID_ls.append(ID)
		Alleles = IDandAlleles[1].strip().split()
		for a in Alleles:
			alleleData.append(a)
sampleQty = len(sampleID_ls)
alleleDataLength = len(alleleData)
print('Number of individuals: '+str(sampleQty))
print('Number of loci in overall dataset: '+str(alleleDataLength))
print('Number of populations: '+str(popCount))

#Generate random index for missing alleles
missingLocusQty = int(alleleDataLength * misPerc)#quantify how many loci to be missing
alleleIndex = random.sample(range(0,alleleDataLength),missingLocusQty)#generate missing data index for total number of loci(alleleDataLength)
alleleIndex.sort()#sort the indices in ascending
#print(alleleIndex)
misAlleleQty = len(alleleIndex)
print('Number of missing loci: '+str(misAlleleQty)+' out of '+str(alleleDataLength))

#Replace allele in alleleData with '0000' based on alleleIndex(missing allele index)
for i in alleleIndex:
	alleleData[i] = '0000'

#Write outfile
infileName = genepop.split('.')[0]
oufileName = infileName + '_' + str(remain) + '.txt'
with open(oufileName, 'w') as res:
	#write file title (1st line) to outfile
	res.write('Genepop format with '+str(int(misPerc*100))+'% missing data in '+str(popCount)+' populations, '+str(sampleQty)+' individuals, '+str(locusQty)+' loci ')
	#write locus name to outfile (one loucs name each line)
	for loc in locus_ls:
		res.write('\n'+loc)
	#write 'pop',sample ID, and allele data to outfile
	popDetect = 0
	k = 0 #index for alleleData to be used for each individual 
	for j in xrange(sampleQty):
		if popLabel[j] > popDetect: #see if pop label goes to the next pop, if yes, print 'pop' and then sampleID + alleles
			popDetect = popLabel[j]
			res.write('\npop')
			indID = sampleID_ls[j] #get sample ID from sampleID_ls
			indAlleles = alleleData[k:k+locusQty] #get allels from allleData
			k = k + locusQty #set allele index(cursor) for next individual
			res.write('\n'+indID+', ')
			for x in indAlleles:
				res.write(' '+x)
		elif popLabel[j] == popDetect:
			indID = sampleID_ls[j] #get sample ID from sampleID_ls
			indAlleles = alleleData[k:k+locusQty] #get allels from allleData
			k = k + locusQty #set allele index(cursor) for next individual
			res.write('\n'+indID+', ')
			for y in indAlleles:
				res.write(' '+y)
	
	
	
	


import ROOT
from ROOT import TFile
import sys
import os
import numpy as np

#Access variables
root_dump = sys.argv[1]
hist_dump = sys.argv[2]

print(root_dump)
print(hist_dump)

#Get list of root files
#Function to return array of file names in a specified path
def file_list(path):
	entries = []
	obj = os.scandir(path)
	for entry in obj:
		if entry.is_file():
			entries.append(entry.name)
	files = np.array(entries)
	return files

files = file_list(root_dump)

#Loop over each file and extract histograms
for i in files:
	#Define root file
	in_name = root_dump + "/" + i
	fin = TFile(in_name,"READ")

	#Modify out file name
	split_in = i.split("_")
	out_name = hist_dump+"/"+split_in[0]+"_"+split_in[1]+"_2D.root"

	#Create out file
	fout = TFile(out_name, "RECREATE")

	#Get histograms and define as TH2D objects
	hClover_gg = fin.Get("hClover_gg")
	hClover_gg_esum = fin.Get("hClover_gg_esum")

	#Write histograms to root file
	fout.WriteObject(hClover_gg,"hClover_gg")
	fout.WriteObject(hClover_gg_esum,"hClover_gg_esum")

				

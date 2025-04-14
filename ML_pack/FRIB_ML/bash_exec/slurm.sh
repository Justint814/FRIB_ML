#!/bin/bash

# BPC + SNL
# 9/7/2023
# Script to send simulations for ML level scheme project
# to the slurm job submission daemon

# Script usage (all files follow same naming convention):

# Run the number of simulations as defined in the "script.py" script
# input 1 - number of simulations to run
# input 2 - simulation path and executable name
# input 3 - path for the directory with the macros for sim

numruns="$(($1-1))"
simname=$2
macname=$3
slurmoutdir=$4

#echo ${numruns}
#echo ${simname}
#echo ${macname}

#Source correct version of root to allow simulations to run
source /home/bpc135/root_installation/builddir/bin/thisroot.sh

#process the range of segments for a given run

#echo "simulation executable name: $infilebase"
#echo "output file base name: $outfilebase"
    

for i in $(seq 0 ${numruns}); do
	echo 'Submitting' ${simname} 'for' ${macname}macro_$i.mac
	sbatch --job-name=sim-${i}  --wrap="${simname} ${macname}/macro_$i.mac" --output=${slurmoutdir}/slurm-ID-%j-JOB-%x.out
	
done

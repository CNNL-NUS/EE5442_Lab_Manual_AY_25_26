#!/bin/bash
#PBS -j oe
#PBS -l vnode=Boltzmann01
#PBS -l walltime=24:00:00
#PBS -l cudamem=500mb
#PBS -l ncpus=4
#PBS -l mem=4gb

. /etc/profile
module load local mumax3

export PROJDIR="/users/---/---/---/---/"

cd ${PROJDIR} && $(which mumax3) example2.mx3



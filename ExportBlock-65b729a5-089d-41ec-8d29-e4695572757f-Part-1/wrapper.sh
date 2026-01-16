#!/bin/bash

echo "wrap here"
. /etc/profile
module load local pytorch/py3/2.2.0

# For this script to execute somthing meaningful, replace
# <working_dir> and <path_to_python_script> with the
# absolute paths to 1) the directory in which the last
# command is to be run from, and 2) the Python script to
# run. Then, uncomment the next two lines.
#cd <working_dir> && \
#python3 <path_to_python_script> 

echo "wrapper successful"
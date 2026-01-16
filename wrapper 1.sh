#!/bin/bash

echo "begin wrapper"
export working_dir='/users/----/----/----/'
export path_to_python_script='/users/----/----/----/try.py'

. /etc/profile
module load pytorch/py3/2.2.0
cd ${working_dir} && \
python3 ${path_to_python_script}
echo "wrapper successful"
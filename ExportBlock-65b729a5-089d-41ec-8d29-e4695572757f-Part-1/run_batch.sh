#!/bin/bash
echo "************************* Rendering batch *************************"
export PROJDIR="/users/---/---/---/---/"
cd ${PROJDIR} && qsub run_single.sh
echo "************************* Completed batch *************************"
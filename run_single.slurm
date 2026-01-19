#!/bin/bash
#SBATCH --job-name=mumax3
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err

#SBATCH --partition=StdQ
#SBATCH --nodes=1
#SBATCH --nodelist=boltzmann01

#SBATCH --time=4:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=4G

# GPU memory request (cluster-dependent)
# If your system supports gres:
#SBATCH --gres=cudamem:300

module load mumax/3.11.1

# Input file 
if [[ -z "$MX3FILE" ]]; then
    echo "WARNING: MX3FILE not provided. Using default."
    MX3FILE="script_4.mx3"
fi
export PROJDIR="/users/ee5442/imemXXX"
cd "${PROJDIR}" || exit 1

# Run mumax3
mumax3 -cache "$TMPDIR" "${MX3FILE}"
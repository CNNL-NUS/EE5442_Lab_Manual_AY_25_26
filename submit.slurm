#!/bin/bash
#SBATCH --job-name=python_job
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err

#SBATCH --partition=StdQ
#SBATCH --nodes=1
#SBATCH --nodelist=boltzmann01        

#SBATCH --time=8:00:00               
#SBATCH --cpus-per-task=4            
#SBATCH --mem=8G                     

# GPU memory request — adjust value as needed
#SBATCH --gres=cudamem:512            

# ── Paths ─────────────────────────────────────────────────────────────────────
# Replace these with your actual absolute paths
PROJDIR="/users/grad/avadhharkishanka/trial"
WRAPPER_SCRIPT="/users/grad/avadhharkishanka/trial/wrapper.sh"

# ── Run ───────────────────────────────────────────────────────────────────────
echo "Job started: $(date)"
echo "Running on node: $(hostname)"

cd "${PROJDIR}" || exit 1

# Launch NNTools container (Ubuntu 22), which executes the wrapper script
# --nv passes through NVIDIA GPU access into the container
/apps/containers/scripts/nntools/loadNNTools_Ub22.sh \
  -run \
  --nv \
  "${WRAPPER_SCRIPT}"

echo "Job finished: $(date)"

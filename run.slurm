#!/bin/bash
#SBATCH --job-name=map_anything_test    # Job name
#SBATCH --output=logs/%x_%j.out         # Standard output (%x=job name, %j=job ID)
#SBATCH --error=logs/%x_%j.err          # Standard error
#SBATCH --partition=gpu                 # Partition name (adjust if different)
#SBATCH --gres=gpu:1                    # Request 1 GPU
#SBATCH --cpus-per-task=8               # CPU cores for data loading
#SBATCH --mem=32G                       # Memory allocation
#SBATCH --time=12:00:00                 # Max runtime (hh:mm:ss)

# Optional: email notifications
# #SBATCH --mail-type=END,FAIL
# #SBATCH --mail-user=you@example.com

# --- Load your environment ---
module purge
module load cuda/12.1                    # Or whatever your cluster provides
module load anaconda                     # Or use a custom conda setup

# Activate your conda environment
source activate vggt

python run_for_dataset.py 
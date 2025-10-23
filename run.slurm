# --- Load your environment ---
module purge
module load cuda/12.1                    # Or whatever your cluster provides
module load anaconda                     # Or use a custom conda setup

# Activate your conda environment
source activate vggt

# Activate your conda environment
source activate vggt

python run_for_dataset.py 
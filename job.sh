#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -o result.log
#SBATCH -e result.err
#SBATCH --gpus 1

source .venv/bin/activate
python -m pip install -e . --no-build-isolation

# python train.py -s dtu_results/mesh/scan105.ply -m output/date/scan105 -r 2 --depth_ratio 1
# python render.py -r 2 --depth_ratio 1 --skip_test --skip_train
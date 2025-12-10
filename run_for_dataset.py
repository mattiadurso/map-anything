import os
import torch

paths = {
    "imc_local": {
        "base_path": "/home/mattia/Desktop/Repos/wrapper_factory/benchmarks_2D/imc/data/phototourism",
        "images_path": "set_100/images",
        "output_path": "/home/mattia/Desktop/Repos/wrapper_factory/benchmarks_3D/results",
    },
    "imc_orochi": {
        "base_path": "/data/mdurso/imc",
        "images_path": "set_100/images",
        "output_path": "/data/mdurso/results",
    },
    "eth3d_local": {
        "base_path": "/home/mattia/Desktop/Repos/wrapper_factory/benchmarks_3D/eth3d",
        "images_path": "images_by_k",
        "output_path": "/home/mattia/Desktop/Repos/wrapper_factory/benchmarks_3D/results",
    },
    "eth3d_orochi": {
        "base_path": "/data/mdurso/eth3d",
        "images_path": "images_by_k",
        "output_path": "/data/mdurso/results",
    },
    "terrasky3D_local": {
        "base_path": "/home/mattia/Desktop/datasets/terrasky3D",
        "images_path": "images_150",
        "output_path": "/home/mattia/Desktop/Repos/batchsfm/benchmark",
    },
    "terrasky3D_orochi": {
        "base_path": "/data/mdurso/terrasky3d",
        "images_path": "frames",
        "output_path": "/data/mdurso/terrasky3d/results",
    },
}


# device
cuda_id = 7
device = f"cuda:{cuda_id}" if torch.cuda.is_available() else "cpu"

dataset = "terrasky3D_orochi"
base_path = paths[dataset]["base_path"]
images_path = paths[dataset]["images_path"]
output_path = paths[dataset]["output_path"]
scenes = sorted(os.listdir(f"{base_path}"))

for scene in scenes:
    out_dir = f"{output_path}/map_anything/{dataset.split('_')[0]}/{scene}"
    os.makedirs(out_dir, exist_ok=True)
    os.system(
        f"python scripts/demo_colmap.py \
            --scene_dir {base_path}/{scene} \
            --images_dir {base_path}/{scene}/{images_path} \
            --output_dir {out_dir} \
            --device {device} \
    "
        #       --use_ba \
    )

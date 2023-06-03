
# CoOp

python train.py --root data --seed 1 --trainer CoOp --dataset-config-file configs/datasets/caltech101.yaml --config-file configs/trainers/CoOp/rn50.yaml --output-dir temp_output TRAINER.COOP.N_CTX 8 TRAINER.COOP.CSC False TRAINER.COOP.CLASS_TOKEN_POSITION end DATASET.NUM_SHOTS 4

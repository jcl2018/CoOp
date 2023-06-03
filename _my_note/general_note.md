
1. environment setup: follow https://github.com/KaiyangZhou/Dassl.pytorch use conda to activate an environment called dassl; set interpreter;
2. download a dataset (use small one first, I used caltech101)
3. download cn_clip module from https://github.com/OFA-Sys/Chinese-CLIP
4. adjust coop.py to use cn_clip (also change the code in this file where uses clip):

from cn_clip.clip import utils
from cn_clip import clip
from cn_clip.clip.bert_tokenizer import FullTokenizer as _Tokenizer  # cn-clip uses Bert tokenizer which has 3 classes. idk which one to use so I randomly chose fulltokenizer

problem now: build_model method need to be changed


run train.py:
train.py --root data --seed 1 --trainer CoOp --dataset-config-file configs/datasets/caltech101.yaml --config-file configs/trainers/CoOp/rn50.yaml --output-dir output_dir TRAINER.COOP.N_CT
X 8 TRAINER.COOP.CSC False TRAINER.COOP.CLASS_TOKEN_POSITION end DATASET.NUM_SHOTS 4

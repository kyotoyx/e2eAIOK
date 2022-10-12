#!/bin/bash

# init conda env
eval "$('/opt/intel/oneapi/intelpython/latest/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
# activate conda
conda activate pytorch-1.10.0
# run main.py
cd /home/vmagent/app/AIDK/TransferLearningKit/src
python main_finetunner_cifar.py -s1 -r0 -t0 -R10
python main_finetunner_cifar.py -s1 -r0 -t1 -R10
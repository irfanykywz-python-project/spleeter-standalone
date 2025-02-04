import argparse
import os
import sys
from multiprocessing import freeze_support
from spleeter import separator

# for spleeter
if sys.stdout is None:
	sys.stdout = open(os.devnull, 'w', encoding='utf-8')
if sys.stderr is None:
	sys.stderr = open(os.devnull, 'w', encoding='utf-8')

# setup spleeter
freeze_support()
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spleeter Standalone CLI")
    parser.add_argument('--file', type=str, help='.wav file', required=True)
    parser.add_argument('--output', type=str, help='output location', required=True)
    args = parser.parse_args()

    try:
        split = separator.Separator('spleeter:2stems', multiprocess=False)
        split.separate_to_file(args.file, args.output)
        print('success')
    except:
        print('error')
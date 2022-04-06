import os
import sys
import time
import argparse


a_parser = argparse.ArgumentParser()
a_parser.add_argument('--src', nargs='+')
args = a_parser.parse_args()


if __name__ == '__main__':

    if args.src is not None:
        path_list = args.src
    else:
        path_list = []
        for line in sys.stdin.readlines():
            line = line.strip()
            line = os.path.abspath(line)
            path_list.append(line)

    for path in path_list:

        found_res = False
        dpath_res = os.path.join(path, 'outdir/result')
        for fname in os.listdir(dpath_res):
            if fname.endswith('.json'):
                found_res = True
        
        if not found_res:
            sys.stdout.write(path+'\n')

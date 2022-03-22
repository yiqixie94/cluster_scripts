import os
import sys
import time
import argparse


a_parser = argparse.ArgumentParser()
a_parser.add_argument('--src', nargs='+')
a_parser.add_argument('-v', '--verbose', action='store_true')
a_parser.add_argument('-m', '--maxnum', type=int, default=-1)
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

    n_submit = 0

    for path in path_list:

        os.chdir(path)
        fpath_ini = os.path.join(path, 'config.ini')
        if not os.path.exists(fpath_ini):
            sys.stderr.write('WARNING: ini file not found, for \"{}\"\n'.format(path))
            continue

        try:
            message = subprocess.check_output(['parallel_bilby_generation', 'config.ini']).decode()
            if args.verbose:
                sys.stdout(message)
            n_submit += 1
            sys.stdout.write(path + '\n')
            sys.stdout.flush()
            time.sleep(1)
        except:
            sys.stderr.write('WARNING: generation failed, for \"{}\"\n'.format(path))

        if n_submit == args.maxnum:
            break
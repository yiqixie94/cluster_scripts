import os
import sys
import time
import argparse


a_parser = argparse.ArgumentParser()
a_parser.add_argument('--src', nargs='+')
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
        dpath_submit = os.path.join(path, 'outdir/submit')
        fpath_submit = None
        for name in os.listdir(dpath_submit):
            if name.startswith('analysis') and name.endswith('.sh'):
                fpath_submit = os.path.join(dpath_submit, name)
        if fpath_submit is None:
            sys.stderr.write('WARNING: submit script not found, for \"{}\"\n'.format(path))
            continue

        try:
            subprocess.check_output(['sbatch', fpath_submit])
            n_submit += 1
            sys.stdout.write(path + '\n')
            sys.stdout.flush()
            time.sleep(1)
        except:
            sys.stderr.write('WARNING: submission failed, for \"{}\"\n'.format(path))

        if n_submit == args.maxnum:
            break
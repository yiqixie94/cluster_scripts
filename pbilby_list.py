import os
import sys
import argparse


a_parser = argparse.ArgumentParser()
a_parser.add_argument('root', nargs='+')
args = a_parser.parse_args()


if __name__ == '__main__':

    for rt in args.root:

        for name in os.listdir(rt):

            path = os.path.join(rt, name)
            if os.path.isfile(path):
                continue
            elif 'config.ini' not in os.listdir(path):
                continue

            sys.stdout.write(path)

            if slurm.Job.validate(top)\
                    and vasp.Relaxation.validate(top):
                job = slurm.Job(top)
                rel = vasp.Relaxation(top)
            else:
                continue




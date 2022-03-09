import os
import sys
import time
import argparse
import subprocess

a_parser = argparse.ArgumentParser()
a_parser.add_argument('-p', '--partition', default='secondary')
args = a_parser.parse_args()

if __name__ == '__main__':

    cpu_list = subprocess.check_output(
        ['sinfo', '-p', args.partition, '-o', '%50f %20C']
    ).decode().splitlines()

    result = {}

    for i,cpu_info in enumerate(cpu_list):

        if i == 0:
            continue

        cpu_info = cpu_info.strip()
        features, _, states = cpu_info.partition(' ')
        _, _, features = features.rpartition(',')
        cpu_type = features.split('_')[0]
        net_type = features.split('_')[1]
        num_idle = int(states.split('/')[1])

        kw = (cpu_type,net_type)
        if kw not in result:
            result[kw] = 0
        result[kw] += num_idle

    result = list(result.items())
    result = sorted(result, key=lambda x:x[1], reverse=True)

    for kw, num_idle in result:
        kw = ','.join(kw)
        sys.stdout.write('{}: {}\n'.format(kw, num_idle))


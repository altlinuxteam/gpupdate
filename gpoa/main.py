#! /usr/bin/env python3

import argparse

import sys, os
from policy import data_roots, Perms
from jinja2 import  Environment, PackageLoader, FileSystemLoader, StrictUndefined, select_autoescape

templateLoader = FileSystemLoader(searchpath="./templates")
env = Environment(loader=templateLoader, undefined=StrictUndefined)

class policy_generator:
    _gpupdate_cache = '/var/cache/gpupdate'
    _base_path = "/tmp/gpoa_scripts"

    def __init__(self, sid):
        self._sid = sid
        self._root_path = '{base}/root'.format(base=self._base_path)
        self._user_path = '{base}/user'.format(base=self._base_path)

    def generate(self):
        cpath = os.path.join(self._gpupdate_cache, self._sid)

        for root, dirs, files in os.walk(cpath):
            path = root[len(cpath):] #.split(os.sep)
            scope = path.split(os.sep)[0]
            reg = path[len(scope) + len(os.sep) + len(self._sid):]
            if reg in data_roots.keys():
                h = data_roots[reg]()
                print("found applier %s for %s" % (h.name(), reg))
                res = h.process(scope, root)
                if res:
                    params = res
                    template = env.get_template(h.template)
                    if h.perms == Perms.ROOT:
                        out = self._root_path
                    elif h.perms == Perms.USER:
                        out = self._user_path

                    with open('{}/{}'.format(out, h.script_name), 'w') as f:
                        f.write(template.render(**params, DEBUG=False))


def parse_arguments():
    arguments = argparse.ArgumentParser(description='Generate configuration out of parsed policies')
    arguments.add_argument('sid',
        type=str,
        help='SID to parse policies from')
    return arguments.parse_args()

def main():
    args = parse_arguments()
    polgen = policy_generator(args.sid)
    polgen.generate()

if __name__ == "__main__":
    main()


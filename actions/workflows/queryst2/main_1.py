import os, sys, json, re

from st2common.runners.base_action import Action


        
class QuerySt2(Action):
    def run(self, pack_name):
        print("directory name = " + pack_name)
        
        packs = {}
        secret_list = []
        path = r"/opt/stackstorm/packs"
        packFullPath = os.path.join(path, pack_name)

        # check if pack available
        p = re.compile(r"\S+.yaml")
        for root, d_names, f_names in os.walk(packFullPath):
            for f in f_names:
                if p.match(f):
                    fullpath = os.path.join(root,f)
                    fh = open(fullpath, "r")
                    lines = fh.readlines()
                    contents = "----".join(lines)
                    match = re.findall(r'.*st2kv.system.(\S+)\s?|', contents)
                    for m in match:
                        if m not in secret_list and m:
                            secret_list.append(m)
                            print(m)
                    fh.close()
        packs[pack_name] = secret_list
        print(packs)
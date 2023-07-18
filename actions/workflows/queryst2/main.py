import os, sys, json, re

from st2common.runners.base_action import Action


        
class QuerySt2(Action):
    def run(self, directoryName):
        print("directory name = " + directoryName)
        mypacks = { 'name': os.path.basename(directoryName),
                    'secretList': [] }
        p = re.compile(r"\S+.yaml")
        for root, d_names, f_names in os.walk(directoryName):
            for f in f_names:
                if p.match(f):
                    fullpath = os.path.join(root,f)
                    fh = open(fullpah, "r")
                    lines = fh.readlines()
                    contents = "----".join(lines)
                    match = re.findall(r'.*st2kv.system.(\S+)\s*|', contents)
                    for m in match:
                        if m not in mypacks['secretList']:
                            mypacks['secretList'].append(m)
                            print(m)
                    fh.close()
        print(mypacks)
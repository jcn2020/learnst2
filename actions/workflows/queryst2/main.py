import os, sys, json, re

from st2common.runners.base_action import Action


        
class QuerySt2(Action):
    def run(self, pack_name):
        print("directory name = " + pack_name)
        
        # looping through /opt/stackstorm/packs
        pack_secrets = {}
        secret_list = []
        path = r"/opt/stackstorm/packs"

        ## find different packs in packs
        pack_list = [name for name in os.listdir(path)]
        print("========")
        print(pack_list)
        print("=== LIST PACKS /opt/stackstorm =====")

        for pack in pack_list: 
          print("=====> pack = ", pack)
          secret_list = []
          pack_fullpath = os.path.join(path, pack)

          # check for all secrets in st2kv.system.* 
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
                    fh.close()
          if secret_list: pack_secrets[pack] = secret_list
        print(packs)
        # find the current working pwd
        print("======== Current PWD ===== ")
        print(os.listdir())
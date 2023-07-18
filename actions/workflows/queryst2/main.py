import os, sys, json, re

from st2common.runners.base_action import Action

class QuerySt2(Action):
    def run(self, directory_name):
        print("directory name = " + directory_name)
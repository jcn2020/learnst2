import os, sys, json, re

from st2common.runners.base_action import Action

class QuerySt2(Action):
    def run(self, directoryName):
        print("directory name = " + directoryName)
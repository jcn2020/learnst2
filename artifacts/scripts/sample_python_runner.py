
import sys, os

from st2common.runners.base_action import Action

class MeClass(Action):
  def run(self, name):
    try:
        print('Hello {}'.format(name))
    except:
        sys.exit()
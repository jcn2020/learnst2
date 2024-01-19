import os, time, sys
import logging

logging.basicConfig(format='%(ascitime)s %(message)s',
                     level=logging.DEBUG')

from st2common.runners.base_action import Action  

class var_contidition_1_checker(Action):
  def run(self, production_active): 
    self.production_active = production_active
    logging.debug(f"value of production_active = {production_active}")

    if production_active == True : 
        self.result = "True - production_active is True"
    else:
        self.result = "False - procdution_active is False "
      
                    
    logging.debug(self.result)
    return(self.result)
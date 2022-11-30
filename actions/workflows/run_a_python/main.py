import time, os, sys 
import logging
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig( format='%(asctime)s %(message)s',
                     level=logging.DEBUG )

from st2common.runner.base_action import Action 

class RunAPython:
  def __init__( self, my_api_key, my_docserv_client_secret):
    self.api_key = my_api_key
    self.client_secret = my_docserv_client_secret
  
  def run(self): 
    logging.debug(f"value of api_key = {self.api_key}")
    logging.debug(f"value of client_secret= {self.client_secret}")

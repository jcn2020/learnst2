import time, os, sys 
import logging
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig( format='%(asctime)s %(message)s',
                     level=logging.DEBUG )

from st2common.runners.base_action import Action 

class RunAPython(Action):
  #def __init__( self, my_api_key , my_docserv_client_secret ):
    #self.api_key = my_api_key
    #self.client_secret = my_docserv_client_secret
  
  def run(self, my_api_key="v1", my_docserv_client_secret="v2"): 
    self.api_key = my_api_key
    self.docserv_client_secret = my_docserv_client_secret
    logging.debug(f"value of api_key = {my_api_key}")
    logging.debug(f"value of client_secret= {my_docserv_client_secret}")

    logging.debug(f"value of api_key = {self.api_key}")
    logging.debug(f"value of client_secret= {self.docserv_client_secret}")
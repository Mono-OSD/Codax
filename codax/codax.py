"""
Add the below to your code before you can use these functions:
- import codax
- from codax import codax

Then, to use the functions, do something like:
- codax.setup_wiz()
"""
import time
from time import sleep
# You can also import your own files here.

def setup_wiz():
  print("The below is powered by the Codax setup wizard.")
  print("""
                                                               
   _|_|_|              _|                                      
 _|          _|_|    _|_|_|_|              _|    _|  _|_|_|    
   _|_|    _|_|_|_|    _|      _|_|_|_|_|  _|    _|  _|    _|  
       _|  _|          _|                  _|    _|  _|    _|  
 _|_|_|      _|_|_|      _|_|                _|_|_|  _|_|_|    
                                                     _|        
                                                     _|     \n\n""")
  sleep(1.00)
  name = input("(1) What's your name?\n> ")
  sleep(1.00)
  
  # Feel free to add more code for this function!

# Comment the line below, this is purely for testing
#setup_wiz()

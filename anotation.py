import os
import re
import pandas as pd
import numpy as np
from glob import glob
import json
from collections import OrderedDict
import pprint

currentdir = os.getcwd()
file = glob('*.json')
def change(val1, val2):
  for i in file:
    text_dir= os.path.join(currentdir,str(i))
    with open(text_dir) as f:
      df = json.load(f)
      for index in range(len(df['regions'])):
        if df['regions'][index]["tags"] == [val1] :
          df['regions'][index]["tags"] = [val2]
      d_update = df
    with open(text_dir, 'w') as f:
      json.dump(d_update, f, indent=2, ensure_ascii=False)
  
  if __name__ == '__main__':
    val1 = input('Enter the class name before: ')
    val2 = input('Enter the class name after: ')
    change(val1, val2)
    
  


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
for i in file:
  text_dir= os.path.join(currentdir,str(i))
  print(text_dir)
  with open(text_dir) as f:
    df = json.load(f)
    for index in range(len(df['regions'])):
      if df['regions'][index]["tags"] == ['rose2'] :
        df['regions'][index]["tags"] = ['rose1']
      if df['regions'][index]["tags"] == ['rose4'] :
        df['regions'][index]["tags"] = ['rose3']
    d_update = df
  with open(text_dir, 'w') as f:
    json.dump(d_update, f, indent=2, ensure_ascii=False)
  


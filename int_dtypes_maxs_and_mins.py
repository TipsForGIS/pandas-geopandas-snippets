import numpy as np

d_types = ['int8', 'int16', 'int32', 'int64']

for t in d_types:
     print(np.iinfo(t))

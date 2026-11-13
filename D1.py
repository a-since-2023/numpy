#why numpy ?

#implementation of basic vector addition and multiplication

import sys
import numpy as np
np_array = np.arange(1_000_000,dtype=np.int64)
py_list = list(range(1_000_000))

ls_size = sys.getsizeof(py_list)+ sum(sys.getsizeof(x) for x in py_list);
a_size = np_array.nbytes;

print(ls_size,a_size);

#vector implementation

v_a = np.array([1,2])
v_b = np.array([3,4])

v_sum = v_a + v_b;
print(v_sum)

v_a = v_a*3; #streching
v_b = v_b*0.33; #shrinking
v_sum = v_sum * -1; #reversing

print(v_a,v_b,v_sum)
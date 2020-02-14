# An example of how to create two nested lists with numerical elements and find common elements in sublists satisfying a condition.

from IPython import get_ipython
get_ipython().magic('reset -f') # clear all variables

import numpy as np

A = [[1,2,3],[1,1,2,2],[2,4,1,3]] # List of properties
B = np.array([[135,45,44],[135,135,45,45],[45,55,135,44]]) # corresponding list of arbitrary labels converted to numpy array

# to find common values within A's sublists:
result = set(A[0])
for s in A[1:]:
    result.intersection_update(s)
q = list(result)
print(result)

# To find the labels from the corresponding properties satisfying a condition
idx_of_lbls = [] # index of labels
target_sublist = [] # targeted sublist
for i in range(len(A)):
    idx_of_lbls.append([x for x,y in enumerate(A[i]) if y > 1]) # condition
    target_sublist.append([B[i][j] for j in idx_of_lbls[i]])
    rsl = set(property_asel[0])
    for s in property_asel[1:]:
        rsl.intersection_update(s)
    q = list(rsl) # resulting list of the labels which in this example should be 45

#!/usr/bin/env python
# coding: utf-8

# # Create a null vector of size 10 but the fifth value which is 1.

# In[1]:


import numpy as np
null_vector = np.zeros(10)
null_vector[4] = 1

print(null_vector)


# # Create a vector with values ranging from 10 to 49.

# In[2]:


import numpy as np
vector = np.arange(10, 50)
print(vector)


# 
# # Create a 3x3 matrix with values ranging from 0 to 8

# In[3]:


import numpy as np
matrix = np.arange(9).reshape(3, 3)
print(matrix)


# # Find indices of non-zero elements from [1,2,0,0,4,0]

# In[4]:


import numpy as np
arr = np.array([1, 2, 0, 0, 4, 0])
indices = np.nonzero(arr)

print(indices)


# # Create a 10x10 array with random values and find the minimum and maximum values.

# In[5]:


import numpy as np
arr = np.random.rand(10, 10)
min_val = arr.min()
max_val = arr.max()

print("Minimum value:", min_val)
print("Maximum value:", max_val)


# # Create a random vector of size 30 and find the mean value.

# In[8]:


import numpy as np
vector = np.random.rand(30)
mean_val = vector.mean()

print("Mean value:", mean_val)


# In[ ]:





# In[ ]:





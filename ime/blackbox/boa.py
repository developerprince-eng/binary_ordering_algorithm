import numpy as np
def orderboa(a):

  row = a.shape[0]
  col = a.shape[1]
  lst = []

  for i in a[1:]:
    sum1 = 0
    k = 3
    for item in i[1:-1]:
      item = int(item)
      sum1 = int(sum1 + item * (2 ** (col - k)))
      k = k + 1
    i[-1] = sum1
    lst.append(int(sum1))

  lst1 = sorted(lst,reverse=True)

  if lst == lst1:
    pass
  else:
    a = a[np.argsort(a[:, -1].astype(int))[::-1]]

  lst = []
  for i in a[1:]:
    i[-1] = 0
  a = a.T


  for i in a[1:-1]:
    sum1 = 0
    k=2
    for item in i[1:]:

      item = int(item)
      sum1 = int(sum1 + item * (2 ** (row - k)))
      k = k + 1
    i[-1] = sum1
    lst.append(int(sum1))

  lst1 = sorted(lst,reverse=True)

  if lst == lst1:
     pass
  else:
    a = a[np.argsort(a[:, -1].astype(int))[::-1]]

  for i in a[1:]:
    i[-1]=0
  a = a.T

  return a


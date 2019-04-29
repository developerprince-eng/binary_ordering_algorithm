import numpy as np

class BOA:
    def __init__(self):
        self.is_obj = True
    
    def convert_to_arry(self, listInput):
        arrayOutput = np.asarray(listInput, dtype=np.int32)
        return arrayOutput

    def order(self, matrix):
        row = matrix.shape[0]
        col = matrix.shape[1]
        lst = []

        for i in matrix[1:]:
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
            matrix = matrix[np.argsort(matrix[:, -1].astype(int))[::-1]]

        lst = []
        for i in matrix[1:]:
            i[-1] = 0
        matrix = matrix.T


        for i in matrix[1:-1]:
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
            matrix = matrix[np.argsort(matrix[:, -1].astype(int))[::-1]]
        for i in matrix[1:]:
            i[-1]=0
        matrix = matrix.T
        return matrix
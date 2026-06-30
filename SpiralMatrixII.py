class SpiralMatrixII(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        elif n == 1:
            return [[1]]
        else:
            #no of rows
            r = n
            #no of columns
            c = n
            #start of row
            k = 0
            #start of column
            l = 0
     #allocate a square matrix with all zeros
            matrix = [[0 for j in range(c)] for i in range(r)]
            #counter for the elements
            count = 1
            while k < r and l < c:
                #print the first row from the remaining rows
                for i in range(l, c):
                    matrix[k][i] = count
                    count += 1
                k += 1
                #print the last column from the remaining column
                for i in range(k, r):
                    matrix[i][c-1] = count
                    count += 1
                c -= 1
                #print the last row from the remaining rows
                if k < r:
                    for i in range(c-1, l-1, -1):
                        matrix[r-1][i] = count
                        count += 1
                    r -= 1
                #print the first column from the remaining column
                if l < c:
                    for i in range(r-1, k-1, -1):
                        matrix[i][l] = count
                        count += 1
                    l += 1
            return matrix
          
    
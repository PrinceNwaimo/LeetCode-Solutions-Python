class SpiralMatrix(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == None or matrix == []:
            return matrix
        else:
            #no of rows
            m = len(matrix)
            #no of columns
            n = len(matrix[0])
            #starting row
            k = 0
            #starting column
            l = 0
          #spiral order matrix
            spiral = []

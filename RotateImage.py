class RotateImage(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix == None or matrix == []:
            pass
        else:
            n = len(matrix)
            for layer in range(0, n//2):
                first = layer
                last = n - 1 - layer
                for i in range(first, last):
                    offset = i - first
                    top = matrix[first][i]
                    matrix[first][i] = matrix[last - offset][first]
                    matrix[last - offset][first] = matrix[last][last - offset]
                    matrix[last][last - offset] = matrix[i][last]
                    matrix[i][last] = top

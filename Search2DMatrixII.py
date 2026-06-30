class SearchMatrixII(object):
    def searchMatrix(self, matrix, target):         
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool         
        """
        if matrix == []:
            return False         
        else:
            no_rows = len(matrix)
            no_cols = len(matrix[0])
        if target < matrix[0][0] or target > matrix[no_rows-1][no_cols-1]:
                return False
        else:
                r = 0
                c = no_cols-1    
                while r < no_rows and c >=0:
                    if matrix[r][c] == target:
                        return True
                    elif target > matrix[r][c]:
                        r += 1
                    elif target < matrix[r][c]:
                        c -= 1
                return False
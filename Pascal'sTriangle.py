class PascalTriangle(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        result = []
        previous_row = []
        previous_row.append(1)
        result.append(previous_row)
        for i in range(0, numRows-1):
            current_row = []
            current_row.append(1)
            for j in range(0, len(previous_row) - 1):
                current_row.append(previous_row[j + 1] + previous_row[j])
            current_row.append(1)
            result.append(current_row)
            previous_row = current_row
            
        return result
    
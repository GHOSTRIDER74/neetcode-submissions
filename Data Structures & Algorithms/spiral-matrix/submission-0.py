class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # top row then increment top
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # rightmost row then decrement right
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            # check if this iteration we reached the innermost part of the matrix 
            if not (left < right and top < bottom):
                break
            # bottommost row then decrement bottom 
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # leftmost row then increment left
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
import random
class Matrix_Math :

    def __init__ (self) :
        a=1

    def create_array (self, rows, cols, init = -1) :
        matrix = []
        for x in range (rows) :
            matrix.append([])
        for x in range (rows) :
            for y in range(cols) :
                if(init == -1) :
                    matrix[x].append (random.random()*2-1)
                else :
                    matrix[x].append (init)
        return matrix

    def print_array (self, matrix) :
        for x in range (len(matrix)) :
            for y in range (len(matrix[x])) :
                print (matrix[x][y], end = " ")
            print("\n")
    
    def add_array (self, matrix_1, matrix_2) :
        result = self.create_array(len(matrix_1), len(matrix_1[0]), 0)
        for x in range (len(matrix_2)) :
            for y in range (len(matrix_2[x])) :
                result[x][y] = matrix_1[x][y] + matrix_2[x][y]
        return result

    def multiply_scalar (self, matrix, scalar) :
        result = self.create_array(len(matrix), len(matrix[0]), 0)
        for x in range(len(matrix)) :
            for y in range (len(matrix[x])) :
                result[x][y] = matrix[x][y]*scalar
        return result

    def multiply_array (self, matrix_1, matrix_2, type = '.') :
        result = []
        if type == '.' :
            result = self.create_array(len(matrix_1), len(matrix_1[0]), 0)
            for x in range(len(matrix_1)) :
                for y in range (len(matrix_1[x])) :
                    result[x][y] = matrix_1[x][y]*matrix_2[x][y]
        else :
            result = self.create_array(len(matrix_1), len(matrix_2[0]), 0)
            for x in range(len(matrix_1)) :
                for y in range(len(matrix_2[0])) :
                    for z in range (len(matrix_2)) :
                        result[x][y] = result[x][y]+ matrix_1[x][z]*matrix_2[z][y]
        return result
        
    def transpose (self, matrix) :
        result = self.create_array(len(matrix[0]), len(matrix))
        for x in range(len(matrix)) :
            for y in range(len(matrix[0])) :
                result[y][x] = matrix[x][y]
        return result

    def to_matrix (self, array) :
        result = self.create_array(len(array), 1)
        for x in range (len(array)) :
            result[x][0] = array[x]
        return result

    def apply (self, matrix, function) :
        result = self.create_array(len(matrix), len(matrix[0]))
        for x in range(len(matrix)) :
            for y in range(len(matrix[x])) :
                result[x][y] = function(matrix[x][y])
        return result

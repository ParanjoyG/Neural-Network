import matrix_math as math_ 
import math

matrix = math_.Matrix_Math()

class Network :

    def __init__ (self, str) :
        self.structure = str
        self.weights = []
        self.biases = []
        self.lr = 0.1
        for x in range (1, len(str)) :
            self.weights.append(matrix.create_array(str[x], str[x-1]))
            self.biases.append(matrix.create_array(str[x], 1))

    def feed_forward (self, inputs) :
        self.A = []
        inputs = matrix.to_matrix(inputs)
        X = inputs
        for x in range (len(self.weights)) :
            Z = matrix.add_array(matrix.multiply_array(self.weights[x], X, 'x'),self.biases[x])
            A = matrix.apply(Z, self.sigmoid)
            X = A
            self.A.append(A)
        return A

    def sigmoid (self, x) :
        return (1/(1+math.exp(-x)))

    def dsigmoid (self, x) :
        return (x*(1-x))

    def train(self, inputs, outputs) :
        guess = self.feed_forward(inputs)
        outputs = matrix.to_matrix(outputs)
        error = matrix.add_array(outputs,matrix.multiply_scalar(guess,-1))
        for x in range (len(self.structure)-2, -1, -1) :
            if(x == len(self.structure)-2) :
                error = matrix.add_array(outputs,matrix.multiply_scalar(guess,-1))
            else :
                error = matrix.multiply_array(matrix.transpose(self.weights[x+1]), error, 'x')
            derivative = matrix.apply(self.A[x], self.dsigmoid)
            intermediate = matrix.multiply_array(error, derivative)
            db = matrix.multiply_scalar(intermediate, self.lr)
            if x == 0 :
                inp = matrix.to_matrix(inputs)
            else:
                inp = self.A[x-1]
            inp = matrix.transpose(inp)
            dw = matrix.multiply_array(db, inp, 'x')
            self.weights[x] = matrix.add_array(self.weights[x],dw)
            self.biases[x] = matrix.add_array(self.biases[x], db)
        


    
        
    
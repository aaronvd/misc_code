import numpy as np

def partial(g, k, X):
    '''Takes partial derivative of function g with respect to kth component of X.'''
    h = 1e-9
    Y = np.copy(X)
    X[k] = X[k] + h
    dg = (g(X) - g(Y)) / h
    return dg

def grad(f, X, clip):
    '''Computes gradient of function f with respect to vector X.'''
    grad = []
    for i in np.arange(0, len(X)):
        grad_i = partial(f, i, X)
        if grad_i<0:
            grad_i = max(grad_i, -1*clip)
        else:
            grad_i = min(grad_i, clip)
        grad.append(grad_i)
    return grad

def descend_grad(f, X0, eta, steps, tolerance=1e-7, clip=100, quiet=True):
    i=0     # gradient descent iterations
    while True:
        if not quiet:
            if i%1 == 0:
                print('Iteration ' + str(i) + ': ' + str(X0))
        i = i+1
        X0 = X0 - eta*np.array(grad(f, X0, clip))
        if (np.linalg.norm(grad(f, X0, clip)) < tolerance) or (i > steps): 
            break
    return X0

if __name__ == '__main__':
    #### Test gradient descent
    def f(X):
        return (X[0]-20)**4 + (X[1]-25)**4
        # return X[0]**2

    X0 = [2, 30]
    eta = 0.001
    steps = 10000
    xmin = descend_grad(f, X0, eta, steps)
    print(xmin) 
from numpy import asarray
from numpy import arrange
from numpy.random import rand
from matplotlib import pyplot

def objective(x):
    return x**2.0
def derivative(x):
    return x * 2.0
def gradient_descent(objective, derivative,bounds,n_iter,step_size):
    solutions, scores = list(),list()
    solution = bounds[:,0] + rand(len(bounds)) * (bounds[:,1]-bounds[:,0])
    for i in range(n_iter):
        gradient = derivative(solution)
        solution = solution - step_size * gradient
        solution_evel = objective(solution)
        solution.append(solution)
        scores.append(solution_evel)
        print('>%d f(%s) = %.5f'%(i ,solution,solution_evel))
    return [solution,scores]
bounds = asarray([[-1.0,1.0]])
n_iter = 30
step_size = 0.1
solution,scores = gradient_descent(objective,derivative,bounds,n_iter,step_size)
inputs = arrange(bounds[0,0],bounds[0,1]+0.1,0.1)
result = objective(inputs)
pyplot.plot(inputs,result)
pyplot.plot(solution,scores,',-',color = 'red')
pyplot.show()
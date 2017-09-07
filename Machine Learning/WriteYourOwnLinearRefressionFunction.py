import numpy.random
from sympy import Symbol, Derivative
from sympy import solve, Poly, Eq, Function, exp
m=Symbol('m')
b=Symbol('b')
MIN_X = -10
MAX_X = 10
NUM_INPUTS = 50

noise = numpy.random.normal(size=NUM_INPUTS)
x1 = numpy.random.uniform(low=MIN_X, high=MAX_X, size=(NUM_INPUTS, 1))
data=[]
for num in range(NUM_INPUTS):
	data.append([x1[num][0],0.3 * x1[num][0] + 1 + noise[num]])

f=((data[0][0] * m + b) - data[0][1])**2
for num in range(1,NUM_INPUTS):
        f += ((data[num][0] * m + b) - data[num][1])**2

parderiv_m = Derivative(f,m)
parderiv_b = Derivative(f,b)
parderiv_m.doit()
parderiv_b.doit()


for i in range(0,3):
        if (parderiv_m.doit().as_coeff_add()[1][i].as_coeff_Mul())[1] == 1:
                coeffecient1m = (parderiv_m.doit().as_coeff_add()[1][i].as_coeff_Mul())[0]
for i in range(0,3):
        if (parderiv_m.doit().as_coeff_add()[1][i].as_coeff_Mul())[1] == m:
                coeffecientmm = (parderiv_m.doit().as_coeff_add()[1][i].as_coeff_Mul())[0]
for i in range(0,3):
        if (parderiv_m.doit().as_coeff_add()[1][i].as_coeff_Mul())[1] == b:
                coeffecientbm = (parderiv_m.doit().as_coeff_add()[1][i].as_coeff_Mul())[0]
for i in range(0,3):
        if (parderiv_b.doit().as_coeff_add()[1][i].as_coeff_Mul())[1] == 1:
                coeffecient1b = (parderiv_b.doit().as_coeff_add()[1][i].as_coeff_Mul())[0]
for i in range(0,3):
        if (parderiv_b.doit().as_coeff_add()[1][i].as_coeff_Mul())[1] == m:
                coeffecientmb = (parderiv_b.doit().as_coeff_add()[1][i].as_coeff_Mul())[0]
for i in range(0,3):
        if (parderiv_b.doit().as_coeff_add()[1][i].as_coeff_Mul())[1] == b:
                coeffecientbb = (parderiv_b.doit().as_coeff_add()[1][i].as_coeff_Mul())[0]

final = numpy.array([[coeffecientmm,coeffecientbm],[coeffecientmb,coeffecientbb]], dtype = 'float')
final2 = numpy.array([-coeffecient1m,-coeffecient1b], dtype = 'float')
print (numpy.linalg.solve(final,final2))




        
       
        



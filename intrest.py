# Take p, N, R as input from user
P = float(input('Please enter principal in INR :'))
N = float(input('please enter number of years : '))
R = float(input('please enter rate of intrest in %p.a.:'))

# calculate simple intrest
I = P*N*R/100

# calculate simple intrest
A = P + I

# print above resuts
print(f'simple Intrest :{I:.2f} INR')
print(f'total amount is : {A:.2f}INR')
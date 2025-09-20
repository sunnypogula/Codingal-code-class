class Employee:

    #intializing(constructor)
    def __init__(self):
        print('Employee created.')

    #Deletinf(destructor)
    def __del__(self):
        print('Destructor called , employee deleted.')

obj = Employee()
del obj
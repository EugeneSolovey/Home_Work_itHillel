import sys
print(sys.path)

# Import function from package.module
from operations.add import add
from operations.mul import mul
from operations import __version__ as operations_version

# Import module from package
# from operations import add
# from operations import mul

# Import package
# import operations.add
# import operations.mul


#from operations import *
# The same as?
# from operations import add, mul

operator_to_operation = {
    "+": add,
    "*": mul,
    #"+": operations.add.add,
    #"*": operations.mul.mul,
    #"+": add.add,
    #"+": add_operation,
    #"*": mul.mul,
}

if __name__ == "__main__":
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    operator = input("Enter operator: ")

    get_result = operator_to_operation[operator]
    print("Result:", get_result(first_number, second_number))
    print("Version of 'operations' package:", operations_version)

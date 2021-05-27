# Finite State Expression (FiniStEx) Proof of Concept
# Authored by Vishnuprasadh

from parser import parser
from validator import validator

fa_dict = {}

looper= True

print("Enter Finite State Expression:")
fa = input()
fa_dict = parser(fa, fa_dict)

print(fa_dict)

while(looper):
    print('Enter input string: Leave empty to quit')
    input_string = input()
    if input_string == "": break
    else:
        validator(input_string, fa_dict)





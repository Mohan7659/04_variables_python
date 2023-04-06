""""
Description: to find the given variables are valid or not
"""

print('hello'.isidentifier())
print("true".isidentifier())
print("is".isidentifier())
print("your".isidentifier())
print("great".isidentifier())

"""
Description:keywords and how to find keywords or not
"""
import keyword as ky
print(ky.kwlist)
print(len(ky.kwlist))

print(ky.iskeyword('while'))
print(ky.iskeyword('is'))
print(ky.iskeyword('when'))
print(ky.iskeyword('for'))
print(ky.iskeyword('and'))
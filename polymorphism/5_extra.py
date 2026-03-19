from functools import singledispatch

@singledispatch
def fun(arg):
    print("Default")

@fun.register
def _(arg: int):
    print("Integer")

@fun.register
def _(arg: str):
    print("String")

fun(10)
fun("hello")
fun(0.5)

"""
Integer
String
Default
"""
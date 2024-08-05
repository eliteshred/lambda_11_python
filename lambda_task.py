#1
def add(a,b):
    return a+b  
print(add(5,6))

#lambda function
l_add = lambda a,b : a+b
print(l_add(3,4))


#2
def even(c):
    return c % 2 == 0
print(even(8))

#lambda function
l_even = lambda c:c % 2 == 0
print(l_even(9))


# 3
def f_type(t):
    return type(t)
print(f_type("rutu"))

# lambda function
l_type = lambda t: type(t)
print(l_type(35))


# 4
def square(w):
    return w*w
print(square(4))

#lambda function
l_squa = lambda w: w*w
print(l_squa(8))


# 5
def  f_min(e,f):
    return min(e,f)
print(f_min(7,8))

# lambda function
l_min = lambda e,f:min(e,f)
print(l_min(9,5))


# 6
def f_round(g):
    return round(g)
print(f_round(6.9999))

# lambda function
l_Round = lambda g: round(g)
print(l_Round(8.080))


# 7
def f_hex(j):
    return hex(j)
print(f_hex(8))

# lambda function
l_hex = lambda j: hex(j)
print(l_hex(266))


# 8
def f_max(h,k):
        return max(h,k)
print(f_max(9,8))

# lambda function
l_max = lambda h,k: max(h,k)
print(l_max(5,4))


# 9
def f_bin(y):
    return bin(y)
print(f_bin(7))

# lambda function
l_bin = lambda y: bin(y)
print(l_bin(7))


# 10
def div(m,n):
    return m/n
print(div(9,3))

#lambda function
l_div = lambda m,n: m/n
print(l_div(8,2))




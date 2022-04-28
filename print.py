#!/usr/bin/env python3
print("Durga"+"Soft")
print("Durga \t Soft")
print(10 * "Durga")
print("Durga \n Soft")
a,b,c, = 10,20,30
print("valures are:", a, b, c)
print(f"valures are:", {a}, {b}, {c} )
#using seperator
print(a,b,c, sep='@')
print('Hello',end='')
print('Durga',end='')
print('Soft')
# Using End
print('Hello',end='::')
print('Durga',end='**')
print('Soft')
# Combination of sep and end
print(10,20,30,sep=':',end='###')
print(40,50,60,sep='::')
print(70,80,sep='**',end='@@')
print(90,100)

# print with Replacement operator
name = 'Durga'
sl = 10000
company = 'dsoft'
print('Hello {}, your Salary is {}, and your company is: {}'.format(name,sl,company))
print('Hello {0}, your Salary is {1}, and your company is: {2}'.format(name,sl,company))
# Keyword Arguments
print('Hello {n}, your Salary is {s}, and your company is: {c}'.format(n=name,s=sl,c=company))
print(f'Hello {name}, your Salary is {sl}, and your company is: {company}')

#print with formatted string
# %i - signed decimal value
# %d - signed Decimal value
# %f - float value
# %s - string value - including object list set 
a = 10
b = 20
c = 30
print('a value is: %i' %a)
print('a=%d,b=%d,c=%d' %(a,b,c))

price = 70.1234
print("The price is {}".format(price))
print("The price is %f" %price)
print("The price is %.2f" %price)
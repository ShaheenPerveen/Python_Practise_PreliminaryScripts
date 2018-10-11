!/usr/bin/env python3

import timeit

N=int(input())

# N = input()

def weird_notWeird(N):
  if(N % 2 != 0):
      print("Weird")
  elif(N % 2 == 0):
      if(2<=N<=5):
          print("Not Weird")
      elif(6<=N<=20):
          print("Weird")
      elif(N>20):
          print("Not Weird")

weird_notWeird(N)


a=int(input("enter a "))
def shorthand(a):
  while a<N:
      print("%d" % a)
      a *= a

shorthand(a)

x = int(input("enter the value of x "))
n = int(input("enter the value of n "))

def equation(x, n):
  sum=0.0
  for i in range(x, n+1):
      sum += x / i
      print("%d %6.4f" % (i, sum))

equation(x, n)

x = float(input("enter the value of x(between 0 and 1): "))
# n = int(input("enter the value of n: "))

def powerSeries(x, n):
  sum = 1.0
  n = term = 1
  while n < 100.0:
      term *= x / n
      sum += term
      n += 1
      if term < 0.0001:
          break
      print("%d %f" % (n, sum))

powerSeries(x, n)

import time

x = int(input("enter the value till which you want the multiplication table: "))

start = time.time()

def multTill10(x):
    i = 1
    while i < x+1:
        n = 1
        while n < 11:
            print("%4d" % (i * n), end=' ')
            n = n + 1
        print()
        i = i + 1
    print("-" * 50)

multTill10(x)

# timeit(multTill10(x))
end = time.time()
print("time taken is %f" %(end - start))

import numpy as np

x = int(input("enter the value till which you want the multiplication table: "))


y = np.arange(1,x+1)
n = np.arange(1,11)

start = time.time()
# print(y)
# print(n)
def multTill10_np(y, n):
    k =1
    while k < x+1:
        i = y[k-1]
        l = 1
        while l < 10:
            # print(i)
            m = n[l-1]
            # print(m)
            print("%4d" % (i * m), end=' ')
            l = l + 1
        print()
        k = k + 1
    print("-" * 50)

multTill10_np(y, n)

end = time.time()
print("time taken using np is %f" %(end - start))

n = int(input("enter the number of rows: "))

i = n
while i > 0:
    print(" " * (n-i))
    print("*" * (n-i))
    i -= 1
    
#Q: Stick Problem solution

def factorial(x):
    if x==1:
      return 1
    else:
       return x*factorial(x-1)

print(factorial(6))

"""
阶乘
5！  5*4*3*2*1
4！	   4*3*2*1
3！		 3*2*1
2！		   2*1
1！		     1

5！=5*4！
		4！=4*3！
				3！=3*2！
						2！=2*1！
								1！=1
"""

def squares_odd_sum(n):
   return sum(x*x for x in range(0,n) if x%2==1)
print(squares_odd_sum(9))

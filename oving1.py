prime = (i for i in range(2,10**100) if 0 not in ( i%j for j in range(2,int(i**0.5 + 1) )  )    )
print("\n".join([ str(next(prime)) for _ in range(1000)]), sep="", end="") 

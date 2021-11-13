def rec_mult(x,y):
    if len(str(x))==1 or len(str(y))==1:
        return x * y
    
    n = max( len(str(x)), len(str(y)) )
    n_over_2 = n // 2
    
    a = x // (10 ** n_over_2)
    b = x % (10 ** n_over_2)
    c = y // (10 ** n_over_2)
    d = y % (10 **n_over_2)
    
    ac = rec_mult(a,c)
    bd = rec_mult(b,d)
    ad = rec_mult(a,d)
    bc = rec_mult(b,c)
    
    
    return ac * (10 ** (2 * n_over_2)) + (ad + bc) * (10 ** n_over_2) + bd

def karatsuba(x,y):
    if len(str(x))==1 or len(str(y))==1:
        return x * y
    
    n = max( len(str(x)), len(str(y)) )
    n_over_2 = n // 2
    
    a = x // (10 ** n_over_2)
    b = x % (10 ** n_over_2)
    c = y // (10 ** n_over_2)
    d = y % (10 **n_over_2)
    
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    pq = karatsuba((a+b),(c+d))
    
    return ac * (10 ** (2 * n_over_2)) + (pq - ac - bd) * (10 ** n_over_2) + bd
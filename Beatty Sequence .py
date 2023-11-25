from decimal import Decimal, getcontext
from math import floor

TWO = Decimal(2)
FACTOR = Decimal("1.4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727350138462309122970249248360558507372126441214971") - Decimal(1)

def beatty_sequence(n):
    if n == 0:
        return 0
    else:
        n_prime = (FACTOR * Decimal(n)).to_integral_value()
        p = n * n_prime
        q = n * (n + 1) // 2
        r = n_prime * (n_prime + 1) // 2
        return p + q - r - beatty_sequence(n_prime)

def solution(str_n):
    getcontext().prec = 102  
    return str(beatty_sequence(int(str_n)))



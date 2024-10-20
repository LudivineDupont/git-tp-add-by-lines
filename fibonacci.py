"""
la suite de fibonacci
"""
from functools import cache

def fibo_cached(n):
    """
    en cachant les résultats, on arrive
    à une complexité linéaire
    """
    if n <= 1:
        return n
    else:
        return fibo_cached(n-1) + fibo_cached(n-2)

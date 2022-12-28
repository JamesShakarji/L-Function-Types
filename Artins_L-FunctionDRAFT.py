import numpy as np
from sympy import Poly

#Input example:
#K = NumberField(x**2 + 1, 'i')
#p = 2
#frob = frobenius_element(K, p)
#print(frob)

#p = prime number
#rho = galois representation
def artin_l_function(s, rho):
    """Compute the Artin L-function for a given Galois representation.
    Args:
        s (float): The complex number s at which to evaluate the L-function.
        rho (np.ndarray): The n x n matrix representing the Galois representation.
    Returns:
        complex: The value of the Artin L-function at s.
    """
    # Compute the trace of the representation at each prime p
    a = [np.trace(rho @ frobenius_at_p(p)) for p in primes()]

    # Compute the sum over all positive integers n
    L = 0
    for n in range(1, len(a)):
        L += a[n] * n ** (-s)

    return L

def frobenius_at_p(K, p):
    """Compute the Frobenius element at a prime p for a given number field K.
    Args:
        K (NumberField): The number field for which to compute the Frobenius element.
        p (int): The prime at which to compute the Frobenius element.
    Returns:
        Element: The Frobenius element at p.
    """
    # Compute the polynomial defining the field extension K/Q
    ext_poly = K.poly()
    
    # Compute the prime ideal of p in K
    prime_ideal = K.ideal(p)
    
    # Compute the Frobenius automorphism of K at p
    frob_aut = K.frobenius_automorphism(p)
    
    # Compute the polynomial that represents the Frobenius element in the Galois group
    frob_poly = Poly(ext_poly.subs(frob_aut), domain='ZZ')
    
    # Return the Frobenius element
    return K.galois_group().element(frob_poly, name='Frob')

def primes():
    """Generate a list of all prime numbers.
    Yields:
        int: The next prime number in the list.
    """
    n = 2
    while True:
        is_prime = True
        for j in range(2, n):
            if n % j == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1

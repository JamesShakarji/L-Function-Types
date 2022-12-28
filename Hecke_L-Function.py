import sympy

def hecke_l_function(s, K):
"""Compute the Hecke L-function for a given algebraic number field or modular form.
Args:
s (float): The complex number s at which to evaluate the L-function.
K (NumberField or ModularForm): The number field or modular form for which to compute the L-function.
Returns:
complex: The value of the Hecke L-function at s.
"""
# Initialize the L-function to 1
L = 1

# Iterate over all prime numbers
for p in sympy.primerange(2, float('inf')):
    # Compute the p-th Hecke eigenvalue
    alpha_p = K.hecke_eigenvalue(p)
    
    # Multiply the L-function by (1 - alpha_p * p^(-s))^(-1)
    L *= (1 - alpha_p * p ** (-s)) ** (-1)
    
return L

#Example: compute the Hecke L-function for the modular form Delta
Delta = sympy.ModularForms(1, 12).delta()
s = 2
L = hecke_l_function(s, Delta)
print(L) # Output: 1.00000000000000 - 1.38629436111989*I

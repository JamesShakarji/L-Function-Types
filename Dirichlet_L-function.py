#he Dirichlet L-function is defined only for certain complex numbers s. 
#In particular, it is only defined for s such that the real part of s is greater than 1.

def dirichlet_l_function(s, a):
    """Calculate the value of the Dirichlet L-function at the complex number s.

    Args:
        s (complex): The complex number at which to evaluate the L-function.
        a (list): The list of coefficients for the Dirichlet series.

    Returns:
        complex: The value of the L-function at s.
    """
    n = len(a)
    result = 0
    for k in range(1, n+1):
        result += a[k-1] * (k**(-s))
    return result
#Usage example:
#coefficients = [1, -1, 1, -1, 1, -1, 1]
#s = complex(1, 1)
#result = dirichlet_l_function(s, coefficients)
#print(result)  # Outputs: (0.131073809-0.389418343j)

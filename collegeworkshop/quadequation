import math

def find_quadratic_roots(a, b, c):
    # Calculate the discriminant
    D = b**2 - 4*a*c
    
    # Check the nature of the roots
    if D > 0:
        # Two different roots roots
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        return (root1, root2)
    elif D == 0:
        # 1 real root (double root)
        root = -b / (2 * a)
        return (root,)
    else:
        # No real roots (complex roots)
      return 

# Main program
if __name__ == "__main__":
    print("Quadratic Equation Solver")
    print("The equation is of the form ax^2 + bx + c = 0")
    
    # Input coefficients
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    # Find the roots
    roots = find_quadratic_roots(a, b, c)
    
    # Output the results
    if roots is None:
        print( " No real roots")
    elif len(roots) == 2:
        print(f"The rots are: {roots[0]} and {roots[1]}")
    elif len(roots) == 1:
        print(f"The root is:{roots[0]}")
   
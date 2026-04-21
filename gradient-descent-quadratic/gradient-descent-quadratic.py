def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Minimizes f(x) = ax^2 + bx + c using vanilla gradient descent.
    Args:
        a, b, c: Coefficients of the quadratic equation
        x0: Initial starting point for x
        lr: Learning rate (step size)
        steps: Number of iterations to perform
    Returns:
        float: The final value of x after optimization
    f(x)=ax^2+bx+c
    Use the update:x=x−lr⋅f′(x) 
    repeated steps times (where lr is the learning rate)
    """
    x = x0
    # Write code here
    for i in range(steps-1):
        gradient = 2*a*x + b
        x = x - lr*gradient
    return float(x)
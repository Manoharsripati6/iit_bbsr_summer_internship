"""
Task 3 -  Functions and Error Handling.
    ->Create a function safe_divide(a,b)
    ->handle division by zero
    ->handle handle invalid inputs
    ->return meaningful error messages
    ->add proper doc strings
"""

#function
def safe_divide(a : float, b: float)->float:
    """
    This is a function which takes 2 float/int positional arguments
    a,b and returns a divided by b.

    Arguments: a,b
    Return type: float 
    """
    try:
        c : float = a/b 
        #returning the value of c
        return c
    except ValueError:
        print("a,b should be numbers.")#handling ivalid arguments
    

def format_output(a : float,b : float,c : float)->None:
    """Function to format the output"""
    print(f"{a} / {b} = {c: .2f}")

if __name__=="__main__":
    try:
        a,b=map(int,input("enter both numbers (space seperated):").split())
        c : int= safe_divide(a,b)
        #print(safe_divide.__doc__) tried printing doc strings from the function
        format_output(a,b,c)
    except ValueError:
        print("only integer values are allowed")#handling invalid values
    except ZeroDivisionError:
        print("Cannot divide with Zero")#handling division by zero error


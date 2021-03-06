# Python Application for calculating Lagrange Polynomials of size N
# author: James Wu

def getdenominator(data, x0):
    "multiplies every coordinate by every other coordinate according to (x0-x1)(x0-x2).. etc"
    denominator = 1;
    for (x, _) in data:
            if(x == x0):  # if it's the original coordinate continue;
                continue;
            else:
                denominator *= (x0 - x);
                # print "(", x0-x,")",
   
    return denominator;

 
def getnumerator(data, x0, var):
    "gets the numerator part of lagrange interpolation, as in (var-x0)(var-x1) etc"
    numerator = 1;
    for (x, _) in data:
        if(x == x0):
            continue;
        else:
        # print "(", var, "-", x ,")",
            
            numerator *= (var - x);
    # print "";
    # print "------------------------------------------------------------------------------------------------------------------------------------"
    return numerator;

def lagrangePoly(data, var, mod):
    "returns the LaGrange polynomial solution f(var) for a set of data"
    total = 0;
    for (x, y) in data:
        # print y, "*",
        num = getnumerator(data, x, var) % mod;
        den = getdenominator(data, x) % mod;
        print num, "/", den;
        
        total = (total + (y * num / den) % mod) % mod;
        
        print "\n";

    return total % mod;


main();

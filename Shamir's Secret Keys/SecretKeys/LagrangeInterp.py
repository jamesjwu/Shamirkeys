# Python Application for calculating Lagrange Polynomials of size N
#author: James Wu
def main():
    
    data = [(116, 5340342343456180831716311918824435227733),
(68, 4694834529111866497642094185471120980099),
(47 , 2985558448356350949342309936054043944717),
(109,    1924442166563347280190854585251876135818),
(62  ,  748595560968274268300719321058251857908),
(25   , 3726790694526994731286288457224202585450),
(79,    2048230071713270354249199930501256851462),
(8  ,  5327131394704077116476117334104026493182),
(111 ,   3080335949645119178852125329439258895211),
(107  ,  2648025329166058715617847942200476539559),
(104   , 5936958858466307424729425256233373932572),
(80    ,4549544863191746965234110952607268201560),
(39   , 3712674476053764452392069862783944354556),
(6    ,123666423930744881600856641172365180327),
(20   , 926512713765690765728997985916608045763),
(74   , 5652379616125941885220848029716944416202)];
    
    print lagrangePoly(data, 0, 5992830235524142758386850633773258681119);
    """
    data = [(0,1), (0,2), ];
    print lagrangePoly(data, 0,5);
    """
def getdenominator(data, x0):
    "multiplies every coordinate by every other coordinate according to (x0-x1)(x0-x2).. etc"
    denominator = 1;
    for (x,_) in data:
            if(x == x0): #if it's the original coordinate continue;
                continue;
            else:
                denominator *= (x0-x);
                print "(", x0-x,")",
   
    return denominator;

 
def getnumerator(data, x0, var):
    "gets the numerator part of lagrange interpolation, as in (var-x0)(var-x1) etc"
    numerator = 1;
    for (x, _) in data:
        if(x == x0):
            continue;
        else:
            print "(", var, "-", x ,")",
            
            numerator *= (var-x);
    print "";
    print "------------------------------------------------------------------------------------------------------------------------------------"
    return numerator;

def lagrangePoly(data, var,mod):
    "returns the LaGrange polynomial solution f(var) for a set of data"
    total = 0;
    for (x,y) in data:
        print y, "*",
        total += (((y * getnumerator(data,x,var)%mod)) / ((getdenominator(data,x))%mod))%mod;
        
        print "\n";

    return total%mod;


main();
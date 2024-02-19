# integer, float, bool
a =10
b =10.1

print ("les bool sont-il une sous classe de int ?\n",issubclass(bool,int),'\n')
print(a,b,'\n')

# tout les objets peuvent être vrai ou faux 
print('je t\'aime en bouléen est :',bool("je t'aime"),'\n')
print(type(a),type(b))

# transformer les types natifs
int(True)
float(2)

# troncature des float vers int 
int(2.0)
int(2.1)
int(2.5)
int(2.6)

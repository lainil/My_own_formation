# les noms pointent sur les object pendant une session ouverte (ca marche dans le terminal mais pas en executant deux fois le script)

nom=5
print(id(nom))
nom_2=nom
print(id(nom_2))

# les nom de variable pointent sur les objets déclarés
id (500)
id (500) # il y a eu une update, les int sont devenu des singleton

#python garde en mémoire le dernier object créée

#affectation simple 
a=2
b=3

#affectation parallèles
a,b=2,3
#inversion
a,b=b,a

#affectation multiple 
a=b=c=3
#not valide 
#a=3=b

#nommage des nom de varialble 
a=4
a.bit_length()
a.to_bytes(length=4,byteorder='big')
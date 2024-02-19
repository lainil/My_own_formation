#changer bonjour par bonsoir
phrase = "Bonjour tout le monde."
start_phrase,middle_phrase,end_phrase =phrase.partition("jour")
nouvelle_phrase=start_phrase + "soir" + end_phrase
print(nouvelle_phrase)

#compter le nombre d'occurences"
lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
resultat = phrase.lower().count(lettre_a_chercher)
print (resultat)

#compter le nombre de phrases
lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
		   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
		   Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
		   Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
		   
resultat = lorem.count(".")
print(resultat)


#ordonner un chaine de caractère
chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine=chaine.split(", ")
chaine.sort()
chaine=', '.join(chaine.sort)
print(chaine)
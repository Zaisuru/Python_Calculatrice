# Creation d'une calculatrice sur python en ligne de commande

a = b = ""

while not (a.isdigit() and b.isdigit()):
    a = input("Veuillez entrer un premier nombre")
    b = input("Veuillez entrer un deuxieme nombre")

    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer un nombre valide")
print (f"Le result de {a} et de {b} est égal à {int(a) + int(b)}")

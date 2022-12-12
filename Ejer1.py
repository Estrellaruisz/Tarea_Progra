
dato = True
while (dato):
    print("Menu de recomendaciones")
    print(" 1. Literatura")
    print(" 2. Cine")
    print(" 3. Musica")
    print(" 4. Videojuegos")
    print(" 5. Salir")
    Op=int(input("Elija una opciom(1-5): "))
    if Op == 1:
        print("Lecturas recomendables :")
        print("+ Esperando a Tito y otros cuentos de futbal(Eduardo Sacheri)")
        print("+ El juego de Ender (Orson Scott Card)")
        print("+ El sueño de los heroes(Adolfo Bioy Casares)")
    elif Op == 2:
        print("Películas recomendables:")
        print(" + Matrix (1999)")
        print(" + El último samuray (2003)")
        print(" + Cars (2006)")
    elif Op == 3:
        print("Discos recomendables:")
        print(" + Despedazado por mil partes (La Renga, 1996)")
        print(" + Búfalo (La Mississippi, 2008)")
        print(" + Gaia (Mägo de Oz, 2003)")
    elif Op == 4:
        print("Videojuegos clásicos recomendables")
        print(" + Día del tentáculo (LucasArts, 1993)")
        print(" + Terminal Velocity (Terminal Reality/3D Realms, 1995)")
        print(" + Death Rally (Remedy/Apogee, 1996)")
    elif Op == 5:
        print("Gracias, vuelva prontos")
        dato = False

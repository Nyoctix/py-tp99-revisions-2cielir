# =====================================================
#  Mission 5 - Analyser un motif
# =====================================================
# Le motif est fourni. Vous devez le mesurer.
# Affichages attendus, dans cet ordre et avec exactement ce texte :
#   LED allumees : ...
#   Courant total : ... mA
#   Ligne la plus allumee : i (n LED)
#   Colonne la plus allumee : j (n LED)
# En cas d'egalite, on garde la plus petite ligne / colonne.

TAILLE = 8
COURANT_LED = 20   # milliamperes consommes par une LED allumee

# --- motif fourni : ne pas modifier ---
matrice = [
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
]

# --- affichage du motif (donne) ---
for i in range(TAILLE):
    texte = ""
    for j in range(TAILLE):
        if matrice[i][j] == 1:
            texte = texte + "# "
        else:
            texte = texte + ". "
    print(texte)

print()

# --- 1. nombre total de LED allumees ---
# TODO
Led_On = 0
for i in range(TAILLE):
    texte = ""
    for j in range(TAILLE):
        if matrice[i][j] == 1:
            Led_On += 1

print( "Nombre de led allumée :", Led_On )


# --- 2. courant total consomme (en mA) ---
# TODO
print("Total en mA :", Led_On*COURANT_LED)

# --- 3. ligne la plus allumee ---
# TODO : compter les LED de chaque ligne et retenir la meilleure
record_led = 0
Max_On_C = 0
for i in range(TAILLE):
    Led_On = 0
    for j in range(TAILLE):
        if matrice[i][j] == 1:
            Led_On += 1
    if Led_On > record_led:
        record_led = Led_On
        Max_On_C = i
print("Ligne la plus allumee : ", most_allumed_line, "(", record_led, "LED)")


# --- 4. colonne la plus allumee ---
# TODO : attention, ici la boucle des colonnes est a l'exterieur
record_led = 0
Max_On_L = 0
for j in range(TAILLE):
    Led_On = 0
    for i in range(TAILLE):
        if matrice[i][j] == 1:
            Led_On += 1
    if Led_On > record_led:
        record_led = Led_On
        Max_On_L = j
print("Colonne la plus allumee : ", most_allumed_line, "(", record_led, "LED)")
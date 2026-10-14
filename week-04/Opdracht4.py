# Opdracht - Weapon Selector
#
# Je gaat een programma maken waarin een speler een wapen kan kiezen.
# Ieder wapen heeft zijn eigen damage en een speciale eigenschap.
#
# Stap 1 - Variabelen
# Maak de volgende variabelen aan:
# - Een variabele voor de naam van de speler
# - Een variabele voor het gekozen wapen
# - Een variabele voor de damage van het wapen
#
# Geef de speler zelf een naam en kies alvast een wapen.
#
# LET OP:
# Gebruik voor alle variabelen de juiste Python naming conventions!
# Bijvoorbeeld: player_name in plaats van playerName.


#geeft de speler naam type wapen en de damge van het wapen mee
player_name = "Joris"
weapon_choice = "Sword"
weapon_damage = 0
enemy_health = 100

# Stap 2 - Match Case
# Gebruik een match case om te controleren welk wapen de speler heeft.
#
# De speler kan kiezen uit de volgende wapens:
#
# Sword:
# - Doet 20 damage
# - Print "Je gebruikt een zwaard!"
#
# Bow:
# - Doet 15 damage
# - Print "Je gebruikt een boog!"
#
# Staff:
# - Doet 25 damage
# - Print "Je gebruikt een magische staf!"
#
# Axe:
# - Doet 30 damage
# - Print "Je gebruikt een bijl!"
#
# Zorg ervoor dat de damage variabele de juiste waarde krijgt.
#
# Als de speler een onbekend wapen heeft gekozen:
# - Zet de damage op 0
# - Print "Onbekend wapen!"
#
# TIP:
# Gebruik case _ voor een onbekende waarde.

# maak aan behand van een match case welk wampen gekozen is en print dat en daarna was hij de damage mee voor dat wapen 
match weapon_choice:
    case "Sword":
        print("Je gebruikt een zwaard!")
        weapon_damage = 20
    case "Bow":
        print("Je gebruikt een boog!")
        weapon_damage = 15
    case "Staff":
        print("Je gebruikt een magische staf!")
        weapon_damage = 25
    case "Axe":
        print("Je gebruikt een bijl!")
        weapon_damage = 30
    case "Pistol":
        print("Je gebruikt een pistool!")
        weapon_damage = 50
    case "Grenade":
        print("Je gebruikt een granaat!")
        weapon_damage = 40
    case _ :
        print("Onbekend wapen!")
        weapon_damage = 0

# Stap 3 - Resultaat printen
# Print na de match case de volgende informatie:
#
# Speler: Steve
# Wapen: Sword
# Damage: 20
#
# Zorg ervoor dat de informatie uit je variabelen komt.

# print de uitkomst in de terminal
print(f"Speler: {player_name}")
print(f"Wapen: {weapon_choice}")
print(f"Damege: {weapon_damage}")

# Stap 4 - Comments
# Voeg minimaal 3 eigen comments toe aan je programma.
#
# Leg met deze comments uit:
# - Wat een bepaald stuk code doet
# - Waarom je een match case gebruikt
# - Wat er gebeurt als het wapen niet bestaat
#
# Schrijf duidelijke comments die iemand anders helpen
# om jouw code te begrijpen.


# Stap 5 - Naming Conventions
# Controleer of je code voldoet aan de Python naming conventions.
#
# - Gebruik snake_case voor variabelen
# - Gebruik duidelijke Engelse namen
# - Begin variabelen met een kleine letter
# - Gebruik geen spaties in variabelenamen
#
# FOUT: playerDamage = 20
# GOED: player_damage = 20
#
# FOUT: x = "Sword"
# GOED: selected_weapon = "Sword"


# BONUS 1
# Voeg zelf minimaal 2 nieuwe wapens toe aan je match case.
# Bedenk voor ieder wapen een eigen damage en beschrijving.


# BONUS 2
# Maak een variabele enemy_health met de waarde 100.
# Laat de speler 3 keer aanvallen met zijn gekozen wapen.
#
# Gebruik hiervoor een for-loop.
#
# Print na iedere aanval hoeveel health de vijand nog heeft.
# Zorg ervoor dat de health niet onder de 0 komt.

for i in range(0,3):
    enemy_health = enemy_health - weapon_damage
    if enemy_health <= 0:
        enemy_health = 0
    print(f"de vijand heeft nog: {enemy_health}")

# BONUS 3
# Gebruik een while-loop om de vijand aan te vallen
# totdat de vijand geen health meer heeft.
#
# Print daarna "Vijand verslagen!"
enemy_health = 100

while enemy_health != 0:
    enemy_health = enemy_health - weapon_damage
    if enemy_health <= 0:
            enemy_health = 0
    if enemy_health != 0:
        print(f"de vijand heeft nog: {enemy_health}")
print("Vijand verslagen!")

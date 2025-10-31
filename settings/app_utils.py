from colorama import Fore, Style, init
import os
init()

def parse_str(question=None,*,  enter_quit = False):
    """Analyse une chaîne de caractères et demande la saisie si elle est vide"""
    var = ""
    while var == "":
        if enter_quit:
            var = input(f"{question} (i pour ignorer): ")
            if var == "i":
                return
        else:
            var = input(f"{question}: ")
    return var.strip(" ")


def select(array, attribute=None):
    """Analyse une liste de tâches ou de listes de tâches pour identifier une tache/liste de tache"""
    if attribute == None:
        for i, element in enumerate(array):
            print(f"{i+1}- {element}")
    else:
        for i, entity in enumerate(array):
            print(f"{i+1}- {getattr(entity, attribute)}")
    choice = int(parse_str("Choisissez un numéro"))
    return array[choice-1]

def to_color(color , text):
    colors = {
        "red": Fore.RED,
        "green":Fore.GREEN,
        "blue": Fore.BLUE,
        "cyan":Fore.CYAN,
        "reset": Style.RESET_ALL
    }
    if color in colors:
        return colors[color] + text + colors["reset"]
    
def parse_entry(menu: dict, /):
    print("="*40)
    print("|"+"-"*15+" "*2+"MENU"+" "*2+"-"*15+"|")
    print("="*40)
    for i in menu:
        print(f"{i} -> {menu[i][0]}")
    option = parse_str("Choisissez un nombre")
    for i in menu:
        if option == i:
            return i
    print(f"Attention! Vous devez entrer un nombre entre {min(menu)} et {max(menu)}")
    return parse_entry(menu)


def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def check_none(entry):
    if entry == " ":
        return False
    return True
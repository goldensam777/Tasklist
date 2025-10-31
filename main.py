from settings.manager import *
from settings.app_utils import parse_str, parse_entry, to_color
import time
init()
COLOR = Fore.CYAN
RESET = Style.RESET_ALL

gestionnaire = TasklistManager()
menu_du_gestionnaire = {
    "1": ("Créer une liste de tâches", gestionnaire.create_tasklist),
    "2": ("Ajouter une tâche", gestionnaire.add_task_to_tasklist),
    "3": ("Voir toutes les listes de tâches", gestionnaire.list_all_tasklists),
    "4": ("Marquer une tâche comme terminée", gestionnaire.mark_done),
    "5": ("Quitter le gestionnaire des tâches", gestionnaire.go_threading)
}
def main():
    # nom de l'utilisteur
    nom = parse_str("Votre nom")
    clear_screen()
    print(to_color("blue", f"Salut {nom.capitalize()}! Bienvenue dans le Gestionnaire des tâches."))
    print()
    while True:
        # menu du gestionnaire & recuperation de l'option choisie
        option = parse_entry(menu_du_gestionnaire)
        clear_screen()
        parametre = menu_du_gestionnaire[option][0].capitalize()
        operation = menu_du_gestionnaire[option][1]
        print(f"Vous avez choisi l'option {parametre}")
        print("\n")

        # lancement de l'operation 
        operation()

main()
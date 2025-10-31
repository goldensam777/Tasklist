import json
from .tasklist import *
from .app_utils import *

class TasklistManager:
    def __init__(self):
        self.list_of_tasklists = []
    

    @property
    def store_data(self):
        """Enregistrer les données avant la mise en arrière plan"""
        # with open("tasklist_manager.json", "w") as file:
        #     json.dump(self.data, file, indent=4)
        pass


    @property
    def load_data(self):
        """Charge les données au relancement du processus"""
        # with open("tasklist_manager.json", "r") as file:
        #     data = json.load(self.data, file, indent=4)
        pass


    def list_all_tasklists(self):
        """Affiche toute les taches"""
        if self.tasklist_exists():
            print("Liste de toutes les listes des taches")
            for tasklist in self.list_of_tasklists:
                tasklist.list_tasks
        return

    def create_tasklist(self):
        """
        Crée une nouvelle liste de tâches
        Retourne True si la création a réussi, False sinon
        """
        try:
            tasklist_name = parse_str("Nom de la liste des tâches", enter_quit=True)
            if tasklist_name is None:
                tasklist_name = f"Liste des tâches {len(self.list_of_tasklists)+1}"
            
            # Vérifier si une liste avec le même nom existe déjà
            if any(tl.name.lower() == tasklist_name.lower() for tl in self.list_of_tasklists):
                print(to_color("yellow", f"Une liste nommée '{tasklist_name}' existe déjà."))
                return False
                
            tasklist = Tasklist(tasklist_name)
            self.list_of_tasklists.append(tasklist)
            print(to_color("green", f"✓ Liste '{tasklist.name}' créée avec succès."))
            return True
            
        except KeyboardInterrupt:
            print("\nCréation de liste annulée.")
            return False
        except Exception as e:
            print(to_color("red", f"Erreur lors de la création de la liste: {e}"))
            return False


    def add_task_to_tasklist(self):
        """
        Ajoute une tâche à une liste existante
        Retourne True si l'ajout a réussi, False sinon
        """
        if not self.tasklist_exists():
            return False
            
        try:
            tasklist = select(self.list_of_tasklists, 'name')
            if tasklist is None:
                print(to_color("yellow", "Aucune liste sélectionnée."))
                return False
                
            return tasklist.add_task()
            
        except KeyboardInterrupt:
            print("\nAjout de tâche annulé.")
            return False
        except Exception as e:
            print(to_color("red", f"Erreur lors de l'ajout de la tâche: {e}"))
            return False


    def mark_done(self):
        """
        Marque une tâche comme terminée
        Retourne True si l'opération a réussi, False sinon
        """
        if not self.tasklist_exists():
            return False
            
        try:
            tasklist = select(self.list_of_tasklists, 'name')
            if tasklist is None:
                print(to_color("yellow", "Aucune liste sélectionnée."))
                return False
                
            return tasklist.mark_done()
            
        except KeyboardInterrupt:
            print("\nOpération annulée.")
            return False
        except Exception as e:
            print(to_color("red", f"Erreur lors du marquage de la tâche: {e}"))
            return False
    

    def go_threading(self):
        """Permet au processus de s'èxecuter en arrière plan """
        pass


    def define_recurrence(self):
        """Permet au gestionnaire de redéfinir les tâches recurrente"""
        pass

    def tasklist_exists(self):
        """
        Vérifie s'il existe au moins une liste de tâches
        Retourne True si oui, False sinon
        """
        if not self.list_of_tasklists:
            print(to_color("yellow", "Aucune liste de tâches n'existe encore."))
            print("Veuillez d'abord créer une liste de tâches.")
            return False
        return True
    
    def task_exists(self):
        """
        Vérifie s'il existe au moins une tâche dans une liste
        Retourne True si oui, False sinon
        """
        if not self.tasklist_exists():
            return False
            
        for tasklist in self.list_of_tasklists:
            if tasklist.tasklist:  # Si la liste n'est pas vide
                return True
                
        print(to_color("yellow", "Aucune tâche n'existe dans les listes."))
        return False
from .app_utils import *
from .task import *


class Tasklist:
    """Représente une liste de tâches"""

    def __init__(self, name=""):
        """Initialise une nouvelle liste de tâches"""
        self.name = name
        self.tasklist: list[Task] = []
    

    @property
    def list_tasks(self):
        """Affiche toutes les tâches de la liste"""
        print(f"--{self.name}")
        for task in self.tasklist:
            task.present_yourself
    
    def find_task(self):
        """
        Trouve une tâche dans la liste
        Retourne la tâche si trouvée, None sinon
        """
        if not self.tasklist:
            print(to_color("red", "Aucune tâche dans la liste."))
            return None
            
        try:
            task = select(self.tasklist, 'name')
            if task is None:
                print(to_color("yellow", "Aucune tâche sélectionnée."))
            return task
        except Exception as e:
            print(to_color("red", f"Erreur lors de la recherche de la tâche: {e}"))
            return None

    def add_task(self):
        """Ajoute une nouvelle tâche à la liste"""
        try:
            name = parse_str("Nom de la tâche", enter_quit=True)
            if name is None:
                name = f"Tâche {len(self.tasklist)+1}"
                
            task = Task(name)
            self.tasklist.append(task)
            print(to_color("green", f"✓ Tâche '{task.name}' ajoutée avec succès."))
            return True
            
        except KeyboardInterrupt:
            print("\nCréation de tâche annulée.")
            return False
        except Exception as e:
            print(to_color("red", f"Erreur lors de l'ajout de la tâche: {e}"))
            return False

    def mark_done(self):
        """Marque une tâche comme terminée"""
        task_found = self.find_task()
        if task_found is None:
            print(to_color("yellow", "Aucune tâche sélectionnée ou liste vide."))
            return False
            
        try:
            task_found.done = True
            print(to_color("green", f"✓ Tâche '{task_found.name}' marquée comme terminée."))
            return True
        except Exception as e:
            print(to_color("red", f"Erreur lors du marquage de la tâche: {e}"))
            return False
        

    
    def remove_task(self):
        """Supprime une tâche de la liste"""
        if not self.tasklist:
            print(to_color("yellow", "La liste des tâches est vide."))
            return False
            
        task_to_remove = self.find_task()
        if task_to_remove is None:
            return False
            
        try:
            confirm = input(f"Êtes-vous sûr de vouloir supprimer la tâche '{task_to_remove.name}' ? (o/n): ").lower()
            if confirm == 'o':
                self.tasklist.remove(task_to_remove)
                print(to_color("green", f"✓ Tâche '{task_to_remove.name}' supprimée avec succès."))
                return True
            else:
                print("Suppression annulée.")
                return False
        except ValueError:
            print(to_color("red", "Erreur: Tâche introuvable dans la liste."))
            return False
        except Exception as e:
            print(to_color("red", f"Erreur lors de la suppression de la tâche: {e}"))
            return False
    


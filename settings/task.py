"""
What is a task ?

A task is a piece of work that has to be done, an objective to be attained.
Task:
    - Name
    - Date
    - Time if necessary
    - Recurrence
    - State: done/undone
"""
import datetime

from .app_utils import *

init()


class Task:
    """Defining the piece of work that has to be done, or the objective to be attained."""
    def __init__(self, name="", done=False):
        self.name = name
        self.date = self.manage_date()
        self.time = self.manage_time()
        self.recurrent = self.set_recurrence()
        self.done = done
        self.state = self.get_state()
        self.present_yourself

    @property
    def present_yourself(self):
        print(Fore.BLUE + f"*{self.name} - {self.date} @ {self.time}, {self.state}." + Style.RESET_ALL)


    def get_state(self):
        state =(Fore.RED + f"Inachevé" + Style.RESET_ALL)
        if self.done:
            state = (Fore.BLUE + f"Terminé" + Style.RESET_ALL)
        return state

    def manage_date(self, provided_date=None):
        """
        Demande la date de la tâche et retourne un objet datetime.date
        Gère les erreurs de format et de date invalide
        """
        if provided_date is not None:
            return provided_date
            
        while True:
            try:
                usr_input = input("Date (JJ-MM-AAAA) (entrer pour aujourd'hui) : ").strip()
                
                if not usr_input:
                    print("Date non fournie. Utilisation de la date d'aujourd'hui.")
                    return datetime.date.today()
                    
                if '-' not in usr_input:
                    raise ValueError("Format de date invalide. Utilisez JJ-MM-AAAA")
                    
                day, month, year = map(int, usr_input.split('-'))
                
                # Validation de la date
                if year < 1000 or year > 9999:
                    raise ValueError("L'année doit être sur 4 chiffres")
                if month < 1 or month > 12:
                    raise ValueError("Le mois doit être entre 01 et 12")
                    
                # Vérification que le jour est valide pour le mois
                max_day = 31
                if month in [4, 6, 9, 11]:
                    max_day = 30
                elif month == 2:
                    max_day = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
                    
                if day < 1 or day > max_day:
                    raise ValueError(f"Jour invalide pour le mois spécifié (doit être entre 1 et {max_day})")
                    
                date_obj = datetime.date(year, month, day)
                
                # Vérifier que la date n'est pas dans le passé
                if date_obj < datetime.date.today():
                    print("Attention : La date est dans le passé.")
                    confirm = input("Voulez-vous continuer ? (o/n): ").lower()
                    if confirm != 'o':
                        continue
                        
                return date_obj
                
            except ValueError as e:
                print(f"Erreur : {e}")
                print("Veuillez réessayer. Format attendu : JJ-MM-AAAA")
            except Exception as e:
                print(f"Erreur inattendue : {e}")
                print("Veuillez réessayer ou appuyez sur Ctrl+C pour annuler")
                date = datetime.date(year, month, day)
                today = datetime.datetime.today().date()
                if today > date:
                    print("Entrez une date valide!")
                    return self.manage_date()
                return date
            except ValueError:
                print("Entrée Invalide, veuillez réessayer.")
                return self.manage_date()
            
    
    def manage_time(self):
        """Asks the user's task's date and returns a datetime.time object"""
        time = ""
        if not time:
            usr_input = input("Heure(hh:mm): ")
        else:
            usr_input = time
        try:
            usr_input_split = usr_input.split(":")
            hour, minute = [int(e) for e in usr_input_split]
            time = datetime.time(hour, minute).isoformat("minutes") # la date entrée par l'utilisateur
            real_time = datetime.datetime.today().time().isoformat("minutes") # la date d'aujourd'hui 

            if ((time < real_time) and self.date == datetime.datetime.today().date()): 
                print("Entrez l'heure à venir, cette heure est déjà passée.")
                return self.manage_time()
            return time
        except ValueError: # Entrée Invalide
            print("Entrée Invalide, veuillez Réessayer.")
            return self.manage_time()
        
    def replan(self):
        change = input("Voulez vous changer la date?(o/n) ")
        if change.lower() == "o":
            self.date = self.manage_date()
            self.time = self.manage_time()

    
    def set_recurrence(self):
        ask_set = parse_str("Est-ce une tâche récurrente?(o/n) ")
        if ask_set == "o":
            return True
        return
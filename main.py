import datetime as dt
import time
from colorama import init, Fore, Style
import os 

def clear_screen():
    command= "" 
    if os.name == "posix":
        command= "clear"
    else:
        command="cls"
    os.system(command)

# colorama
init(autoreset=True)
# CONSTANTS 
MAX_NUMBER_OF_TASKLISTS = 5

todays_date = dt.date.today()
complete_time = time.asctime().upper()
print("Today's date:", complete_time)

class Task:
    def __init__(self, name="", date_of_operation=todays_date):
        self.done= False
        self.name = name
        self.date_of_operation = date_of_operation
        self.Presentation()

    def SetDate(self):
        """
        This structure mainly depends on the datetime module 
        """
        pass

    def SetState(self):
        """
        This structure mainly depends on the datetime module at the time the user is supposed to do the task
        """
        self.done = True
    
    def Presentation(self):
        if self.done == False:
            self.state = Fore.RED + "Undone"+ Style.RESET_ALL
        else:
            self.state= Fore.GREEN + "Done"+ Style.RESET_ALL

        print(f"* {self.name} - ({self.date_of_operation}): {self.state} \n" )

    def SetRegularity(self):
        # (Monthly, Weekly or Daily @ seriously, for later)
        pass
    
    def Replan(self):
        self.date_of_operation 
        pass

class TaskList:
    def __init__(self, name="", tasklist=None):
        self.name = name
        self.SetName()
        self.tasklist = tasklist or []

    def SetName(self):
        self.name = input("Name? > ").capitalize()
        print()
            
    def CreateTask(self):
        while True:
            taskname = input("Task?(enter to finish) >")
            taskname.capitalize()
            if taskname=="":
                return
            self.tasklist.append(Task(taskname))
            print()
        # set the date option after learning datetime module, for now its by default today's date
        
    def TellTasksOfTaskList(self):
        tell_len = "tasks" if len(self.tasklist)>1 else "task"
        print(f"Tasklist {self.name}, {len(self.tasklist)} {tell_len} left.")
        print()
        for task in self.tasklist:
            task.Presentation()
            print()
    
    def MarkTask(self):
        for i, task in enumerate(self.tasklist):
            print(f"{i+1}. {task.name}")
        select_number = int(input(Fore.CYAN + "<Number? > "+ Style.RESET_ALL))
        task_sel = self.tasklist[select_number-1] 
        task_sel.SetState()
        task_sel.Presentation()
            

# App Code Main Block
list_of_tasklists = []
  # like a checker, right? Would not try to implement yet 
        # if not list_of_tasklists:
        #     print(Fore.RED+"There are no tasklists set yet. Please Create."+Style.RESET_ALL)
        #     return None


def show_menu_and_collect_input(menu_arr):
    print("_"*8 + "Menu" + "_"*8)
    for i in menu_arr:
        print(f"{i}- {menu_arr[i][0]}")
    print()
    user_input = input("Option? >")

    if user_input.strip() in {"1", "2", "3", "4", "5"}:
        return int(user_input)
    else:
        print("Invalid Option. Please Try Again.")
        print()
        return show_menu_and_collect_input(menu_arr)


def create_tasklists_in_list():
    clear_screen()
    tasklist_lenght = len(list_of_tasklists)
    if tasklist_lenght >= MAX_NUMBER_OF_TASKLISTS:
        print(Fore.RED + f"You have already {MAX_NUMBER_OF_TASKLISTS} lists."+Style.RESET_ALL)
        return
    tasklist = TaskList()
    list_of_tasklists.append(tasklist)
    print(Fore.BLUE+f"Tasklist {tasklist.name} Created. You now have "+ str(len(list_of_tasklists))+" tasklists."+Style.RESET_ALL)
    

def create_new_tasks():
    clear_screen()
    if not list_of_tasklists:
        print(Fore.RED+"There are no tasklists set yet. Please Create."+Style.RESET_ALL)
        return
    print("Select a list: ")
    for i, tasklist in enumerate(list_of_tasklists):
        print(f"{i+1}. {tasklist.name}")
    select_number = int(input(Fore.CYAN + "<Number? > "+ Style.RESET_ALL))
    task_l_sel = list_of_tasklists[select_number-1]
    task_l_sel.CreateTask()
    task_l_sel.TellTasksOfTaskList()


def show_all_tasklists():
    clear_screen()
    if not list_of_tasklists:
        print(Fore.RED+"There are no tasklists set yet. Please Create."+Style.RESET_ALL)
        return
    print()
    for i, tasklist in enumerate(list_of_tasklists):
        print(f"{i+1}. {tasklist.name}")
        tasklist.TellTasksOfTaskList()


def mark_task_done():
    clear_screen()
    if not list_of_tasklists:
        print(Fore.RED+"There are no tasklists set yet. Please Create."+Style.RESET_ALL)
        return
    print("Select a list: ")
    for i, tasklist in enumerate(list_of_tasklists):
        print(f"{i+1}. {tasklist.name}")
    select_number = int(input(Fore.CYAN + "<Number? > "+ Style.RESET_ALL))
    task_l_sel = list_of_tasklists[select_number-1]
    task_l_sel.MarkTask()


def quit_program():
    clear_screen()
    raise SystemExit("Goodbye! :)")

app_menu = {
        1:("Create a new tasklist", create_tasklists_in_list),
        2:("Create a new task", create_new_tasks),
        3:("Show all taskslists", show_all_tasklists),
        4:("Mark a task done", mark_task_done),
        5:("Quit", quit_program)
            }

def main():
    while True:
        user_input = show_menu_and_collect_input(app_menu)
        opt_select = app_menu[user_input][1]
        opt_function = opt_select
        opt_function()
        print()

        
if __name__ == "__main__":
    main()

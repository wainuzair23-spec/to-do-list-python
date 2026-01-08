import os
import json
from datetime import datetime


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def save_tasks(tasks):
  with open("tasks.json" , "w") as f:
    json.dump(tasks, f)
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            content = f.read().strip()
            if not content: 
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
       
        return []
  
  



tasks=[]
def add_task(tasks):
   clear_screen()
   t=int(input("How many tasks you want to add : "))
   i=1
   clear_screen() 
   while (i<=t):
     clear_screen() 

     task_name=input("Enter your task : \n\n\t\t")
     time_added = datetime.now().strftime("%d-%b-%Y %I:%M %p")
     task = {"task": task_name, "time": time_added , "done" : False}
     
     tasks.append(task)
     
     
     input("\n__--Press Enter to continue--__ ") 
     clear_screen()
     i=i+1
   
   for j, task in enumerate(tasks, start=1):
    print(f"{j}. ✅ {task['task']} — added on {task['time']}")
   save_tasks(tasks)

   input("\n__--Press Enter to continue--__")
   clear_screen() 

def view_task(tasks):
    

    if len(tasks) == 0:
        print("📭 No tasks yet!\n")
        input("__--Press Enter to continue--__")
        clear_screen()
    else:
        
        print("\n📋 Your Tasks :\n")
        for i, task in enumerate(tasks, start=1):
            status = "✅ Done" if task['done'] else "❌ Pending"
            print(f"{i}. {task['task']} — added on {task['time']} — {status}")
        input("\n__--Press Enter to continue--__")
        clear_screen()    
     

def mark_task(tasks):
  

  while True:
        
        if len(tasks)==0:
           print("\t\t\tMark Task as done Task option selected\n\n")
           print("📭 No tasks yet!\n")
           input("__--Press Enter to continue--__")
           clear_screen()
           break
        else: 
             print("\t\t\tMark Task as done Task option selected\n\n")  
             print("\n📋 Your Tasks :\n")
             for i, task in enumerate(tasks, start=1):
                status = "✅ Done" if task['done'] else "❌ Pending"
                print(f"{i}. {task['task']} — added on {task['time']} — {status}")

             marker = int(input("\nEnter task number (0 to exit): "))
             if marker==0:
                break
             if 1 <= marker <=len(tasks)  :
                if tasks[marker - 1]["done"] == True:
                 
                 print("\n❌ This task already has marked as done! ")
                 input("__--Press Enter to continue--__")
                 clear_screen()
                 continue
                else: 
                 
                 tasks[marker - 1]["done"] = True
                 print(f"\n✅ '{tasks[marker-1]['task']}' marked as completed")
                 save_tasks(tasks)
                 
                 input("__--Press Enter to continue--__")
                 clear_screen()
             else:
                print("\n⚠️ Invalid task number.")
                input("__--Try again!--__")
                clear_screen()
                continue  
       
  save_tasks(tasks)





def delete_task(tasks):
  
  if len(tasks)==0:
      print("\t\t\tDelete Task option selected\n\n")
      print("📭 No tasks yet!\n")
      input("__--Press Enter to continue--__")
      clear_screen()
      
  else:       
    indices_to_delete=[]
    
   
    while True:
          print("\t\t\tDelete Task option selected\n\n")
          print("\n📋 Your Tasks :\n")
          for i, task in enumerate(tasks, start=1):
            status = "✅ Done" if task['done'] else "❌ Pending"
            print(f"{i}. {task['task']} — added on {task['time']} — {status}")
          
          delete_tasks = int(input("\nEnter task number (0 to exit): "))
          
  
          if delete_tasks==0:
             clear_screen()
             break
          
          elif 1 <= delete_tasks <= len(tasks):
              
              indices_to_delete.append(delete_tasks-1)
              input(f"🗑 Task {delete_tasks } marked for deletion. ")
              clear_screen()


          else:
              print("⚠️ Invalid task number.")
              input("__--Try again!--__")
              clear_screen()
              continue
          
    # Delete in reverse order to avoid index shift
      
    for idx in sorted(indices_to_delete, reverse=True):
          deleted_task = tasks.pop(idx)
          print(f"\n✅ '{deleted_task['task']}' deleted successfully")
          save_tasks(tasks)
          

    input("__--Press Enter to continue--__")
    clear_screen()
    view_task(tasks)
    
  



            
   


def show_menu():
 print("\t\t Uzair's To-Do-List\n\n")
 print("1. Add Task")
 print("2. View Tasks")
 print("3. Mark Task as Done")
 print("4. Delete Task")
 print("5. Exit")

tasks=load_tasks()

while True :
 
 clear_screen() 
 show_menu()
 
 try:
  ch=int(input("\n==>> Enter your Choice : "))
  clear_screen()
  if ch==1:
   
   print("\t\t\tAdd Task option selected\n\n")
   add_task(tasks)
  elif ch==2:
    print("\t\t\tView Task option selected\n\n")
    view_task(tasks)
  elif ch==3:
    
    mark_task(tasks)
  elif ch==4:
    
    delete_task(tasks)
  elif ch==5:
    input("You are Exiting Uzair's To-Do-List , GoodBye! ")
    clear_screen()
 
    break
  else:
    
    print("\nInvalid Task option selected\n\n")
    input("__--Press Enter to continue--__ ")
 except ValueError:
    clear_screen()
    print("\nPlease Enter numbers from 1-5")
    input("__--Press Enter to continue--__ ")

# Write your solution here

# If you use the classes made in the previous exercise, copy them here
# Write your solution here:

class Task:
    identity = 1
   
    def __init__ (self , description:str, programmer:str, workload:int ):
        self.id = Task.identity
        Task.identity += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.__finich = False

    def is_finished(self):
        return self.__finich

    def mark_finished(self):
        self.__finich = True

    def __str__(self):
        last = "FINISHED" if self.is_finished() else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {last}"
        
class OrderBook:
    
    def __init__ (self):
        self.__order = []

    def add_order(self, description, programmer, workload):
        self.__order.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.__order

    def programmers(self):
        return list(set([name.programmer for name in self.__order]))

    def mark_finished(self, id: int):
        value = True
        for task in self.__order:
            if task.id == id:
                task.mark_finished()
                value = False
                break
        if value:
            raise ValueError
    def finished_orders(self):
        return [task for task in self.__order if task.is_finished()]
    
    def unfinished_orders(self):
        return [task for task in self.__order if not task.is_finished()]

    def status_of_programmer(self, programmer: str):
        if programmer in self.programmers():
            task_f = [task for task in self.finished_orders() if task.programmer == programmer]
            task_u = [task for task in self.unfinished_orders() if task.programmer == programmer]
            hours1 = sum(hours.workload for hours in task_f)
            hours2 = sum(hours.workload for hours in task_u )
            return len(task_f) , len(task_u) , hours1 ,hours2
        else:
            raise ValueError

class UserInterface:
    def __init__ (self):
        self.__order = OrderBook()

    def add_order(self):
        try:
            description = input("description: ")
            p_w = input("programmer and workload estimate: ").split()
            programmer = p_w[0]
            workload = int(p_w[1])
            self.__order.add_order(description, programmer, workload)
            print("added!")
        except:
            print("erroneous input")

    def list_finished(self):
        if self.__order.finished_orders() == []:
            print("no finished tasks")
        else:
            for task in self.__order.finished_orders():
                print(task)

    def list_unfinished(self):
        if self.__order.unfinished_orders() == []:
            print("no unfinished tasks")
        else:
            for task in self.__order.unfinished_orders():
                print(task)

    def mark_task(self):
        try:
            id = int(input("id: "))
            self.__order.mark_finished(id)
            print("marked as finished")
        except:
            print("erroneous input")
    def programmers(self):
        for programmer in self.__order.programmers():
            print(programmer)

    def status(self):
        try:
            programmer = input("programmer: ")
            stats = self.__order.status_of_programmer(programmer)
            print(f"tasks: finished {stats[0]} not finished {stats[1]}, hours: done {stats[2]} scheduled {stats[3]}")
        except:
            print("erroneous input")
    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
        
    def search(self):
        self.help()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished()
            elif command == "3":
                self.list_unfinished()
            elif command == "4":
                self.mark_task()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status()
            
app = UserInterface()
app.search()
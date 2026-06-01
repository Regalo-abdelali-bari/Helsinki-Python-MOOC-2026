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

if __name__ == "__main__":
   
    t = OrderBook()
    t.add_order("program web store", "Andy", 10)
    t.add_order("program mobile gane", "Eric", 5)
    t.add_order("code better facebook", "Jonas", 5000)
    t.mark_finished(1)
    t.mark_finished(2)
    t.finished_orders()
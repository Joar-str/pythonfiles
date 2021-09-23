import random

"""
Fråga. Hur skall man identifiera vilken väg som kopplar respektive transaktion
"""
class Road:
    def __init__(self):
        self._road_work_list = [1,1,1,1]
    
    def check_worker(self):
        found = True
        if len(self._road_work_list) == 0:
            found = False
        return found

    def road_in(self):
        self._workers = Worker()
        self._road_work_list.append(Worker())
        

    def road_out(self):
        pass

    """FIFO - Först in först ut"""
    def worker_out(self):
        return self._road_work_list.pop(0)

    def worker_in(self, worker):
        self._road_work_list.append(worker)

    def lower_life(self):
        """Om en arbetare har väntat för länge sänks livskraften"""
        Worker.decrease_life()


#TODO Fråga vilka argument som bör användas vid __init__

class DinningHall:
    def __init__(self):

        self.food = 4
        self._eating_workers = []
        self.hall_road_in = None
        self.hall_rout_out = None

    def set_road_in(self, road):
        self.hall_road_in = road
    
    def set_road_out(self, road):
        self.hall_rout_out = road
    
    """Ska även kunna sänka livskraften om maten är dålig"""
    def feed_worker(self):
        Worker.increase_life()
    
    def worker_in(self, worker):
        if Road.check_worker == True:
            self._eating_workers.append(worker)
        
    def worker_out(self):
        pass

    def food_in(self, barn):
        if Barn.is_food == True:
            self.food += barn


class Field:
    def __init__(self):
        #self.worker = worker
        self.food = 0
        self.workers = []
        self.field_road_in = int
        self.field_road_out = int 

    def field_worker_in(self, worker):
        self.workers.append(worker)
    
    def field_worker_out(self):
        return self.workers.pop(-1)

    def create_food(self):
        for _ in self.workers:
            self.food += 1

    def field_food_out(self):
        return self.food

class Barn:

    def __init__(self, food):
        self.food  = food
        self.inventory = []

    def is_food(self):
        return bool(self.inventory)

    def barn_food_out(self):
        """
        FIFO - först in först ut
        """
        return self.inventory.pop(0)

    def barn_food_in(self, food):
        self.inventory.append(food)

class Food:
    def __init__(self):
        self._food = Field()

    def food_quality(self):
        pass

class Worker:
    def __init__(self):
        self.current_life = 100

    def decrease_life(self):
        self.current_life -= 1
    
    def increase_life(self):
        self.current_life += 1

    def check_life(self):
        return self.current_life
    
class House:
    def __init__(self):
        self.start_life = 100 # ???
        self.house_road_in = int
        self.house_road_out = int
        self._amount = random.randint(1,4)
    
    def house_input(self, worker, product):
        pass

    def house_output(self):
        pass

    def increase_life(self):
        Worker.increase_life()

    def amount_worker(self):
        return self._amount
    
class Stock:
    def __init__(self):
        self.products = [1,1,1,1]
    
    def is_product(self):
        return bool(self.products)

    def stock_pro_in(self):
        pass

    def stock_pro_out(self):
        pass

class Factory:
    def __init__(self):
        self.factory_road_in = int
        self.factory_road_out = int

    def worker_in(self):
        pass

    def worker_out(self):
        pass

    def product_out(self):
        pass

    def decrease_life(self):
        Worker.decrease_life()


    




if __name__ == "__main__":
    
    w1 = Worker()
    r1 = Road()
    d1 = DinningHall()
    #b1 = Barn()
    print(d1.worker_in(w1))
    


    
    
        
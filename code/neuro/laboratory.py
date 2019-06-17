




class Lab:
    def __init__(self, ecosystem):
        self.is_working = False
        self.current_dish = None
        self.ecosystem = ecosystem

    def work(self, dish):
        self.is_working = True
        while self.is_working:
            self.play_epoch(dish)



    def save_progress(self):
        pass

    def load_progress(self):
        pass

    def play_epoch(self, dish):
        pass















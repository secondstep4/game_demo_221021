class Cplace:
    def __init__(self, name:str) -> None:
        self.name = name
        self.link_list = []
        self.event_list = []

    def add_place(self, target):
        self.link_list.append(target)

    def get_linked_place(self):
        return self.link_list

    def add_event(self, event_code):
        self.event_list.append(event_code)

    def get_event_list(self):
        return self.event_list

class Centity:
    def __init__(self, name:str, max_hp:int, power:int):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.power = power

    def get_dmg(self, dmg:int) -> bool :
        if self.current_hp > dmg:
            self.current_hp -= dmg
            return False
        else :
            self.current_hp = 0
            return True

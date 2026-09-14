class FleetList:
    def __init__(self):
        self.head = None

    def insert(self, bike):
        nuevo = Node(bike)
        nuevo.next = self.head
        self.head = nuevo

    def search(self, code):
        act = self.head
        while act is not None:
            if act.data.code == code:
                return act.data
            act = act.next
        return None
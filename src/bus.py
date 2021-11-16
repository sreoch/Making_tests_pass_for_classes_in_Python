class Bus:
    def __init__(self, route, destination):
        self.route_number = route
        self.destination = destination

    def drive(self):
        return 'Brum brum'
class Bot:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.description = []
        self.eta = []
        self.sum_eta = None

    def print_robot_details(self):
        print("Your Robot:", self.name, "\nType:", self.type, "\n")

    def assign_task(self, type, desc, eta):
        if type.capitalize() == 'Unipedal':
            self.description = desc[0:4]
            self.eta = eta[0:4]
            self.sum_eta = sum(self.eta) / 1000
            print('Task completed:', self.description, 'Duration:', self.sum_eta, 'seconds')

        elif type.capitalize() == 'Bipedal':
            self.description = desc[1:5]
            self.eta = eta[1:5]
            self.sum_eta = sum(self.eta) / 1000
            print('Task completed:', self.description, 'Duration:', self.sum_eta, 'seconds')

        elif type.capitalize() == 'Quadrupedal':
            self.description = desc[2:6]
            self.eta = eta[2:6]
            self.sum_eta = sum(self.eta) / 1000
            print('Task completed:', self.description, 'Duration:', self.sum_eta, 'seconds')

        elif type.capitalize() == 'Arachnid':
            self.description = desc[3:7]
            self.eta = eta[3:7]
            sum_eta = sum(self.eta) / 1000
            print('Task completed:', self.description, 'Duration:', self.sum_eta, 'seconds')

        elif type.capitalize() == 'Radial':
            self.description = desc[4:8]
            self.eta = eta[4:8]
            self.sum_eta = sum(self.eta) / 1000
            print('Task completed:', self.description, 'Duration:', self.sum_eta, 'seconds')

        elif type.capitalize() == 'Aeronautical':
            self.description = desc[5:-1]
            self.eta = eta[5:-1]
            self.sum_eta = sum(self.eta) / 1000
            print('Task completed:', self.description, 'Duration:', self.sum_eta, 'seconds')


def fastest(robot, robot2):
    if robot.sum_eta < robot2.sum_eta:
        print('Leadership Board\n********************************')
        print('First place:', robot.name, 'Total Time:', robot.sum_eta)
        print('Second Place:', robot2.name, 'Total Time:', robot2.sum_eta)
        print('*******************************')

    elif robot.sum_eta > robot2.sum_eta:
        print('Leadership Board\n********************************')
        print('First place:', robot2.name, 'Total Time:', robot2.sum_eta, 'seconds')
        print('Second Place:', robot.name, 'Total Time:', robot.sum_eta, 'seconds')
        print('******************************')

    else:
        print('Leadership Board\n********************************')
        print(robot2.name, 'and', robot.name, 'TIED FIRST PLACE')
        print('Total Time:', robot.sum_eta, 'seconds')
        print('******************************')
    return None

class Node:
    def __init__(self, state=-1, action=-1, cost=0, parent=None):
        self.state = state
        self.action = action
        self.cost = cost
        self.parent = parent

    def __str__(self):
        return 'State: {} Action: {} Cost: {} Parent: {}'.format(self.state, self.action, self.cost, self.parent)


if __name__ == '__main__':
    node = Node()
    print(node)

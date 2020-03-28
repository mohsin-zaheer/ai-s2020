import queue, Node, Problem


def main():
    try:
        first_line = input().split(" ")
        no_of_states = int(first_line[0])
        no_of_rules = int(first_line[1])
        no_of_test_cases = int(first_line[2])
        state_space = []
        rules = []
        transition_table = [[None] * no_of_rules] * no_of_states
        test_cases = []

        input()  # Empty Line

        i = 0
        while i < no_of_states:
            state_space.append(input())
            i += 1

        input()  # Empty Line

        i = 0
        while i < no_of_rules:
            rules.append(input())
            i += 1

        input()  # Empty Line

        i = 0
        while i < no_of_states:
            transition_table[i] = [int(val) for val in input().split(" ")]
            i += 1

        input()  # Empty Line

        input_label = ['start', 'goal']
        i = 0
        while i < no_of_test_cases:
            test_case = input().split("\t")
            test_case_mapped = []
            for state in test_case:
                index = -1
                for key, val in enumerate(state_space):
                    if val == state:
                        index = key
                test_case_mapped.append(index)
            test_cases.append(dict(zip(input_label, test_case_mapped)))
            i += 1

        print(state_space)
        print(test_cases)
        print(transition_table)
        print(rules)

    except IOError:
        print("Input not in valid format")

    for case in test_cases:
        problem = Problem.Problem(case['start'], case['goal'], rules)
        node = breadth_first_search(problem, transition_table)
        if node is not None:
            print_solution(node, rules)
        else:
            print("No path from state {} to state {}".format(case['start'], case['goal']))


def breadth_first_search(problem, transition_table):
    node = Node.Node(state=problem.start)

    if node.state is problem.goal:
        return node;
    else:
        frontier = queue.Queue()
        frontier.put(node)
        explored = set()
        while not frontier.empty():
            node = frontier.get()
            explored.add(node.state)
            for action, action_description in enumerate(problem.rules):
                child_node = Node.Node(state=transition_table[node.state][action], cost=node.cost + 1,
                                       action=action, parent=node)
                if child_node not in explored:
                    if child_node.state == problem.goal:
                        return child_node
                    else:
                        frontier.put(child_node)
        return None


def print_solution(goal_node, rules):
    if goal_node.parent is None:
        print()
    else:
        node = goal_node
        stack = []
        while node.parent is not None:
            stack.append(node.action)
            node = node.parent
        while len(stack) > 1:
            print(rules[stack.pop()], end='->')
        print(rules[stack.pop()])


if __name__ == '__main__':
    main()

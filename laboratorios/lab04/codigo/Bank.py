from collections import deque

class Bank:
    """
    This class is used to simulate
    the Queues in bank.

    """

    def __init__(self, *queues):
        """
        Initializes the bank's queues.
        """
        self.queues = deque(queues)

    def simulate(self):
        """
        Simulates the order in which
        each customer from each queue
        will be attended and the cashier
        who will attend them.

        :return: Void
        """

        cashiers = deque([deque([]), deque([])])

        while len(self.queues) > 0:
            current_queue = self.queues.popleft()
            customer = current_queue.popleft()

            if len(current_queue) > 0:
                self.queues.append(current_queue)

            current_cashier = cashiers.popleft()
            current_cashier.append(customer)
            cashiers.append(current_cashier)

        for i, cashier in enumerate(cashiers):
            print("Cashier", str(i + 1) + ":")
            for customer in cashier:
                print("\t", customer)


q1 = deque(["Juan", "Ana", "Roberto"])
q2 = deque(["Casimiro", "Jose Juan"])
q3 = deque(["Berta", "Fabiola", "Yolanda", "Luzmila"])
q4 = deque(["Steve Jobs"])

bank = Bank(q1, q2, q3, q4)
bank.simulate()


class RoboticArm:
    """
    Interprets and executes a series
    of commands given to a robotic arm.
    """

    def __init__(self):

        self.number_of_blocks = int(input("Number of blocks: "))

        self.block_world = [[i] for i in range(self.number_of_blocks)]

        next_command = input("Commands:\n")
        while next_command != "quit":
            command_pieces = next_command.split()

            a = int(command_pieces[1])
            b = int(command_pieces[3])

            if command_pieces[0] == "move":
                if command_pieces[2] == "onto":
                    self.move_onto(a, b)
                elif command_pieces[2] == "over":
                    self.move_over(a, b)
            elif command_pieces[0] == "pile":
                if command_pieces[2] == "onto":
                    self.pile_onto(a, b)
                elif command_pieces[2] == "over":
                    self.pile_over(a, b)

            next_command = input()

        self.quit()


    def move_onto(self, a, b):
        """
        Puts block a over block b,
        after returning any block that
        is over a and b to its initial
        position.

        :param a: Block a
        :param b: Block b
        :return: Void
        """

        a_block, b_block = self.block_assignment(a, b)

        a_index = a_block.index(a)
        b_index = b_block.index(b)

        while len(a_block) - 1 > a_index:
            over_block = a_block.pop()
            self.block_world[over_block].append(over_block)

        while len(b_block) - 1 > b_index:
            over_block = b_block.pop()
            self.block_world[over_block].append(over_block)

        b_block.append(a_block.pop())

    def move_over(self, a, b):
        """
        Puts the block a over the
        stack that contains the block
        b, after returning any block
        that is over the block a, to
        its initial position.

        :param a: Block a
        :param b: Block b
        :return: Void
        """

        a_block, b_block = self.block_assignment(a, b)

        a_index = a_block.index(a)

        while len(a_block) - 1 > a_index:
            over_block = a_block.pop()
            self.block_world[over_block].append(over_block)

        b_block.append(a_block.pop())

    def pile_onto(self, a, b):
        """
        Moves the stack of blocks formed
        by a and every block over a, over
        the block b, after every block over the
        block b is moved to its initial
        position. The blocks over the block
        a keep their original order after
        being moved.

        :param a: Block a
        :param b: Block b
        :return: Void
        """

        a_block, b_block = self.block_assignment(a, b)

        a_index = a_block.index(a)
        blocks_over_a = a_block[a_index:]
        b_index = b_block.index(b)

        while len(a_block) - 1 > a_index:
            a_block.pop()

        while len(b_block) - 1 > b_index:
            over_block = b_block.pop()
            self.block_world[over_block].append(over_block)

        b_block += blocks_over_a

    def pile_over(self, a, b):
        """
        Puts the stack of blocks
        formed by a and every block
        over a, over the stack that
        contains the block b. The blocks over the block
        a keep their original order after
        being moved.

        :param a: Block a
        :param b: Block b
        :return: Void
        """

        a_block, b_block = self.block_assignment(a, b)

        a_index = a_block.index(a)
        blocks_over_a = []

        while len(a_block) > a_index:
            blocks_over_a = [a_block.pop()] + blocks_over_a

        b_block += blocks_over_a

    def quit(self):
        """
        Stops the robot's actions, and
        prints the final arrangement
        of the blocks.

        :return: Void
        """

        for index, block in enumerate(self.block_world):
            line = str(index) + ": "
            if len(block) > 0:
                line += str(block)[1:-1].replace(",", "")
            print(line)

    def block_assignment(self, a, b):

        a_block = b_block = None

        for block in self.block_world:
            if a in block:
                a_block = block
            if b in block:
                b_block = block
            if a_block != None and b_block != None:
                break

        return a_block, b_block


robot = RoboticArm()
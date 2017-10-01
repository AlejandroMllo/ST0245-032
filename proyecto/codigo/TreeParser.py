"""
Proyecto Final

Presentado por: Juan Pablo Vidal
                Alejandro Murillo
"""
import Root
import Directory
import File

class TreeParser:

    def __init__(self, file_path):
        with open(file_path, "r", encoding="UTF-8") as file:
            self.text = file.read()

    def parse(self):
        root = Root.Root()
        self.text = self.text.split("\n")
        root.set_name(self.text[0][:-1])

        for line in self.text[1:]:
            level = 0
            for character in line:
                if character == "[":

                    file_pieces = line[level:].split()
                    owner = file_pieces[0][1:]
                    size = file_pieces[1][:-1]
                    name = " ".join(file_pieces[2:])
                    file = File.File(name, size, owner)
                    root.add_file(name, file)
                    if file.get_type() != None:
                        root.add_file(file.get_type(), file)
                        root.add_file("." + file.get_type(), file)
                        root.add_file(file.get_name().split(".")[0], file)
                    root.add_file(size, file)
                    root.add_file(owner, file)

                else:
                    level += 1

        return root
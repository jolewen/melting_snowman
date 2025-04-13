### Handle the snowman graphic and it's melting progress

class Snowman:
    def __init__(self):
        self.is_melted = False
        self.melted_levels = 0
        self.ascii_graphic = r"""         ___  
        /___\ 
        (o o)
        ( : )
        ( : )"""
        self.show_snowman()
        self.new_ascii_lines = [idx for idx,ltr in enumerate(self.ascii_graphic) if ltr == '\n']

    def show_snowman(self):
        print(self.ascii_graphic)

    def remove_level(self):
        self.melted_levels += 1
        self.ascii_graphic = self.ascii_graphic[:self.new_ascii_lines.pop()]
        if self.melted_levels >= 3:
            self.is_melted = True
            print(f'The snowman has completely melted :\'( ')
        print(self.ascii_graphic)


if __name__ == '__main__':
    snowman = Snowman()
    i = 0
    while i < 5:
        snowman.remove_level()
        i += 1


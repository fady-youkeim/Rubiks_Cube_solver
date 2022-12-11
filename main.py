# Todo
# check for types of input for all functions and constructors

class Cell():
    def __init__(self, color):
        self.color = color
        
    def get_color(self):
        return color

class Row():
    def __init__(self, cells):
        self.cells = cells

    def get_cells(self):
        return self.cells

    def get_color_list(self):
        return [cell.color for cell in self.cells]

    def set_cells(self, cells):
        self.cells = cells

    def reverse(self):
        self.cells = self.cells[::-1]
        return self

class Face():
    def __init__(self, color_list):
        self.cells = [Cell(color) for color in color_list]

    def get_color_list(self):
        return [cell.color for cell in self.cells]

    def get_horizontal_row(self, index):
        if index == 0:
            horizontal_row = Row(self.cells[0:3])
            return horizontal_row
        elif index == 1:
            horizontal_row = Row(self.cells[3:6])
            return horizontal_row
        elif index == 2:
            horizontal_row = Row(self.cells[6:9])
            return horizontal_row
        else:
            raise Exception("unexpected index")

    def get_virtical_row(self, index):
        if index == 0:
            virtical_row = Row(self.cells[0:9:3])
            return virtical_row
        elif index == 1:
            virtical_row = Row(self.cells[1:9:3])
            return virtical_row
        elif index == 2:
            virtical_row = Row(self.cells[2:9:3])
            return virtical_row
        else:
            raise Exception("unexpected index")

    def set_horizontal_row(self, index, horizontal_row):
        horizontal_row = horizontal_row.get_cells()
        if index == 0:
            self.cells[0] = horizontal_row[0]
            self.cells[1] = horizontal_row[1]
            self.cells[2] = horizontal_row[2]
        elif index == 1:
            self.cells[3] = horizontal_row[0]
            self.cells[4] = horizontal_row[1]
            self.cells[5] = horizontal_row[2]

        elif index == 2:
            self.cells[6] = horizontal_row[0]
            self.cells[7] = horizontal_row[1]
            self.cells[8] = horizontal_row[2]
        else:
            raise Exception("unexpected index")

    def set_virtical_row(self, index, virtical_rows):
        virtical_rows = virtical_rows.get_cells()
        if index == 0:
            self.cells[0] = virtical_rows[0]
            self.cells[3] = virtical_rows[1]
            self.cells[6] = virtical_rows[2]
        elif index == 1:
            self.cells[1] = virtical_rows[0]
            self.cells[4] = virtical_rows[1]
            self.cells[7] = virtical_rows[2]

        elif index == 2:
            self.cells[2] = virtical_rows[0]
            self.cells[5] = virtical_rows[1]
            self.cells[8] = virtical_rows[2]
        else:
            raise Exception("unexpected index")

    def rotate_clock_wise(self):
        self.set_horizontal_row(0, self.get_virtical_row(0).reverse())
        self.set_horizontal_row(1, self.get_virtical_row(1).reverse())
        self.set_horizontal_row(2, self.get_virtical_row(2).reverse())

    def rotate_anti_clock_wise(self):
        self.set_horizontal_row(0, self.get_virtical_row(2))
        self.set_horizontal_row(1, self.get_virtical_row(1))
        self.set_horizontal_row(2, self.get_virtical_row(0))


class Cube():
    def __init__(self, color_list):
        self.front = Face(color_list[0])
        self.back = Face( color_list[1])
        self.top = Face( color_list[2])
        self.bottom = Face( color_list[3])
        self.right = Face( color_list[4])
        self.left = Face( color_list[5])

    def print(self):
        print()
        print("_"*47, end="\n|")
        print(" "*15, end = "")
        print(self.back.get_color_list()[6:][::-1], end="")
        print(" "*15, end = "|\n|")
        print(" "*15, end = "")
        print(self.back.get_color_list()[3:6][::-1], end="")
        print(" "*15, end = "|\n|")
        print(" "*15, end = "")
        print(self.back.get_color_list()[0:3][::-1], end="")
        print(" "*15, end = "|\n|")
        print("-"*15*3, end="|\n|")
        print(" "*15, end = "")
        print(self.top.get_color_list()[0:3], end="")
        print(" "*15, end = "|\n|")
        print(" "*15, end = "")
        print(self.top.get_color_list()[3:6], end="")
        print(" "*15, end = "|\n|")
        print(" "*15, end = "")
        print(self.top.get_color_list()[6:], end="")
        print(" "*15, end = "|\n|")
        print("-"*15*3, end="|\n|")
        print(self.left.get_color_list()[0:3], end = "")
        print(self.front.get_color_list()[0:3], end = "")
        print(self.right.get_color_list()[0:3], end="|\n|")
        print(self.left.get_color_list()[3:6], end = "")
        print(self.front.get_color_list()[3:6], end = "")
        print(self.right.get_color_list()[3:6], end="|\n|")
        print(self.left.get_color_list()[6:], end = "")
        print(self.front.get_color_list()[6:], end = "")
        print(self.right.get_color_list()[6:], end="|\n|")
        print("-"*15*3, end="|\n|")
        print(" "*15, end = "")
        print(self.bottom.get_color_list()[0:3], end="")
        print(" "*15, end = "|\n|")
        print(" "*15, end = "")
        print(self.bottom.get_color_list()[3:6], end="")
        print(" "*15, end = "|\n|")
        print(" "*15, end = "")
        print(self.bottom.get_color_list()[6:], end="")
        print(" "*15, end = "|\n")
        print("‾"*47)
        print()

    def rotate_right():
        return none

    def rotate_left():
        pass

    def rotate_up():
        pass

    def rotate_down():
        pass

    def rotate_front():
        self.front.rotate_clock_wise()
        # continue later

    def rotate_back():
        pass

    def rotate_reverse_right():
        pass

    def rotate_reverse_left():
        pass

    def rotate_reverse_up():
        pass

    def rotate_reverse_down():
        pass

    def rotate_reverse_front():
        pass

    def rotate_reverse_back():
        pass



color_list = [["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9"], 
                ["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9"], 
                ["y1", "y2", "y3", "y4", "y5", "y6", "y7", "y8", "y9"], 
                ["w1", "w2", "w3", "w4", "w5", "w6", "w7", "w8", "w9"], 
                ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9"], 
                ["o1", "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9"]]

cube = Cube(color_list)
cube.front.rotate_clock_wise()
cube.print()


from manim import *
import random


def generador_entrada(size):
    vector = []
    for i in range(size):
        num = random.randint(0, 9)
        vector.append(num)
    return vector


class ArrayVisualization(Scene):
    def construct(self):
        # Definir los elementos del arreglo

        array = generador_entrada(10)

        boxes = []
        groups = []
        for i, value in enumerate(array):
            box = Square(side_length=1, color=RED).move_to([-5 + (i), 0, 0])
            boxes.append(box)

            # Crear el texto con el valor del elemento dentro del rectángulo
            index = Text(str(i), font_size=24).move_to(box.get_center() + UP)
            text = Text(str(value)).move_to(box.get_center())
            groups.append(VGroup(box, text, index))

        array_group = VGroup(*groups)
        array_group.arrange()
        self.play(Create(array_group))
        self.wait(2)
        self.play(array_group.animate.shift(UP * 2))

        max_value = max(array)
        counter = [0] * (max_value + 1)

        c_boxes = []
        c_groups = []

        for i, value in enumerate(counter):
            c_box = Square(side_length=1, color=LIGHT_PINK).move_to(
                [-5 + (i), 0, 0])
            c_boxes.append(c_box)

            # Crear el texto con el valor del elemento dentro del rectángulo
            c_text = Text(str(value)).move_to(c_box.get_center())
            c_index = Text(str(i), font_size=24).move_to(
                c_box.get_center() + UP)
            c_groups.append(VGroup(c_box, c_text, c_index))

        c_array_group = VGroup(*c_groups)
        c_array_group.arrange()
        self.play(Create(c_array_group))
        self.wait(2)
        self.play(c_array_group.animate.shift(DOWN * 1))

        sorted_array = [0] * 10

        j = 0
        for i in array:
            self.wait(0.5)
            s2 = SurroundingRectangle(groups[j][0], color=YELLOW)
            self.play(Write(s2))
            counter[i] = counter[i] + 1
            s = SurroundingRectangle(c_groups[i], color=YELLOW)
            self.play(Write(s))
            self.play(Transform(c_groups[i][1], Text(
                str(counter[i])).move_to(c_boxes[i].get_center())))
            c_boxes[i].set_color(LIGHT_PINK)
            self.play(Transform(s, SurroundingRectangle(
                c_groups[i], color=None)))
            self.play(Transform(s2, SurroundingRectangle(
                groups[j][0], color=None)))
            boxes[j].set_color(BLUE)
            j += 1

        for i in range(1, len(counter)):
            counter[i] += counter[i - 1]

        for i in range(len(array)-1, -1, -1):
            sorted_array[counter[array[i]] - 1] = array[i]
            counter[array[i]] -= 1

        # Sorted array
        for i, value in enumerate(sorted_array):
            new_text = Text(str(value)).move_to(boxes[i].get_center())
            self.play(Transform(groups[i][1], new_text))
            boxes[i].set_color(GREEN)

        self.wait(2)

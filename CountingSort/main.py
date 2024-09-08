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

            c_text = Text(str(value)).move_to(c_box.get_center())
            c_index = Text(str(i), font_size=24).move_to(
                c_box.get_center() + UP)
            c_groups.append(VGroup(c_box, c_text, c_index))

        c_array_group = VGroup(*c_groups)
        c_array_group.arrange()
        self.play(Create(c_array_group))
        self.wait(1)
        self.play(c_array_group.animate.shift(DOWN * 1))

        j = 0
        for i in array:
            s2 = SurroundingRectangle(groups[j][0], color=YELLOW)
            self.play(Write(s2))
            counter[i] = counter[i] + 1
            s = SurroundingRectangle(c_groups[i], color=YELLOW)
            self.play(Write(s))
            self.play(Transform(c_groups[i][1], Text(
                str(counter[i])).move_to(c_boxes[i].get_center())))
            color_change = boxes[j].copy().set_color(BLUE)
            self.play(Transform(boxes[j], color_change))
            c_boxes[i].set_color(LIGHT_PINK)
            self.play(Uncreate(s))
            self.play(Uncreate(s2))
            
            j += 1
        
        array_copy = array_group.copy()
        self.play(FadeOut(array_group))
        self.play(c_array_group.animate.shift(UP * 1))
        
        for i in range(1, len(counter)):
            add_g = VGroup(c_boxes[i-1], c_boxes[i] )
            sa = SurroundingRectangle(add_g, color=YELLOW)
            self.play(Write(sa))    
            counter[i] += counter[i - 1]
            add_t = Text(str(counter[i])).move_to(c_boxes[i].get_center())
            self.play(Transform(c_groups[i][1], add_t))
            self.play(FadeOut(sa))
            


        sorted_array = [0] * 10
        s_boxes = []
        s_groups = []
        for i, value in enumerate(sorted_array):
            s_box = Square(side_length=1, color=YELLOW).move_to(
                [-5 + (i), 0, 0])
            s_boxes.append(s_box)
            s_text = Text(str(value)).move_to(s_box.get_center())
            s_index = Text(str(i), font_size=24).move_to(
                s_box.get_center() + UP)
            s_groups.append(VGroup(s_box, s_text, s_index))
        s_array_group = VGroup(*s_groups)
        s_array_group.arrange()
        
        
            
        self.play(Create(array_copy))
        self.play(array_copy.animate.shift(UP * 1)) 
        self.play(c_array_group.animate.shift(DOWN * 2))
        self.play(Create(s_array_group))
        self.play(array_copy.animate.shift(DOWN * 1)) 
        
        for i in range(len(array) - 1, -1, -1):
            s_s = SurroundingRectangle(array_copy[i][1], color=YELLOW) 
            s_c = SurroundingRectangle(c_groups[array[i]][2], color=YELLOW) 
            s_sort = SurroundingRectangle(s_array_group[counter[array[i]] - 1][2], color=YELLOW)
            
            self.play(Write(s_s))
            self.play(Write(s_c))
            
            pos = counter[array[i]] - 1

            counter[array[i]] -= 1

            minus = Text(str(counter[array[i]])).move_to(c_boxes[array[i]].get_center())
            self.play(Transform(c_groups[array[i]][1], minus))

            number = Text(str(array[i])).move_to(s_boxes[pos].get_center())
            self.play(Transform(s_array_group[pos][1], number))
            self.play(Write(s_sort))

            green_box = s_boxes[pos].copy().set_color(GREEN)
            self.play(Transform(s_boxes[pos], green_box))
            
            red = boxes[i].copy().set_color(RED)
            self.play(Transform(boxes[i], red))
            
            self.play(FadeOut(s_s))
            self.play(FadeOut(s_c))
            self.play(FadeOut(s_sort))


        
        print(sorted_array)
        self.wait(2)

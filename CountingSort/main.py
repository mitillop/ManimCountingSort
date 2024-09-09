from manim import *
import random

def generador_entrada(size):
    vector = []
    for i in range(size):
        num = random.randint(0, 9)
        vector.append(num)
    return vector

class CountingSort(Scene):
    def construct(self):
        self.camera.frame_rate = 60
        array = generador_entrada(11)

        boxes = []
        groups = []
        for i, value in enumerate(array):
            box = Square(side_length=1, color=RED).move_to([-5 + (i), 0, 0])
            boxes.append(box)
            index = Text(str(i), font_size=24).move_to(box.get_center() + UP)
            text = Text(str(value)).move_to(box.get_center())
            groups.append(VGroup(box, text, index))

        array_group = VGroup(*groups)
        array_group.arrange()
        self.play(Create(array_group), run_time=1)  # Ajustar velocidad
        self.wait(1)
        self.play(array_group.animate.shift(UP * 2), run_time=1)

        max_value = max(array)
        counter = [0] * (max_value + 1)

        c_boxes = []
        c_groups = []

        for i, value in enumerate(counter):
            c_box = Square(side_length=1, color=LIGHT_PINK).move_to([-5 + (i), 0, 0])
            c_boxes.append(c_box)
            c_text = Text(str(value)).move_to(c_box.get_center())
            c_index = Text(str(i), font_size=24).move_to(c_box.get_center() + UP)
            c_groups.append(VGroup(c_box, c_text, c_index))

        c_array_group = VGroup(*c_groups)
        c_array_group.arrange()
        self.play(Create(c_array_group), run_time=1)
        self.wait(1)
        self.play(c_array_group.animate.shift(DOWN * 1), run_time=1)

        # Primer ciclo
        for j, i in enumerate(array):
            s2 = SurroundingRectangle(groups[j][0], color=YELLOW)
            self.play(Write(s2), run_time=0.5)
            counter[i] += 1
            s = SurroundingRectangle(c_groups[i], color=YELLOW)
            self.play(Write(s), run_time=0.5)
            self.play(Transform(c_groups[i][1], Text(str(counter[i])).move_to(c_boxes[i].get_center())), run_time=0.5)
            color_change = boxes[j].copy().set_color(BLUE)
            self.play(Transform(boxes[j], color_change), run_time=0.5)
            self.play(Uncreate(s), run_time=0.5)
            self.play(Uncreate(s2), run_time=0.5)

        array_copy = array_group.copy()
        self.play(FadeOut(array_group), run_time=1)
        self.play(c_array_group.animate.shift(UP * 1), run_time=1)

        # Segundo ciclo
        for i in range(1, len(counter)):
            add_g = VGroup(c_boxes[i - 1], c_boxes[i])
            sa = SurroundingRectangle(add_g, color=YELLOW)
            self.play(Write(sa), run_time=0.5)
            counter[i] += counter[i - 1]
            add_t = Text(str(counter[i])).move_to(c_boxes[i].get_center())
            self.play(Transform(c_groups[i][1], add_t), run_time=0.5)
            self.play(FadeOut(sa), run_time=0.5)

        sorted_array = [0] * 10
        s_boxes = []
        s_groups = []
        for i, value in enumerate(sorted_array):
            s_box = Square(side_length=1, color=GREEN).move_to([-5 + (i), 0, 0])
            s_boxes.append(s_box)
            s_text = Text(str(value)).move_to(s_box.get_center())
            s_index = Text(str(i), font_size=24).move_to(s_box.get_center() + UP)
            s_groups.append(VGroup(s_box, s_text, s_index))
        s_array_group = VGroup(*s_groups)
        s_array_group.arrange()

        self.play(Create(array_copy), run_time=1)
        self.play(array_copy.animate.shift(UP * 1), run_time=1)
        self.play(c_array_group.animate.shift(DOWN * 2), run_time=1)
        self.play(Create(s_array_group), run_time=1)
        self.play(array_copy.animate.shift(DOWN * 1), run_time=1)

        for i in range(len(array) - 1, -1, -1):
            s_s = SurroundingRectangle(array_copy[i][1], color=YELLOW)  
            s_c = SurroundingRectangle(c_groups[array[i]][2], color=YELLOW)  
            self.play(Write(s_s), run_time=0.5)
            self.play(Write(s_c), run_time=0.5)

            pos = counter[array[i]] - 1
            counter[array[i]] -= 1
            minus = Text(str(counter[array[i]])).move_to(c_boxes[array[i]].get_center())
            self.play(Transform(c_groups[array[i]][1], minus), run_time=0.5)

            highlight_index = SurroundingRectangle(s_array_group[pos][2], color=GREEN)
            self.play(Create(highlight_index), run_time=0.5)

            highlight_box = SurroundingRectangle(s_array_group[pos][0], color=GREEN)
            self.play(Create(highlight_box), run_time=0.5)

            number = Text(str(array[i])).move_to(s_boxes[pos].get_center())
            self.play(Transform(s_array_group[pos][1], number), run_time=0.5)

            green_box = s_boxes[pos].copy().set_color(GREEN)
            self.play(Transform(s_boxes[pos], green_box), run_time=0.5)

            red = boxes[i].copy().set_color(RED)
            self.play(Transform(boxes[i], red), run_time=0.5)

            self.play(FadeOut(s_s), run_time=0.5)
            self.play(FadeOut(s_c), run_time=0.5)
            self.play(FadeOut(highlight_index), run_time=0.5)
            self.play(FadeOut(highlight_box), run_time=0.5)

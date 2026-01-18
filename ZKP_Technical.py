from manim import *
import numpy as np

class TechnicalExplainer(Scene):
    def construct(self):
        self.part_1_circuit_logic()
        self.part_2_r1cs_constraints()
        self.part_3_qap_visual()

    def part_1_circuit_logic(self):
        # --- TITLE ---
        title = Text("Step 1: The Arithmetic Circuit", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # --- NODES ---
        # Inputs (Left)
        in_year = self.create_node("2026", UP*1.5 + LEFT*4, BLUE)
        in_dob  = self.create_node("1990", DOWN*1.5 + LEFT*4, YELLOW) # Secret
        
        # Gate 1 (Sub)
        gate1 = Square(side_length=1.0, color=WHITE).move_to(LEFT*0.5)
        op1 = Text("-", font_size=40).move_to(gate1)
        lbl1 = Text("Age", font_size=20, color=GRAY).next_to(gate1, UP)
        
        # Gate 2 (Sub)
        gate2 = Square(side_length=1.0, color=WHITE).move_to(RIGHT*3.5)
        op2 = Text("-", font_size=40).move_to(gate2)
        in_thresh = self.create_node("21", DOWN*1.5 + RIGHT*1.5, WHITE)
        lbl2 = Text("Check", font_size=20, color=GRAY).next_to(gate2, UP)

        # --- WIRES ---
        # 2026 -> Gate 1
        w1 = Arrow(in_year.get_right(), gate1.get_left() + UP*0.2, buff=0.1, color=GRAY)
        # 1990 -> Gate 1
        w2 = Arrow(in_dob.get_right(), gate1.get_left() + DOWN*0.2, buff=0.1, color=YELLOW) # Secret Wire
        
        # Gate 1 -> Gate 2
        w3 = Arrow(gate1.get_right(), gate2.get_left() + UP*0.2, buff=0.1, color=GRAY)
        # 21 -> Gate 2
        w4 = Arrow(in_thresh.get_right(), gate2.get_left() + DOWN*0.2, buff=0.1, color=GRAY)
        
        # Gate 2 -> Output
        out_node = self.create_node("Result", RIGHT*6, GREEN)
        w5 = Arrow(gate2.get_right(), out_node.get_left(), buff=0.1, color=GREEN)

        # --- ANIMATE ---
        self.play(FadeIn(in_year), FadeIn(in_dob), FadeIn(in_thresh))
        self.play(Create(gate1), Write(op1), Write(lbl1))
        self.play(GrowArrow(w1), GrowArrow(w2))
        
        # Calculation 1
        calc1 = Text("36", color=BLUE).next_to(gate1, DOWN)
        self.play(Write(calc1))
        self.wait(0.5)
        
        self.play(Create(gate2), Write(op2), Write(lbl2))
        self.play(GrowArrow(w3), GrowArrow(w4))
        
        # Calculation 2
        calc2 = Text("15", color=GREEN).next_to(gate2, DOWN)
        self.play(Write(calc2), GrowArrow(w5), FadeIn(out_node))
        self.wait(2)
        
        # Group for cleanup
        self.circuit_group = VGroup(
            in_year, in_dob, in_thresh, out_node,
            gate1, op1, lbl1, gate2, op2, lbl2,
            w1, w2, w3, w4, w5, calc1, calc2, title
        )

    def part_2_r1cs_constraints(self):
        # Transition: Shrink circuit, show math
        self.play(
            self.circuit_group.animate.scale(0.5).to_edge(UP).set_opacity(0.5)
        )
        
        title = Text("Step 2: R1CS (The Equations)", font_size=36, color=BLUE).next_to(self.circuit_group, DOWN, buff=0.5)
        self.play(Write(title))
        
        # The Math
        eq1 = MathTex(r"(2026 - 1990) \times 1 = \text{age}").shift(DOWN*0.5)
        eq2 = MathTex(r"(\text{age} - 21) \times 1 = \text{result}").next_to(eq1, DOWN)
        
        self.play(Write(eq1))
        self.wait(0.5)
        self.play(Write(eq2))
        self.wait(2)
        
        self.r1cs_group = VGroup(title, eq1, eq2)
        
        # Fade out circuit, keep equations for transformation
        self.play(FadeOut(self.circuit_group))
        self.play(self.r1cs_group.animate.shift(UP*2))

    def part_3_qap_visual(self):
        # --- SETUP ---
        title = Text("Step 3: QAP (The Polynomial)", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Transform(self.r1cs_group[0], title)) 
        
        # Axes - Moved UP to avoid bottom text clash
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 6, 1],
            axis_config={"include_numbers": True},
            x_length=7,
            y_length=4
        ).shift(UP * 0.5) 
        
        x_label = axes.get_x_axis_label("Constraints (Gates)").next_to(axes.x_axis, DOWN)
        # Fix: Move "Value" label to the top of the axis to avoid clashing with the curve
        y_label = axes.get_y_axis_label("Value").next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # --- TRANSFORMATION ---
        # Transform Equations into Points
        # We only have 2 Gates in our circuit.
        # Gate 1 -> x=1. Let's assign it visual value y=3.
        # Gate 2 -> x=2. Let's assign it visual value y=2.
        
        p1 = Dot(axes.c2p(1, 3), color=RED)
        p2 = Dot(axes.c2p(2, 2), color=RED)
        
        lbl1 = Text("Gate 1").next_to(p1, UP).scale(0.5)
        lbl2 = Text("Gate 2").next_to(p2, UP).scale(0.5)
        
        # Animate Eq1 -> Point 1
        self.play(Transform(self.r1cs_group[1], p1), FadeIn(lbl1))
        # Animate Eq2 -> Point 2
        self.play(Transform(self.r1cs_group[2], p2), FadeIn(lbl2))
        
        self.wait(1)
        
        # --- THE POLYNOMIAL ---
        # We need a line passing through (1,3) and (2,2).
        # Slope = (2-3)/(2-1) = -1.
        # Eq: y - 3 = -1(x - 1) => y = -x + 4.
        
        graph = axes.plot(lambda x: -x + 4, color=GREEN, x_range=[0, 4])
        
        graph_label = axes.get_graph_label(graph, label="P(x)", x_val=3.5, direction=UP)
        
        self.play(Create(graph), run_time=2)
        self.play(Write(graph_label))
        
        # Conclusion
        final_text = Text("Valid Proof = Curve hits ALL points", font_size=24, color=GREEN).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(3)
        
        # --- THE INVALID PROOF ---
        # Show what happens if you cheat (change 1990 -> 2010).
        # The calculated value at Gate 1 changes.
        # Let's say it jumps to 5.
        p1_cheat = Dot(axes.c2p(1, 5), color=RED) 
        
        self.play(
            p1.animate.move_to(axes.c2p(1, 5)),
            FadeOut(final_text),
            FadeOut(graph),
            FadeOut(graph_label) # Fade out old label
        )
        
        cheat_text = Text("If you cheat, the points shift...", font_size=24, color=RED).to_edge(DOWN)
        self.play(Write(cheat_text))
        
        # New Curve misses the ORIGINAL logic
        # We redraw the GREEN curve to show it doesn't fit the NEW red dots.
        # (Or we could draw the new curve, but showing the mismatch is clearer).
        
        miss_text = Text("...and the valid Polynomial no longer fits!", font_size=24, color=RED).next_to(cheat_text, DOWN)
        
        # Flash the mismatch
        line_miss = DashedLine(p1.get_center(), axes.c2p(1, 3), color=RED)
        self.play(Create(line_miss))
        self.play(Write(miss_text))
        self.wait(3)

    # Helper
    def create_node(self, label, pos, color):
        c = Circle(radius=0.4, color=color, fill_opacity=0.2).move_to(pos)
        t = Text(label, font_size=16).move_to(c)
        return VGroup(c, t)
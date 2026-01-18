from manim import *
import numpy as np

class TechnicalExplainer(Scene):
    def construct(self):
        # 1. CIRCUIT SETUP (Visualizing the Logic)
        self.part_1_circuit_logic()
        
        # 2. R1CS (Transition to Math)
        self.part_2_r1cs_constraints()
        
        # 3. UNDERAGE PROOF (Valid Math, Negative Result)
        self.part_3_underage_proof()
        
        # 4. ADULT PROOF (Valid Math, Positive Result)
        self.part_4_adult_proof()
        
        # 5. FAKED PROOF (Invalid Math, Logic Mismatch)
        self.part_5_faked_proof()

    def part_1_circuit_logic(self):
        # --- TITLE ---
        title = Text("Step 1: The Arithmetic Circuit", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # --- NODES (Inputs) ---
        # Shifted slightly to optimize space
        start_x = LEFT * 5
        in_year = self.create_node("2026", start_x + UP*2.5, BLUE)
        in_dob  = self.create_node("2010", start_x + UP*0.8, RED)   # Underage (16)
        in_base = self.create_node("21",   start_x + DOWN*0.8, WHITE)
        in_valid= self.create_node("1",    start_x + DOWN*2.5, WHITE) 

        # --- GATES ---
        # Gate 1: Age (Year - DOB)
        g1 = Square(side_length=0.8, color=WHITE).move_to(LEFT*2 + UP*1.6)
        op1 = Text("-", font_size=30).move_to(g1)
        lbl1 = Text("Age", font_size=16, color=GRAY).next_to(g1, UP)
        
        # Gate 2: Threshold (Age - 21)
        g2 = Square(side_length=0.8, color=WHITE).move_to(LEFT*2 + DOWN*1.6)
        op2 = Text("-", font_size=30).move_to(g2)
        lbl2 = Text("Check", font_size=16, color=GRAY).next_to(g2, UP)

        # Gate 3: Validity Check (1 * 1)
        g3 = Square(side_length=0.8, color=WHITE).move_to(RIGHT*1 + DOWN*2.5)
        op3 = Text("*", font_size=30).move_to(g3)
        lbl3 = Text("Valid?", font_size=16, color=GRAY).next_to(g3, UP)

        # Gate 4: Final Combine
        g4 = Square(side_length=0.8, color=WHITE).move_to(RIGHT*1 + UP*0.0)
        op4 = Text("*", font_size=30).move_to(g4)
        lbl4 = Text("Final", font_size=16, color=GRAY).next_to(g4, UP)

        # Output Node
        out_node = self.create_node("Result", RIGHT*5, RED)

        # --- ANIMATION ---
        self.play(FadeIn(in_year), FadeIn(in_dob), FadeIn(in_base), FadeIn(in_valid))
        
        # Step 1: Age
        self.play(Create(g1), Write(op1), Write(lbl1))
        self.play(
            Arrow(in_year.get_right(), g1.get_left() + UP*0.1, color=GRAY).animate,
            Arrow(in_dob.get_right(), g1.get_left() + DOWN*0.1, color=RED).animate 
        )
        res1 = Text("16", font_size=24, color=RED).next_to(g1, RIGHT, buff=0.2)
        self.play(Write(res1))

        # Step 2: Threshold
        self.play(Create(g2), Write(op2), Write(lbl2))
        self.play(
            Arrow(g1.get_bottom(), g2.get_top() + LEFT*0.1, color=GRAY).animate,
            Arrow(in_base.get_right(), g2.get_left(), color=GRAY).animate
        )
        res2 = Text("-5", font_size=24, color=RED).next_to(g2, RIGHT, buff=0.2)
        self.play(Write(res2))

        # Step 3: Valid ID Check
        self.play(Create(g3), Write(op3), Write(lbl3))
        # Fix arrow path to avoid hitting numbers
        self.play(Arrow(in_valid.get_right(), g3.get_left(), color=GRAY, buff=0.1).animate)
        res3 = Text("1", font_size=24, color=WHITE).next_to(g3, RIGHT, buff=0.2)
        self.play(Write(res3))

        # Step 4: Final Combine
        self.play(Create(g4), Write(op4), Write(lbl4))
        self.play(
            Arrow(g2.get_top(), g4.get_bottom() + LEFT*0.1, color=RED).animate,
            Arrow(g3.get_top(), g4.get_bottom() + RIGHT*0.1, color=WHITE).animate
        )
        res4 = Text("-5", font_size=32, color=RED).next_to(g4, RIGHT, buff=0.2)
        self.play(Write(res4), Arrow(g4.get_right(), out_node.get_left(), color=RED).animate, FadeIn(out_node))
        
        # Explainer - MOVED TO BOTTOM LEFT to avoid clashes
        logic_box = RoundedRectangle(height=1.2, width=4, color=RED).to_corner(DL).shift(UP*0.5 + RIGHT*1.0)
        logic_text = Text("Result is Negative (-5)\nACCESS DENIED", font_size=20, color=RED).move_to(logic_box)
        self.play(Create(logic_box), Write(logic_text))
        self.wait(2)

        # Cleanup
        self.circuit_group = VGroup(
            in_year, in_dob, in_base, in_valid, out_node,
            g1, g2, g3, g4, op1, op2, op3, op4, lbl1, lbl2, lbl3, lbl4,
            res1, res2, res3, res4, title, logic_box, logic_text
        )
        for m in self.mobjects:
            if isinstance(m, Arrow): self.circuit_group.add(m)

    def part_2_r1cs_constraints(self):
        self.play(self.circuit_group.animate.scale(0.5).to_edge(UP).set_opacity(0.3))
        
        title = Text("Step 2: R1CS (Equations)", font_size=36, color=BLUE).next_to(self.circuit_group, DOWN, buff=0.2)
        self.play(Write(title))
        
        eq1 = MathTex(r"1: \quad 2026 - 2010 = 16").scale(0.8)
        eq2 = MathTex(r"2: \quad 16 - 21 = -5").scale(0.8)
        eq3 = MathTex(r"3: \quad 1 \times 1 = 1").scale(0.8)
        eq4 = MathTex(r"4: \quad -5 \times 1 = -5").scale(0.8)
        
        eq_group = VGroup(eq1, eq2, eq3, eq4).arrange(DOWN, aligned_edge=LEFT).next_to(title, DOWN)
        
        self.play(Write(eq_group))
        self.wait(1)
        
        self.r1cs_group = VGroup(title, eq_group)
        self.play(FadeOut(self.circuit_group))
        self.play(self.r1cs_group.animate.to_edge(UP))

    def part_3_underage_proof(self):
        title = Text("Scenario 1: Underage (16)", font_size=36, color=RED).to_edge(UP)
        self.play(Transform(self.r1cs_group[0], title), FadeOut(self.r1cs_group[1]))
        
        # --- AXES ---
        # Scaled down to 0.8 to avoid hitting Title
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[-10, 30, 10], 
            axis_config={"include_numbers": True},
            x_length=7,
            y_length=4.5
        ).scale(0.8).shift(DOWN * 0.5) 
        
        x_lbl = axes.get_x_axis_label("Gates").next_to(axes.x_axis, DOWN)
        y_lbl = axes.get_y_axis_label("Val").next_to(axes.y_axis, UP)
        self.play(Create(axes), Write(x_lbl), Write(y_lbl))
        
        # --- POINTS (16, -5, 1, -5) ---
        coords = [(1, 16), (2, -5), (3, 1), (4, -5)]
        
        dots = VGroup()
        labels = VGroup() # New group for explicit values
        
        for i, (x, y) in enumerate(coords):
            d = Dot(axes.c2p(x, y), color=RED)
            dots.add(d)
            # Logic Labels
            if i == 0:
                l = Text("G1=Age(16)", font_size=12).next_to(d, UP)
                labels.add(l)
            if i == 3:
                l = Text("G4=Result(-5)", font_size=12).next_to(d, DOWN)
                labels.add(l)
                
        self.play(FadeIn(dots), FadeIn(labels))
        
        # --- CURVE ---
        coeffs = np.polyfit([c[0] for c in coords], [c[1] for c in coords], 3)
        poly_func = np.poly1d(coeffs)
        
        graph = axes.plot(lambda x: poly_func(x), color=RED, x_range=[0.5, 4.5])
        self.play(Create(graph), run_time=2)
        
        # Explanation
        msg = Text("Valid Proof (Math works), but Result is Negative.", font_size=24, color=RED).to_edge(DOWN)
        self.play(Write(msg))
        self.wait(3)
        
        self.play(FadeOut(dots), FadeOut(graph), FadeOut(msg), FadeOut(labels))
        self.axes = axes 

    def part_4_adult_proof(self):
        new_title = Text("Scenario 2: Adult (26)", font_size=36, color=GREEN).to_edge(UP)
        self.play(Transform(self.r1cs_group[0], new_title))
        
        # Points: (1, 26), (2, 5), (3, 1), (4, 5)
        coords = [(1, 26), (2, 5), (3, 1), (4, 5)]
        
        dots = VGroup()
        labels = VGroup()
        for i, (x, y) in enumerate(coords):
            d = Dot(self.axes.c2p(x, y), color=GREEN)
            dots.add(d)
            if i == 0: labels.add(Text("G1=Age(26)", font_size=12).next_to(d, UP))
            if i == 3: labels.add(Text("G4=Result(5)", font_size=12).next_to(d, UP))

        self.play(FadeIn(dots), FadeIn(labels))
        
        coeffs = np.polyfit([c[0] for c in coords], [c[1] for c in coords], 3)
        poly_func = np.poly1d(coeffs)
        
        graph = self.axes.plot(lambda x: poly_func(x), color=GREEN, x_range=[0.5, 4.5])
        self.play(Create(graph), run_time=2)
        
        msg = Text("Valid Proof AND Positive Result (+5). ACCESS GRANTED.", font_size=24, color=GREEN).to_edge(DOWN)
        self.play(Write(msg))
        self.wait(3)
        
        self.play(FadeOut(dots), FadeOut(graph), FadeOut(msg), FadeOut(labels))

    def part_5_faked_proof(self):
        new_title = Text("Scenario 3: Faked Proof (Cheating)", font_size=36, color=ORANGE).to_edge(UP)
        self.play(Transform(self.r1cs_group[0], new_title))
        
        # 1. The Conflict
        p1 = Dot(self.axes.c2p(1, 16), color=RED) # Reality
        p1_lbl = Text("Real Input\n(16)", font_size=14, color=RED).next_to(p1, DOWN)
        
        p4 = Dot(self.axes.c2p(4, 5), color=GREEN) # Fake Goal
        p4_lbl = Text("Fake Result\n(+5)", font_size=14, color=GREEN).next_to(p4, UP)
        
        self.play(FadeIn(p1), Write(p1_lbl), FadeIn(p4), Write(p4_lbl))
        self.wait(1)
        
        # 2. Fake Curve
        fake_coords = [(1, 16), (2, 0), (3, 1), (4, 5)]
        coeffs = np.polyfit([c[0] for c in fake_coords], [c[1] for c in fake_coords], 3)
        poly_func = np.poly1d(coeffs)
        
        fake_graph = self.axes.plot(lambda x: poly_func(x), color=ORANGE, x_range=[0.5, 4.5])
        self.play(Create(fake_graph))
        
        msg1 = Text("Cheater submits a curve connecting Input(16) to Result(5)...", font_size=20, color=ORANGE).to_edge(DOWN)
        self.play(Write(msg1))
        self.wait(2)
        
        # 3. VERIFIER CHECK (Gate 2 Logic)
        # G2 MUST be 16 - 21 = -5.
        real_g2 = Dot(self.axes.c2p(2, -5), color=YELLOW)
        
        # FIXED: Moved label to the RIGHT to avoid clashing with Orange Curve
        real_lbl = Text("Logic Check:\n16 - 21 = -5", font_size=14, color=YELLOW).next_to(real_g2, RIGHT, buff=0.2)
        
        self.play(FadeIn(real_g2), Write(real_lbl))
        self.play(Indicate(real_g2, scale_factor=2))
        
        # 4. Show the Miss
        # Arrow from curve point (2,0) to real point (2,-5)
        curve_point_at_2 = self.axes.c2p(2, 0)
        arrow = Arrow(curve_point_at_2, real_g2.get_center(), color=RED, buff=0)
        miss_lbl = Text("MISMATCH!", color=RED, font_size=24, weight=BOLD).next_to(arrow, RIGHT)
        
        self.play(GrowArrow(arrow), Write(miss_lbl))
        
        msg2 = Text("The Curve misses the Logic Constraint. PROOF REJECTED.", font_size=24, color=RED).to_edge(DOWN)
        self.play(ReplacementTransform(msg1, msg2))
        
        self.wait(5)

    # Helper
    def create_node(self, label, pos, color):
        c = Circle(radius=0.4, color=color, fill_opacity=0.2).move_to(pos)
        t = Text(label, font_size=16).move_to(c)
        return VGroup(c, t)
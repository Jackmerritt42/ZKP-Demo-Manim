from manim import *
import numpy as np

class ShorsFinalFixed(Scene):
    def construct(self):
        
        # ==========================================
        # SCENE 1: PRIMER - THE SEARCH COMPARISON
        # ==========================================
        
        title_search = Text("The Difference: Finding the Needle", font_size=36).to_edge(UP)
        self.play(Write(title_search))

        classical_label = Text("Classical", font_size=24, color=BLUE).shift(LEFT*3.5 + UP*2)
        quantum_label = Text("Quantum", font_size=24, color=PURPLE).shift(RIGHT*3.5 + UP*2)
        self.play(FadeIn(classical_label), FadeIn(quantum_label))

        def create_grid(color, location):
            grid = VGroup()
            for i in range(5):
                for j in range(5):
                    sq = Square(side_length=0.4, color=color, fill_opacity=0.2)
                    sq.move_to(location + LEFT + UP + RIGHT*j*0.5 + DOWN*i*0.5)
                    grid.add(sq)
            return grid

        grid_c = create_grid(BLUE, LEFT*3.5)
        grid_q = create_grid(PURPLE, RIGHT*3.5)
        self.play(Create(grid_c), Create(grid_q))
        
        target_index = 12 
        
        # Classical Animation
        for i in range(6): 
            sq = grid_c[i]
            self.play(sq.animate.set_color(RED).set_fill(opacity=0.5), run_time=0.1)
            self.play(sq.animate.set_color(BLUE).set_fill(opacity=0.2), run_time=0.1)
        
        c_text = Text("Checks 1 by 1...", font_size=20, color=BLUE).next_to(grid_c, DOWN)
        self.play(Write(c_text))

        # Quantum Animation
        self.play(grid_q.animate.set_color(TEAL).set_fill(opacity=0.5), run_time=0.8)
        
        animations = []
        for i in range(25):
            if i == target_index:
                animations.append(grid_q[i].animate.set_color(YELLOW).set_fill(opacity=1).scale(1.2))
            else:
                animations.append(grid_q[i].animate.set_fill(opacity=0.05).scale(0.8))
        
        self.play(*animations, run_time=0.8)
        
        q_text = Text("Pattern Found", font_size=20, color=PURPLE).next_to(grid_q, DOWN)
        self.play(Write(q_text))
        
        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects)))


        # ==========================================
        # SCENE 1.5: THE BUILDING BLOCK (QUBITS)
        # ==========================================
        
        title_bit = Text("The Building Block: Qubits", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(title_bit))

        # --- LEFT: CLASSICAL BIT ---
        # LAYOUT FIX: Centered vertically between Title (Top) and Box (Bottom)
        bit_title = Text("Classical Bit", font_size=24, color=BLUE).move_to(LEFT*3.5 + UP*2.0)
        bit_val = Text("0", font_size=60, color=BLUE).next_to(bit_title, DOWN, buff=0.5)
        
        self.play(Write(bit_title), FadeIn(bit_val))
        self.wait(0.5)
        
        # Flip Animation
        self.play(Transform(bit_val, Text("1", font_size=60, color=BLUE).move_to(bit_val)))
        self.play(Transform(bit_val, Text("0", font_size=60, color=BLUE).move_to(bit_val)))
        
        bit_desc = Text("Heads OR Tails", font_size=20, color=GREY).next_to(bit_val, DOWN)
        self.play(Write(bit_desc))


        # --- RIGHT: QUBIT ---
        # LAYOUT FIX: Centered vertically
        qubit_title = Text("Quantum Bit (Qubit)", font_size=24, color=PURPLE).move_to(RIGHT*3.5 + UP*2.0)
        
        # Visual: Center circle at UP*0.5 to match the Classical Bit visually
        circle = Circle(radius=0.8, color=PURPLE, fill_opacity=0.2).move_to(RIGHT*3.5 + UP*0.5)
        arrow = Vector(UP*0.8, color=YELLOW).move_to(circle.get_center())
        
        self.play(Write(qubit_title), Create(circle), GrowArrow(arrow))
        
        # Spin Animation
        self.play(Rotate(arrow, angle=2*PI, about_point=circle.get_center()), run_time=2)
        
        qubit_desc = Text("Heads AND Tails", font_size=20, color=GREY).next_to(circle, DOWN)
        super_text = Text("(Superposition)", font_size=20, color=YELLOW).next_to(qubit_desc, DOWN)
        
        self.play(Write(qubit_desc), Write(super_text))
        self.wait(1)
        
        # --- THE ANALOGY BLURB ---
        # Fixed to bottom edge. 
        # Coordinates: DOWN*3.0 puts center near bottom, top edge around DOWN*2.0
        # Diagrams end around DOWN*0.5, so there is a large 1.5 unit gap.
        analogy_box = RoundedRectangle(height=2.0, width=9, color=YELLOW, fill_opacity=0.1).to_edge(DOWN)
        analogy_title = Text("Visual Analogy: The Spinning Coin", font_size=16, color=YELLOW).next_to(analogy_box, UP, buff=0)
        
        analogy_text = Text(
            "Classical Bit = Coin resting on table (Definite state).\n"
            "Qubit = Coin spinning on table (Probability of both).",
            font_size=24
        ).move_to(analogy_box)
        
        self.play(Create(analogy_box), Write(analogy_title), Write(analogy_text))
        self.wait(3)
        
        self.play(FadeOut(Group(*self.mobjects)))


        # ==========================================
        # SCENE 2: CAPABILITIES (What is it good at?)
        # ==========================================
        
        title_cap = Text("So... What is a quantum computer good at?", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(title_cap))
        
        # Left Column: Bad At
        bad_title = Text("BAD AT", font_size=28, color=RED).shift(LEFT*3.5 + UP*1.5)
        bad_list = VGroup(
            Text("• Simple Arithmetic", font_size=20),
            Text("• Brute Force Search", font_size=20),
            Text("• Checking every option", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(bad_title, DOWN)
        
        self.play(Write(bad_title), FadeIn(bad_list))
        
        # Right Column: Good At
        good_title = Text("GOOD AT", font_size=28, color=GREEN).shift(RIGHT*3.5 + UP*1.5)
        good_list = VGroup(
            Text("• Finding Global Patterns", font_size=20),
            Text("• Period Finding", font_size=20),
            Text("• Symmetry", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(good_title, DOWN)
        
        self.play(Write(good_title), FadeIn(good_list))
        self.wait(1)
        
        # The Explanation
        expl_box = RoundedRectangle(height=2, width=8, color=YELLOW, fill_opacity=0.1).shift(DOWN*2)
        expl_title = Text("HOW?", font_size=24, color=YELLOW).next_to(expl_box, UP)
        
        expl_text_1 = Text("It plays a statistics game (Constructive Interference).", font_size=24).move_to(expl_box.get_center() + UP*0.3)
        expl_text_2 = Text("Wrong answers cancel out. Right answers build up.", font_size=24).next_to(expl_text_1, DOWN)
        
        self.play(Create(expl_box), Write(expl_title))
        self.play(Write(expl_text_1))
        self.play(Write(expl_text_2))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))


        # ==========================================
        # SCENE 3: SHOR'S SETUP (N=15) + REALITY CHECK
        # ==========================================
        
        title = Text("Shor's Algorithm: The Math", font_size=36).to_edge(UP)
        subtitle = Text("Using Quantum Math to break Classical RSA", font_size=24, color=RED).next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)

        n_label = MathTex("N = 15", font_size=60).shift(UP*1)
        factors = MathTex("? \\times ? = 15", font_size=60).next_to(n_label, DOWN)
        self.play(Write(n_label), Write(factors))
        self.wait(1)
        
        # REALITY CHECK
        reality_text = Text("REALITY CHECK", font_size=24, color=RED).to_corner(UL)
        huge_num_str = "129807421987124..."
        huge_num = Text(huge_num_str, font_size=48, color=GRAY).move_to(n_label)
        huge_desc = Text("(Real keys have 600+ digits!)", font_size=20, color=RED).next_to(huge_num, DOWN)
        
        self.play(FadeIn(reality_text))
        self.play(Transform(n_label, huge_num), FadeOut(factors))
        self.play(FadeIn(huge_desc))
        self.wait(2)
        
        # Revert to N=15
        self.play(FadeOut(huge_desc), FadeOut(reality_text))
        demo_n = MathTex("N = 15", font_size=60).shift(UP*1) 
        self.play(Transform(n_label, demo_n))
        self.play(FadeOut(n_label))

        # Step 1
        step1 = Text("Step 1: Pick a random guess 'a'", font_size=32, color=PURPLE).to_edge(UP)
        self.play(Transform(title, step1), FadeOut(subtitle))

        guess_expl = MathTex("a = 7", font_size=48).shift(UP*1)
        reason = Text("(We just pick a random number less than 15)", font_size=20, color=GREY).next_to(guess_expl, DOWN)
        retry_text = Text("(If the math fails later, we just pick a new 'a' and retry)", font_size=16, color=YELLOW).next_to(reason, DOWN)
        
        self.play(Write(guess_expl), FadeIn(reason))
        self.play(FadeIn(retry_text))
        self.wait(2)
        self.play(FadeOut(guess_expl), FadeOut(reason), FadeOut(retry_text))


        # ==========================================
        # SCENE 4: THE PATTERN (Modular Exponentiation)
        # ==========================================
        
        step2 = Text("Step 2: Create the Function", font_size=32, color=PURPLE).to_edge(UP)
        self.play(Transform(title, step2))

        func_label = MathTex("f(x) = 7^x \\pmod{15}", font_size=36).to_edge(UR, buff=1.0)
        self.play(Write(func_label))
        
        # Why this function?
        why_label = Text("Why this function?", font_size=24, color=YELLOW).next_to(func_label, DOWN, buff=0.5)
        why_expl = Text("If we find its Period (repetition),", font_size=20).next_to(why_label, DOWN)
        why_expl2 = Text("we find the Factors.", font_size=20).next_to(why_expl, DOWN)
        
        self.play(Write(why_label), Write(why_expl), Write(why_expl2))
        self.wait(2)
        self.play(FadeOut(why_label), FadeOut(why_expl), FadeOut(why_expl2))

        values = [1, 7, 4, 13, 1, 7, 4, 13] 
        
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 15, 5],
            x_length=9,
            y_length=3,
            axis_config={"include_numbers": True}
        ).shift(UP*0.5)
        
        labels = axes.get_axis_labels(x_label="x", y_label="Result")
        self.play(Create(axes), Write(labels))

        dots = VGroup()
        for i, val in enumerate(values):
            dot = Dot(point=axes.c2p(i, val), color=YELLOW)
            dots.add(dot)
        
        graph = axes.plot_line_graph(x_values=list(range(8)), y_values=values, line_color=YELLOW, add_vertex_dots=False)
        self.play(Create(graph), FadeIn(dots))

        brace = Brace(Line(axes.c2p(0,0), axes.c2p(4,0)), DOWN, buff=0.5)
        period_label = brace.get_text("Period (r) = ?")
        self.play(GrowFromCenter(brace), Write(period_label))
        
        self.wait(1)


        # ==========================================
        # SCENE 5: FINDING FREQUENCY (Interference)
        # ==========================================
        
        step3 = Text("Step 3: Find the Frequency", font_size=32, color=PURPLE).to_edge(UP)
        self.play(Transform(title, step3))

        self.play(FadeOut(dots), FadeOut(graph))

        # Wrong Wave
        wrong_wave = axes.plot(lambda x: 7.5 + 5*np.sin(2*x), color=RED, x_range=[0, 8])
        wrong_text = Text("Wrong Fit", font_size=20, color=RED).next_to(wrong_wave, UP).shift(RIGHT*2)
        
        self.play(Create(wrong_wave), Write(wrong_text))
        self.wait(0.5)
        self.play(FadeOut(wrong_wave), FadeOut(wrong_text))
        
        # Correct Wave
        correct_wave = axes.plot(lambda x: 7.5 + 6*np.cos((PI/2)*x), color=GREEN, x_range=[0, 8])
        correct_text = Text("Correct Fit!", font_size=20, color=GREEN).next_to(correct_wave, UP).shift(RIGHT*2)
        
        # Disclosures
        approx_text = Text("*Visualizing discrete quantum states as a continuous wave", font_size=14, color=GREY).to_corner(DR).shift(UP*1.0)
        disclaimer = Text("*QFT is complex linear algebra, simplified here as curve fitting", font_size=14, color=GREY).next_to(approx_text, DOWN)
        prob_text = Text("*Measurement is probabilistic (might need multiple runs)", font_size=14, color=GREY).next_to(disclaimer, DOWN)
        
        self.play(Create(correct_wave), Write(correct_text))
        self.play(FadeIn(approx_text), FadeIn(disclaimer), FadeIn(prob_text))
        
        final_r = MathTex("r = 4", font_size=40, color=GREEN).next_to(brace, DOWN)
        self.play(Transform(period_label, final_r))
        self.wait(1)

        graph_group = VGroup(
            axes, labels, correct_wave, correct_text, brace, 
            period_label, func_label, approx_text, disclaimer, prob_text
        )
        self.play(FadeOut(graph_group))


        # ==========================================
        # SCENE 6: THE CRACK (Calculation)
        # ==========================================
        
        step4 = Text("Step 4: The Crack", font_size=32, color=RED).to_edge(UP)
        self.play(Transform(title, step4))

        ref_r = MathTex("r = 4", font_size=36, color=GREEN).to_edge(UL, buff=1.0).shift(DOWN*1)
        ref_a = MathTex("a = 7", font_size=36, color=PURPLE).next_to(ref_r, DOWN)
        self.play(Write(ref_r), Write(ref_a))

        math_1 = MathTex("\\text{Guess}^ {r/2} \\pm 1", font_size=48).shift(UP*1)
        math_2 = MathTex("7^{4/2} \\pm 1", font_size=48).next_to(math_1, DOWN)
        math_3 = MathTex("49 \\pm 1", font_size=48).next_to(math_2, DOWN)
        
        self.play(Write(math_1))
        self.wait(0.5)
        self.play(Transform(math_1.copy(), math_2))
        self.wait(0.5)
        self.play(Transform(math_2.copy(), math_3))

        num_a = MathTex("48", color=BLUE).shift(LEFT*2 + DOWN*1.5)
        num_b = MathTex("50", color=BLUE).shift(RIGHT*2 + DOWN*1.5)
        
        self.play(Write(num_a), Write(num_b))
        
        gcd_a = MathTex("GCD(48, 15) = \\mathbf{3}", font_size=48, color=YELLOW).next_to(num_a, DOWN)
        gcd_b = MathTex("GCD(50, 15) = \\mathbf{5}", font_size=48, color=YELLOW).next_to(num_b, DOWN)
        
        self.play(Write(gcd_a), Write(gcd_b))
        self.wait(1)

        self.play(FadeOut(Group(*self.mobjects)))
        
        final_factors = MathTex("15 = 3 \\times 5", font_size=80, color=GREEN).move_to(ORIGIN)
        self.play(FadeIn(final_factors))
        self.play(Indicate(final_factors))
        self.wait(3)
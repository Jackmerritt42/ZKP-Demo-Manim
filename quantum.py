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
        
        # FIX: Changed to "Amplifies Correct Pattern" to avoid the "Instant Magic" myth
        q_text = Text("Amplifies Correct Pattern", font_size=20, color=PURPLE).next_to(grid_q, DOWN)
        self.play(Write(q_text))
        
        self.wait(1)
        
        # NUCLEAR CLEANUP 1
        self.play(FadeOut(Group(*self.mobjects)))


        # ==========================================
        # SCENE 2: SHOR'S SETUP (N=15)
        # ==========================================
        
        title = Text("Shor's Algorithm: The Math", font_size=36).to_edge(UP)
        self.play(Write(title))

        n_label = MathTex("N = 15", font_size=60).shift(UP*1)
        factors = MathTex("? \\times ? = 15", font_size=60).next_to(n_label, DOWN)
        self.play(Write(n_label), Write(factors))
        self.wait(1)
        
        self.play(FadeOut(n_label), FadeOut(factors))

        step1 = Text("Step 1: Pick a random guess 'a'", font_size=32, color=PURPLE).to_edge(UP)
        self.play(Transform(title, step1))

        guess_expl = MathTex("a = 7", font_size=48).shift(UP*1)
        reason = Text("(We just pick a random number less than 15)", font_size=20, color=GREY).next_to(guess_expl, DOWN)
        
        self.play(Write(guess_expl), FadeIn(reason))
        self.wait(1.5)
        self.play(FadeOut(guess_expl), FadeOut(reason))


        # ==========================================
        # SCENE 3: THE PATTERN (Modular Exponentiation)
        # ==========================================
        
        step2 = Text("Step 2: Create the Function", font_size=32, color=PURPLE).to_edge(UP)
        self.play(Transform(title, step2))

        func_label = MathTex("f(x) = 7^x \\pmod{15}", font_size=36).to_edge(UR, buff=1.0)
        self.play(Write(func_label))

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

        brace = Brace(Line(axes.c2p(0,0), axes.c2p(4,0)), DOWN)
        period_label = brace.get_text("Period (r) = ?")
        self.play(GrowFromCenter(brace), Write(period_label))
        
        self.wait(1)


        # ==========================================
        # SCENE 4: FINDING FREQUENCY (Interference)
        # ==========================================
        
        step3 = Text("Step 3: Find the Frequency", font_size=32, color=PURPLE).to_edge(UP)
        self.play(Transform(title, step3))

        # Fade out the noisy data points so we can see the wave clearly
        self.play(FadeOut(dots), FadeOut(graph))

        # Wrong Wave (Red)
        wrong_wave = axes.plot(lambda x: 7.5 + 5*np.sin(2*x), color=RED, x_range=[0, 8])
        wrong_text = Text("Wrong Fit", font_size=20, color=RED).next_to(wrong_wave, UP).shift(RIGHT*2)
        
        self.play(Create(wrong_wave), Write(wrong_text))
        self.wait(0.5)
        self.play(FadeOut(wrong_wave), FadeOut(wrong_text))
        
        # Correct Wave (Green)
        correct_wave = axes.plot(lambda x: 7.5 + 6*np.cos((PI/2)*x), color=GREEN, x_range=[0, 8])
        correct_text = Text("Correct Fit!", font_size=20, color=GREEN).next_to(correct_wave, UP).shift(RIGHT*2)
        
        # FIX: Added disclosure that this is a continuous visual of a discrete process
        approx_text = Text("(Continuous Approximation)", font_size=14, color=GREY).next_to(correct_text, DOWN)
        
        self.play(Create(correct_wave), Write(correct_text), FadeIn(approx_text))
        
        final_r = MathTex("r = 4", font_size=40, color=GREEN).next_to(brace, DOWN)
        self.play(Transform(period_label, final_r))
        self.wait(1)

        # Clear Graph for Math step
        graph_group = VGroup(axes, labels, correct_wave, correct_text, brace, period_label, func_label, approx_text)
        self.play(FadeOut(graph_group))


        # ==========================================
        # SCENE 5: THE CRACK (Calculation)
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

        # NUCLEAR CLEANUP 2 (The Fix)
        # Fade out EVERY object currently on screen
        self.play(FadeOut(Group(*self.mobjects)))
        
        # Now fade in the final answer on a clean slate
        final_factors = MathTex("15 = 3 \\times 5", font_size=80, color=GREEN).move_to(ORIGIN)
        self.play(FadeIn(final_factors))
        
        self.play(Indicate(final_factors))
        self.wait(3)
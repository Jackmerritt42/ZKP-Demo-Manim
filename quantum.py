from manim import *
import numpy as np

class ShorsAlgorithmDeepDive(Scene):
    def construct(self):
        # ==========================================
        # SCENE 1: THE SETUP (The Impossible Problem)
        # ==========================================
        
        # Title
        title = Text("How Shor's Algorithm Actually Works", font_size=36).to_edge(UP)
        self.play(Write(title))

        # The Number to Factor (N=15)
        # We use 15 because it's small enough to visualize, but the logic holds for huge numbers
        n_label = MathTex("N = 15", font_size=60).shift(UP*1)
        factors = MathTex("? \\times ? = 15", font_size=60).next_to(n_label, DOWN)
        
        self.play(Write(n_label), Write(factors))
        self.wait(1)

        # Classical Computer trying to guess
        guess_text = Text("Classical Computer: Guessing...", font_size=24, color=BLUE).shift(DOWN*1.5)
        self.play(FadeIn(guess_text))
        
        guess_num = Integer(2).next_to(guess_text, DOWN)
        self.add(guess_num)
        
        # Rapidly cycle through numbers to show "brute force"
        for i in [2, 3, 4, 5]:
            guess_num.set_value(i)
            self.wait(0.2)
        
        fail_comment = Text("(Easy for 15, Impossible for 2048-bit keys)", font_size=20, color=RED).next_to(guess_num, DOWN)
        self.play(Write(fail_comment))
        self.wait(1.5)
        
        # Clear Scene 1
        self.play(FadeOut(Group(n_label, factors, guess_text, guess_num, fail_comment)))


        # ==========================================
        # SCENE 2: THE QUANTUM TRANSFORMATION
        # ==========================================
        
        step1 = Text("Step 1: Convert to a Pattern", font_size=32, color=PURPLE).to_edge(UP)
        self.play(Transform(title, step1))

        # Explanation: Shor's turns factoring into a "Period Finding" problem
        # We pick a random guess 'a' (let's pick 7)
        # Function: f(x) = 7^x mod 15
        
        func_label = MathTex("f(x) = 7^x \\pmod{15}", font_size=48).shift(UP*1.5)
        self.play(Write(func_label))

        # Show the sequence generation (Superposition allows us to calculate these all at once implicitly)
        # x = 0 -> 7^0 = 1
        # x = 1 -> 7^1 = 7
        # x = 2 -> 7^2 = 49 -> 4 (49 % 15)
        # x = 3 -> 7^3 = 343 -> 13
        # x = 4 -> 7^4 ... -> 1
        
        results = VGroup()
        values = [1, 7, 4, 13, 1, 7, 4, 13] # The repeating pattern
        
        # Draw a simple number line / graph
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 15, 5],
            x_length=8,
            y_length=3,
            axis_config={"include_numbers": True}
        ).shift(DOWN*0.5)
        
        labels = axes.get_axis_labels(x_label="x", y_label="Result")
        self.play(Create(axes), Write(labels))

        # Plot points one by one (representing the calculation)
        dots = VGroup()
        for i, val in enumerate(values):
            dot = Dot(point=axes.c2p(i, val), color=YELLOW)
            dots.add(dot)
            if i < 4: # Only animate the first few slowly
                self.play(FadeIn(dot), run_time=0.3)
            else:
                self.add(dot) # Speed up
        
        # Connect them to show the pattern
        graph = axes.plot_line_graph(x_values=list(range(8)), y_values=values, line_color=YELLOW, add_vertex_dots=False)
        self.play(Create(graph))

        pattern_text = Text("Look! It repeats!", font_size=24, color=YELLOW).next_to(graph, UP)
        self.play(Write(pattern_text))
        
        # Highlight the "Period"
        # From x=0 to x=4, the pattern restarts. So Period (r) = 4.
        brace = Brace(Line(axes.c2p(0,0), axes.c2p(4,0)), UP)
        period_label = brace.get_text("Period (r) = ?")
        self.play(GrowFromCenter(brace), Write(period_label))
        
        self.wait(1)
        
        # Clear for next step
        self.play(FadeOut(Group(func_label, results, dots, graph, pattern_text, step1)))


        # ==========================================
        # SCENE 3: QUANTUM FOURIER TRANSFORM (Finding 'r')
        # ==========================================
        
        step2 = Text("Step 2: Find the Frequency (QFT)", font_size=32, color=PURPLE).to_edge(UP)
        self.play(Transform(title, step2))

        # Explanation: A classical computer has to check x=1, x=2, x=3... to find the repeat.
        # A Quantum computer throws a "Wave" at the data to see what fits.
        
        # Move axes down slightly
        self.play(axes.animate.shift(DOWN*0.5), brace.animate.shift(DOWN*0.5), period_label.animate.shift(DOWN*0.5))

        # Visualizing Constructive Interference
        # We try a "Wrong" frequency first (Red wave)
        wrong_wave = axes.plot(lambda x: 7.5 + 5*np.sin(2*x), color=RED, x_range=[0, 8])
        wrong_text = Text("Wrong Frequency (Destructive)", font_size=20, color=RED).to_edge(RIGHT).shift(UP)
        
        self.play(Create(wrong_wave), Write(wrong_text))
        self.wait(0.5)
        self.play(FadeOut(wrong_wave), FadeOut(wrong_text))
        
        # We try the "Correct" frequency (Green wave)
        # The period is 4.
        correct_wave = axes.plot(lambda x: 7.5 + 6*np.cos((PI/2)*x), color=GREEN, x_range=[0, 8])
        correct_text = Text("Correct Frequency!", font_size=20, color=GREEN).to_edge(RIGHT).shift(UP)
        
        self.play(Create(correct_wave), Write(correct_text))
        
        # The Quantum Computer "collapses" on this answer
        final_r = MathTex("r = 4", font_size=40, color=GREEN).next_to(brace, UP)
        self.play(Transform(period_label, final_r))
        self.play(Indicate(final_r))
        
        self.wait(1)
        self.play(FadeOut(Group(axes, labels, correct_wave, correct_text, brace, period_label, title)))


        # ==========================================
        # SCENE 4: THE CRACK (The Math)
        # ==========================================
        
        step3 = Text("Step 3: The Crack", font_size=32, color=RED).to_edge(UP)
        self.play(Write(step3))

        # Now we have r=4. The math is simple from here.
        # Formula: Factors share GCD with (guess^(r/2) +/- 1)
        
        # guess = 7, r = 4
        math_1 = MathTex("\\text{Guess}^ {r/2} \\pm 1", font_size=48).shift(UP*1)
        math_2 = MathTex("7^{4/2} \\pm 1", font_size=48).next_to(math_1, DOWN)
        math_3 = MathTex("7^2 \\pm 1 \\rightarrow 49 \\pm 1", font_size=48).next_to(math_2, DOWN)
        
        self.play(Write(math_1))
        self.wait(0.5)
        self.play(Transform(math_1.copy(), math_2))
        self.wait(0.5)
        self.play(Transform(math_2.copy(), math_3))

        # Calculate the two numbers
        num_a = MathTex("49 - 1 = 48", color=BLUE).shift(LEFT*3 + DOWN*1.5)
        num_b = MathTex("49 + 1 = 50", color=BLUE).shift(RIGHT*3 + DOWN*1.5)
        
        self.play(Write(num_a), Write(num_b))
        
        # GCD Calculation
        # GCD(48, 15) = 3
        # GCD(50, 15) = 5
        
        gcd_a = MathTex("GCD(48, 15) = \\mathbf{3}", font_size=60, color=YELLOW).next_to(num_a, DOWN)
        gcd_b = MathTex("GCD(50, 15) = \\mathbf{5}", font_size=60, color=YELLOW).next_to(num_b, DOWN)
        
        self.play(Write(gcd_a), Write(gcd_b))
        
        final_factors = MathTex("15 = 3 \\times 5", font_size=80, color=GREEN).move_to(ORIGIN).shift(DOWN*1)
        
        # Clear math to show final result
        self.play(
            FadeOut(math_1), FadeOut(math_2), FadeOut(math_3), 
            FadeOut(num_a), FadeOut(num_b),
            Transform(Group(gcd_a, gcd_b), final_factors)
        )
        
        self.play(Indicate(final_factors))
        self.wait(3)
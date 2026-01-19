from manim import *

class FullPresentation(Scene):
    def construct(self):
        # ==========================================
        # PART 1: SEARCH COMPARISON (Classical vs Quantum)
        # ==========================================
        
        title = Text("The Search Problem", font_size=40).to_edge(UP)
        subtitle = Text("Why Quantum breaks encryption keys", font_size=24, color=GREY).next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        
        line = Line(UP*2, DOWN*3)
        self.play(Create(line))

        classical_label = Text("Classical Computer", font_size=28, color=BLUE).to_edge(LEFT, buff=1.5).shift(UP*2)
        quantum_label = Text("Quantum Computer", font_size=28, color=PURPLE).to_edge(RIGHT, buff=1.5).shift(UP*2)
        self.play(FadeIn(classical_label), FadeIn(quantum_label))

        # --- Grids ---
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
        
        # --- Classical Animation ---
        self.play(Indicate(classical_label))
        desc_c = Text("Low Overhead, Sequential", font_size=20, color=BLUE).next_to(grid_c, DOWN)
        self.play(Write(desc_c))
        
        for i in range(target_index + 1):
            sq = grid_c[i]
            if i == target_index:
                self.play(sq.animate.set_color(YELLOW).set_fill(opacity=1), run_time=0.5)
                found_text_c = Text("FOUND (13 steps)", font_size=24, color=YELLOW).next_to(grid_c, UP)
                self.play(Write(found_text_c))
            else:
                self.play(sq.animate.set_color(RED).set_fill(opacity=0.5), run_time=0.05)
                self.play(sq.animate.set_color(BLUE).set_fill(opacity=0.2), run_time=0.05)

        self.wait(0.5)

        # --- Quantum Animation ---
        self.play(Indicate(quantum_label))
        
        # 1. Inefficiency
        overhead_text = Text("Initializing (High Overhead)...", font_size=20, color=GREY).next_to(grid_q, DOWN)
        self.play(Write(overhead_text))
        loading_dots = VGroup(*[Circle(radius=0.05, color=WHITE, fill_opacity=1) for _ in range(3)]).arrange(RIGHT).next_to(overhead_text, DOWN)
        self.play(FadeIn(loading_dots))
        self.play(
            loading_dots[0].animate.set_color(PURPLE),
            loading_dots[1].animate.set_color(PURPLE),
            loading_dots[2].animate.set_color(PURPLE),
            run_time=1.0 
        )
        self.play(FadeOut(loading_dots), FadeOut(overhead_text))

        # 2. Superposition
        desc_q = Text("Superposition", font_size=20, color=PURPLE).next_to(grid_q, DOWN)
        self.play(Write(desc_q))
        self.play(grid_q.animate.set_color(TEAL).set_fill(opacity=0.5), run_time=1)
        
        # 3. Collapse
        self.play(Transform(desc_q, Text("Measurement Collapse", font_size=20, color=PURPLE).next_to(grid_q, DOWN)))
        animations = []
        for i in range(25):
            if i == target_index:
                animations.append(grid_q[i].animate.set_color(YELLOW).set_fill(opacity=1).scale(1.2))
            else:
                animations.append(grid_q[i].animate.set_fill(opacity=0.05).scale(0.8)) 
        self.play(*animations, run_time=1.5)
        
        found_text_q = Text("FOUND (1 step)", font_size=24, color=YELLOW).next_to(grid_q, UP)
        self.play(Write(found_text_q))
        self.wait(2)

        # Clean up Part 1
        self.play(FadeOut(Group(*self.mobjects)))


        # ==========================================
        # PART 2: SHOR'S ALGORITHM (The "Magic" Split)
        # ==========================================
        
        # Setup
        shor_title = Text("Shor's Algorithm: The Key Breaker", font_size=36).to_edge(UP)
        self.play(Write(shor_title))

        # The "Public Key" (A Big Block)
        # We represent the number N as a solid block that is hard to break
        block = Rectangle(height=2, width=3, color=WHITE, fill_opacity=0.5, fill_color=GREY)
        block_label = Text("Public Key (N)", font_size=24).move_to(block.get_center())
        block_group = VGroup(block, block_label).shift(LEFT * 2)

        self.play(FadeIn(block_group))
        
        # --- Classical Attempt ---
        hammer = Square(side_length=0.5, color=BLUE, fill_opacity=1).next_to(block, RIGHT, buff=0.5)
        hammer_label = Text("Classical", font_size=16, color=BLUE).next_to(hammer, UP)
        
        self.play(FadeIn(hammer), FadeIn(hammer_label))
        
        # Hammer hits block (Animation)
        for _ in range(3):
            self.play(hammer.animate.shift(LEFT * 0.3), run_time=0.1)
            self.play(hammer.animate.shift(RIGHT * 0.3), run_time=0.1)
        
        fail_text = Text("Too Hard.", font_size=20, color=RED).next_to(block, DOWN)
        self.play(Write(fail_text))
        self.wait(0.5)
        self.play(FadeOut(hammer), FadeOut(hammer_label), FadeOut(fail_text))

        # --- Shor's Attempt (Quantum Wave) ---
        wave = FunctionGraph(lambda x: 0.5 * np.sin(3*x), x_range=[-1, 1], color=PURPLE).rotate(PI/2).next_to(block, RIGHT, buff=1)
        wave_label = Text("Shor's Algo", font_size=16, color=PURPLE).next_to(wave, UP)

        self.play(FadeIn(wave), FadeIn(wave_label))
        
        # Wave passes THROUGH the block
        self.play(
            wave.animate.move_to(block.get_center()).scale(2),
            run_time=1.0
        )
        
        # The Block SPLITS (Factoring)
        # Create two smaller blocks
        factor1 = Rectangle(height=2, width=1.4, color=RED, fill_opacity=0.8).move_to(block.get_center()).shift(LEFT*0.8)
        factor2 = Rectangle(height=2, width=1.4, color=RED, fill_opacity=0.8).move_to(block.get_center()).shift(RIGHT*0.8)
        
        f1_label = Text("Private", font_size=16).move_to(factor1.get_center())
        f2_label = Text("Key", font_size=16).move_to(factor2.get_center())

        self.play(
            FadeOut(block), FadeOut(block_label), FadeOut(wave),
            FadeIn(factor1), FadeIn(f1_label),
            FadeIn(factor2), FadeIn(f2_label),
            run_time=0.5
        )
        
        success_text = Text("Factored Instantly!", font_size=24, color=YELLOW).next_to(factor1, DOWN).shift(RIGHT*0.8)
        self.play(Write(success_text))
        self.wait(2)

        # Final Cleanup
        self.play(FadeOut(Group(*self.mobjects)))

        # Final Summary
        final_text = Paragraph(
            "Shor's Algorithm finds the 'crack' in the math",
            "that holds the Public Key together.",
            alignment="center", font_size=32
        )
        self.play(Write(final_text))
        self.wait(3)
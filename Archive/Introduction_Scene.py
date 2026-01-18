# old document, probably not needed... used to build ZKP Story mode / ZKP presentation files

from manim import *

class ZKP_Unified_Explainer(Scene):
    def construct(self):
        self.part_1_definition()
        self.part_2_privacy()
        self.part_3_scaling()
        self.part_4_conclusion()

    def part_1_definition(self):
        # --- TITLE ---
        title = Text("Zero-Knowledge Proofs", font_size=48, color=BLUE).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # --- SETUP ---
        # Create Prover (Alice) and Verifier (Bob)
        prover = Text("Prover", color=GREEN, font_size=36).shift(LEFT * 4)
        verifier = Text("Verifier", color=RED, font_size=36).shift(RIGHT * 4)
        self.play(Write(prover), Write(verifier))

        # --- THE SECRET ---
        # The secret stays with the Prover
        secret_box = Square(side_length=1.2, color=YELLOW, fill_opacity=0.5).next_to(prover, DOWN)
        secret_text = Text("Secret", font_size=20).move_to(secret_box)
        secret_group = VGroup(secret_box, secret_text)
        
        self.play(GrowFromCenter(secret_group))
        self.wait(0.5)

        # --- THE PROOF ---
        # Prover generates a separate object: The Proof
        proof_doc = RoundedRectangle(height=1, width=0.8, corner_radius=0.1, color=BLUE, fill_opacity=0.2).next_to(secret_group, RIGHT)
        proof_label = Text("Proof", font_size=16).move_to(proof_doc)
        proof_group = VGroup(proof_doc, proof_label)

        self.play(FadeIn(proof_group))
        self.wait(0.5)

        # --- THE TRANSFER ---
        # KEY VISUAL: The Proof travels, the Secret stays put
        self.play(proof_group.animate.move_to(verifier.get_center() + DOWN*1.5), run_time=2)
        
        # Verifier checks it
        check = Text("TRUE", color=GREEN, font_size=24).next_to(proof_group, DOWN)
        self.play(Write(check))
        self.wait(2)

        # Cleanup
        self.play(FadeOut(Group(*self.mobjects)))

    def part_2_privacy(self):
        # --- LOGIC 1: PRIVACY (SELECTIVE DISCLOSURE) ---
        title = Text("Application 1: Privacy", font_size=40).to_edge(UP)
        self.play(Write(title))

        # The Data Silo (ID Card)
        id_card = RoundedRectangle(height=4, width=6, corner_radius=0.2, color=WHITE)
        
        # FIXED: Changed align_edge to aligned_edge
        data = VGroup(
            Text("Name: Alice", font_size=24),
            Text("Address: 123 Main St", font_size=24),
            Text("SSN: XXX-XX-XXXX", font_size=24, color=RED),
            Text("DOB: 01/01/1990", font_size=24, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT).move_to(id_card)
        
        full_id = VGroup(id_card, data)
        self.play(Create(id_card), Write(data))
        self.wait(1)

        # The Logic: We only want to prove ONE fact (Age > 21)
        # Mask everything else
        mask = Rectangle(width=6.1, height=4.1, fill_color=BLACK, fill_opacity=0.95, stroke_color=BLUE)
        result = Text("Age > 21: YES", color=GREEN, font_size=40)
        
        self.play(FadeIn(mask))
        self.play(Write(result))
        self.wait(2)
        
        # Cleanup
        self.play(FadeOut(Group(*self.mobjects)))

    def part_3_scaling(self):
        # --- LOGIC 2: SCALING (COMPRESSION) ---
        title = Text("Application 2: Scaling", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Visual: Many transactions becoming one
        # Create 10 small squares representing "Transactions"
        txs = VGroup(*[Square(side_length=0.5, color=WHITE) for _ in range(10)])
        txs.arrange_in_grid(rows=2, buff=0.2)
        
        label_tx = Text("1000+ Transactions", font_size=24).next_to(txs, DOWN)
        
        self.play(Create(txs), Write(label_tx))
        self.wait(1)

        # Compress them into one ZKP
        proof_box = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        proof_label = Text("1 Proof", font_size=20).move_to(proof_box)
        zk_proof = VGroup(proof_box, proof_label)

        self.play(
            ReplacementTransform(txs, zk_proof),
            FadeOut(label_tx)
        )
        
        # Verify the single proof
        verify_text = Text("Verify Once = Verify All", font_size=30, color=BLUE).next_to(zk_proof, DOWN)
        self.play(Write(verify_text))
        self.wait(2)

        # Cleanup
        self.play(FadeOut(Group(*self.mobjects)))

    def part_4_conclusion(self):
        # --- CONCLUSION ---
        final_text = Text("Verify, Don't Trust.", font_size=48, color=YELLOW)
        self.play(Write(final_text))
        self.wait(3)
        self.play(FadeOut(final_text))
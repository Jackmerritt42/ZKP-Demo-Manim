#also old and maybe unneeded? keeping here in case, but ZKP_Presentation is a better more polished version...

from manim import *

class ZKP_Final_Presentation(Scene):
    def construct(self):
        self.part_1_id_card()
        self.part_2_medical_simple()
        self.part_3_core_value()

    def part_1_id_card(self):
        # --- TITLE ---
        title = Text("Part 1: The Core Concept", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # --- THE SCENARIO ---
        # "I want to prove I'm 21 without revealing my address."
        narrative = Text("Goal: Prove Age > 21 without revealing personal data.", font_size=24).next_to(title, DOWN)
        self.play(Write(narrative))

        # --- THE ID CARD (THE PROBLEM) ---
        id_card = RoundedRectangle(height=3.5, width=5.5, corner_radius=0.2, color=WHITE)
        
        # Data Fields
        # Using VGroup and arrange to keep it clean
        photo = Square(side_length=1.2, color=WHITE, fill_opacity=0.2)
        
        data_group = VGroup(
            Text("Name: John Doe", font_size=20),
            Text("Address: 123 Main St", font_size=20, color=RED), # Red to show risk
            Text("DOB: 01/01/1990", font_size=20, color=GREEN),   # Green is what we want
            Text("ID#: A123456789", font_size=20, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Arrange Photo left, Data right
        content = VGroup(photo, data_group).arrange(RIGHT, buff=0.5).move_to(id_card)
        
        full_id = VGroup(id_card, content).shift(DOWN*0.5)
        
        self.play(Create(id_card), FadeIn(content))
        self.wait(1)

        # Highlight the problem (Over-sharing)
        problem_text = Text("Standard ID reveals EVERYTHING.", color=RED, font_size=24).next_to(full_id, DOWN)
        self.play(Write(problem_text))
        self.play(Indicate(data_group[1], color=RED), Indicate(data_group[3], color=RED))
        self.wait(2)

        # --- THE ZKP SOLUTION ---
        self.play(FadeOut(problem_text))
        
        # Create a "Zero Knowledge Mask"
        mask = Rectangle(height=3.6, width=5.6, color=BLUE, fill_opacity=0.95).move_to(id_card)
        
        # The only thing revealed
        zkp_fact = Text("AGE > 21: YES", font_size=40, color=WHITE).move_to(mask)
        zkp_group = VGroup(mask, zkp_fact)

        self.play(FadeIn(zkp_group))
        
        solution_text = Text("ZKP Proof: Verifies the fact, hides the data.", color=GREEN, font_size=24).next_to(zkp_group, DOWN)
        self.play(Write(solution_text))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))

    def part_2_medical_simple(self):
        title = Text("Part 2: Real World Application", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # --- SETUP ---
        # Patient Left, Pharmacy Right. Wide spacing to prevent clash.
        patient = VGroup(Dot(radius=0.2), Text("Patient", font_size=20).next_to(Dot(), DOWN)).to_edge(LEFT, buff=1.5)
        pharmacy = VGroup(Square(side_length=0.4), Text("Pharmacy", font_size=20).next_to(Square(), DOWN)).to_edge(RIGHT, buff=1.5)
        
        self.play(FadeIn(patient), FadeIn(pharmacy))

        # --- THE SECRET ---
        # Diagnosis stays ABOVE the patient to keep center clear
        secret_box = Rectangle(height=0.8, width=2, color=YELLOW, fill_opacity=0.2).next_to(patient, UP, buff=0.5)
        secret_text = Text("Diagnosis:\nSensitive Illness", color=YELLOW, font_size=16).move_to(secret_box)
        secret_group = VGroup(secret_box, secret_text)
        
        self.play(GrowFromCenter(secret_group))
        self.wait(0.5)

        # --- THE REQUIREMENT ---
        # Pharmacy needs to know if patient is eligible
        req_text = Text("Requirement:\nEligible for Medicine?", font_size=16, color=GREY).next_to(pharmacy, UP, buff=0.5)
        self.play(Write(req_text))
        self.wait(1)

        # --- THE PROOF ---
        # Patient creates proof (Blue)
        proof_box = RoundedRectangle(height=0.8, width=1.5, corner_radius=0.2, color=BLUE, fill_opacity=0.5)
        proof_text = Text("ELIGIBLE:\nYES", font_size=16, color=WHITE).move_to(proof_box)
        proof_group = VGroup(proof_box, proof_text).next_to(patient, RIGHT)

        self.play(FadeIn(proof_group))
        
        # Crucial: Show secret staying, Proof moving
        self.play(Indicate(secret_group, scale_factor=1.1)) # Emphasis on secret staying
        
        # Move proof to pharmacy
        self.play(proof_group.animate.next_to(pharmacy, LEFT), run_time=2)
        
        # Success
        check = Text("Dispense Meds", color=GREEN, font_size=20).next_to(proof_group, DOWN)
        self.play(Write(check))
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))

    def part_3_core_value(self):
        # --- TITLE ---
        title = Text("Why This Matters", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # --- MAIN VISUAL ---
        # A locked box (The Secret) -> An arrow -> A Checkmark (The Proof)
        
        secret_box = Square(side_length=2, color=YELLOW, fill_opacity=0.2)
        secret_lbl = Text("My Secret\n(Knowledge)", font_size=20).move_to(secret_box)
        secret_grp = VGroup(secret_box, secret_lbl).shift(LEFT * 3)
        
        arrow = Arrow(LEFT, RIGHT, color=GREY).next_to(secret_grp, RIGHT)
        
        proof_check = Text("✔", font_size=80, color=GREEN).next_to(arrow, RIGHT)
        proof_lbl = Text("The Proof", font_size=24).next_to(proof_check, DOWN)
        
        self.play(Create(secret_grp))
        self.play(GrowArrow(arrow))
        self.play(Write(proof_check), Write(proof_lbl))
        self.wait(1)

        # --- KEY TAKEAWAY TEXT ---
        # "Prove you know it without revealing it"
        main_point = Text("Prove you know the secret...", font_size=32).shift(DOWN * 1.5)
        sub_point = Text("...without ever revealing it.", font_size=32, color=BLUE).next_to(main_point, DOWN)
        
        self.play(Write(main_point))
        self.play(Write(sub_point))
        self.wait(2)

        # --- FINAL TAG ---
        final_tag = Text('"Verify, don\'t trust."', font_size=48, color=YELLOW).to_edge(DOWN, buff=0.5)
        
        # Clear the middle text to make room for the big finish
        self.play(
            FadeOut(main_point), 
            FadeOut(sub_point),
            FadeIn(final_tag)
        )
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))
from manim import *

class ZKP_Final_Presentation(Scene):
    def construct(self):
        self.part_0_intro()
        self.part_1_id_card()
        self.part_2_medical_simple()
        self.part_3_core_value()

    def part_0_intro(self):
        # --- TITLE SEQUENCE ---
        title = Text("Zero-Knowledge Proofs", font_size=48, color=BLUE).to_edge(UP)
        subtitle = Text("The Future of Data Security", font_size=32, color=GREY).next_to(title, DOWN)
        
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)

        # --- DEFINITION ---
        # "What is it?"
        def_box = Rectangle(height=2, width=8, color=WHITE, fill_opacity=0.1)
        def_text = Text(
            "A cryptographic method to prove you know a secret\nwithout revealing the secret itself.", 
            font_size=28, t2c={"without revealing": YELLOW}
        ).move_to(def_box)
        
        self.play(Create(def_box), Write(def_text))
        self.wait(2)

        # --- WHY IT MATTERS ---
        # Clear definition, show "Data Security" aspect
        self.play(FadeOut(def_text), FadeOut(def_box))
        
        # Two pillars
        p1 = VGroup(
            Text("Privacy", color=BLUE, font_size=36),
            Text("Keep data user-controlled", font_size=20, color=GREY)
        ).arrange(DOWN).shift(LEFT * 3)
        
        p2 = VGroup(
            Text("Security", color=GREEN, font_size=36),
            Text("Eliminate data leaks", font_size=20, color=GREY)
        ).arrange(DOWN).shift(RIGHT * 3)

        self.play(FadeIn(p1), FadeIn(p2))
        self.wait(2)
        
        self.play(FadeOut(Group(*self.mobjects)))

    def part_1_id_card(self):
        # --- TITLE ---
        title = Text("Part 1: The Concept", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # --- THE SCENARIO ---
        narrative = Text("Goal: Prove Age > 21 without revealing personal data.", font_size=24).next_to(title, DOWN)
        self.play(Write(narrative))

        # --- THE ID CARD ---
        id_card = RoundedRectangle(height=3.5, width=5.5, corner_radius=0.2, color=WHITE)
        
        # Photo
        photo = Square(side_length=1.2, color=WHITE, fill_opacity=0.2)
        
        # Data Fields (Grouped manually to avoid overlap issues)
        l1 = Text("Name: John Doe", font_size=20)
        l2 = Text("Address: 123 Main St", font_size=20, color=RED)
        l3 = Text("DOB: 01/01/1990", font_size=20, color=GREEN)
        l4 = Text("ID#: A123456789", font_size=20, color=RED)
        
        data_group = VGroup(l1, l2, l3, l4).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        content = VGroup(photo, data_group).arrange(RIGHT, buff=0.5).move_to(id_card)
        full_id = VGroup(id_card, content).shift(DOWN*0.5)
        
        self.play(Create(id_card), FadeIn(content))
        self.wait(1)

        # Highlight problem
        problem_text = Text("Standard ID reveals EVERYTHING.", color=RED, font_size=24).next_to(full_id, DOWN)
        self.play(Write(problem_text))
        self.wait(1)

        # --- THE ZKP SOLUTION ---
        self.play(FadeOut(problem_text))
        
        # Mask - Fully Opaque (fill_opacity=1) to hide text underneath
        mask = Rectangle(height=3.6, width=5.6, color=BLUE, fill_opacity=1).move_to(id_card)
        
        # The Fact
        zkp_fact = Text("AGE > 21: YES", font_size=40, color=WHITE).move_to(mask)
        zkp_group = VGroup(mask, zkp_fact) # Z-index handles order, mask covers ID

        self.play(FadeIn(zkp_group))
        
        solution_text = Text("ZKP Proof: Verifies the fact, hides the data.", color=GREEN, font_size=24).next_to(zkp_group, DOWN)
        self.play(Write(solution_text))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))

    def part_2_medical_simple(self):
        title = Text("Part 2: Real World Application", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # --- SETUP ---
        patient = VGroup(Dot(radius=0.2), Text("Patient", font_size=20).next_to(Dot(), DOWN)).to_edge(LEFT, buff=1.5)
        pharmacy = VGroup(Square(side_length=0.4), Text("Pharmacy", font_size=20).next_to(Square(), DOWN)).to_edge(RIGHT, buff=1.5)
        
        self.play(FadeIn(patient), FadeIn(pharmacy))

        # --- THE SECRET ---
        secret_box = Rectangle(height=1, width=2.5, color=YELLOW, fill_opacity=0.2).next_to(patient, UP, buff=0.5)
        
        # Split text to avoid spacing issues
        s_line1 = Text("DIAGNOSIS:", color=YELLOW, font_size=16)
        s_line2 = Text("Sensitive Illness", color=YELLOW, font_size=16)
        secret_text = VGroup(s_line1, s_line2).arrange(DOWN).move_to(secret_box)
        secret_group = VGroup(secret_box, secret_text)
        
        self.play(GrowFromCenter(secret_group))
        self.wait(0.5)

        # --- THE REQUIREMENT ---
        r_line1 = Text("Requirement:", font_size=16, color=GREY)
        r_line2 = Text("Eligible for Medicine?", font_size=16, color=GREY)
        req_text = VGroup(r_line1, r_line2).arrange(DOWN).next_to(pharmacy, UP, buff=0.5)
        
        self.play(Write(req_text))
        self.wait(1)

        # --- THE PROOF ---
        proof_box = RoundedRectangle(height=1, width=2, corner_radius=0.2, color=BLUE, fill_opacity=0.5)
        
        p_line1 = Text("ELIGIBLE:", font_size=16, color=WHITE)
        p_line2 = Text("YES", font_size=24, color=WHITE, weight=BOLD)
        proof_text = VGroup(p_line1, p_line2).arrange(DOWN).move_to(proof_box)
        
        proof_group = VGroup(proof_box, proof_text).next_to(patient, RIGHT)

        self.play(FadeIn(proof_group))
        
        # Show secret staying
        self.play(Indicate(secret_group, scale_factor=1.1, color=YELLOW))
        
        # Move proof
        self.play(proof_group.animate.next_to(pharmacy, LEFT), run_time=2)
        
        # Success
        check = Text("Dispense Meds", color=GREEN, font_size=20).next_to(proof_group, DOWN)
        self.play(Write(check))
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))

    def part_3_core_value(self):
        title = Text("Why This Matters", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # --- VISUAL: BOX -> CHECKMARK ---
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

        # --- KEY TEXT ---
        main_point = Text("Prove you know the secret...", font_size=32).shift(DOWN * 1.5)
        sub_point = Text("...without ever revealing it.", font_size=32, color=BLUE).next_to(main_point, DOWN)
        
        self.play(Write(main_point))
        self.play(Write(sub_point))
        self.wait(2)

        # --- FINAL TAG ---
        final_tag = Text('"Verify, don\'t trust."', font_size=48, color=YELLOW).to_edge(DOWN, buff=0.5)
        
        self.play(
            FadeOut(main_point), 
            FadeOut(sub_point),
            FadeIn(final_tag)
        )
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))
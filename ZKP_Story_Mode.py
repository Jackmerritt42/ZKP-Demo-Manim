from manim import *

class ZKP_Story_Mode(Scene):
    def construct(self):
        self.part_1_the_hack()
        self.part_2_medical_example()
        self.part_3_conclusion()

    def part_1_the_hack(self):
        # --- SETUP ---
        title = Text("Part 1: The Problem with Sending Data", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        # Actors
        alice = Text("Alice\n(Prover)", color=GREEN, font_size=24).shift(LEFT * 4)
        bob = Text("Server\n(Verifier)", color=BLUE, font_size=24).shift(RIGHT * 4)
        self.play(Write(alice), Write(bob))

        # --- SCENARIO A: THE HACK ---
        # 1. The Secret
        secret_box = Square(side_length=1, color=YELLOW, fill_opacity=0.5).next_to(alice, DOWN)
        secret_label = Text("Password", font_size=16).move_to(secret_box)
        secret_group = VGroup(secret_box, secret_label)
        
        self.play(GrowFromCenter(secret_group))
        
        # Narration
        narrative_1 = Text("Standard Login: Alice sends her password.", font_size=24).next_to(title, DOWN)
        self.play(Write(narrative_1))
        self.wait(1)

        # 2. The Interception
        # Hacker appears mid-transfer
        eve = Text("Hacker", color=RED, font_size=24).shift(UP * 0.5)
        
        self.play(secret_group.animate.move_to(ORIGIN), run_time=1.5)
        self.play(FadeIn(eve))
        
        # Hacker steals it
        self.play(secret_group.animate.next_to(eve, DOWN), run_time=0.5)
        self.play(secret_group.animate.set_color(RED))
        
        alert = Text("DATA COMPROMISED", color=RED, font_size=36, weight=BOLD).move_to(DOWN*2)
        self.play(Write(alert))
        self.wait(2)

        # Reset for Scene B
        self.play(
            FadeOut(secret_group), FadeOut(eve), FadeOut(alert), FadeOut(narrative_1),
            alice.animate.set_color(WHITE), bob.animate.set_color(WHITE)
        )

        # --- SCENARIO B: THE ZKP SOLUTION ---
        narrative_2 = Text("ZKP Solution: Alice sends a Proof, not the Password.", font_size=24).next_to(title, DOWN)
        self.play(Write(narrative_2))
        
        # Re-create secret with Alice
        secret_group.move_to(alice.get_center() + DOWN*1.5).set_color(YELLOW)
        self.play(FadeIn(secret_group))

        # Generate Proof
        proof_doc = RoundedRectangle(height=0.8, width=0.6, corner_radius=0.1, color=BLUE, fill_opacity=0.2).next_to(secret_group, RIGHT)
        proof_lbl = Text("Proof", font_size=12).move_to(proof_doc)
        proof_group = VGroup(proof_doc, proof_lbl)

        self.play(FadeIn(proof_group))
        self.wait(0.5)

        # Transfer Proof
        self.play(proof_group.animate.move_to(ORIGIN), run_time=1.5)
        
        # Hacker appears again
        self.play(FadeIn(eve))
        self.play(proof_group.animate.next_to(eve, DOWN))
        
        # Hacker confusion
        q_marks = Text("???", color=RED).next_to(proof_group, RIGHT)
        useless_text = Text("Useless to Hacker", color=GREY, font_size=20).next_to(proof_group, DOWN)
        
        self.play(Write(q_marks), Write(useless_text))
        self.wait(1)
        
        # Move to Bob anyway
        self.play(
            FadeOut(q_marks), FadeOut(useless_text),
            proof_group.animate.move_to(bob.get_center() + DOWN*1.5)
        )
        
        # Verification
        check = Text("ACCESS GRANTED", color=GREEN, font_size=24).next_to(proof_group, DOWN)
        self.play(Write(check))
        self.wait(2)
        
        self.play(FadeOut(Group(*self.mobjects)))

    def part_2_medical_example(self):
        title = Text("Part 2: Real World Application", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # Setup Patient
        patient = Text("Patient", font_size=24).to_edge(LEFT).shift(RIGHT)
        patient_icon = Circle(color=WHITE, fill_opacity=0.2).next_to(patient, UP)
        self.play(FadeIn(patient), FadeIn(patient_icon))

        # The Secret (The specific disease)
        narrative = Text("Problem: Proving eligibility without revealing the illness.", font_size=24).next_to(title, DOWN)
        self.play(Write(narrative))

        secret_card = Rectangle(height=2, width=3, color=YELLOW, fill_opacity=0.2).next_to(patient, DOWN, buff=1)
        secret_text = Text("DIAGNOSIS:\nRare Disease X", color=YELLOW, font_size=20).move_to(secret_card)
        secret_group = VGroup(secret_card, secret_text)
        
        self.play(Create(secret_card), Write(secret_text))
        self.wait(1)

        # The Pharmacy / Verifier
        pharmacy = Text("Pharmacy", font_size=24).to_edge(RIGHT).shift(LEFT)
        pharm_icon = Square(color=GREEN, fill_opacity=0.2).next_to(pharmacy, UP)
        
        # The Requirement List
        req_box = Rectangle(height=2.5, width=4, color=WHITE).next_to(pharmacy, DOWN, buff=0.5)
        req_title = Text("Approved for Medicine:", font_size=16).move_to(req_box.get_top() + DOWN*0.3)
        req_list = Text("- Disease A\n- Disease B\n- Rare Disease X", font_size=16, color=GREY).next_to(req_title, DOWN)
        req_group = VGroup(pharmacy, pharm_icon, req_box, req_title, req_list)
        
        self.play(FadeIn(req_group))
        self.wait(2)

        # The logic
        step1 = Text("1. Patient generates a ZKP", font_size=20, color=BLUE).shift(UP*1)
        self.play(ReplacementTransform(narrative, step1))

        # Visualizing the math matching
        # Highlight match
        match_line = req_list[17:] # Rough index for 'Rare Disease X'
        self.play(secret_text.animate.set_color(GREEN), match_line.animate.set_color(GREEN))
        
        # The Zero Knowledge Mask
        step2 = Text("2. The Proof hides the specific match", font_size=20, color=BLUE).move_to(step1)
        self.play(ReplacementTransform(step1, step2))

        # Masking the diagnosis
        mask = Rectangle(height=2.1, width=3.1, color=BLUE, fill_opacity=1).move_to(secret_card)
        mask_text = Text("Valid Diagnosis", color=WHITE, font_size=24).move_to(mask)
        zkp_obj = VGroup(mask, mask_text)

        self.play(FadeIn(zkp_obj))
        self.wait(1)

        # Send to pharmacy
        self.play(zkp_obj.animate.move_to(req_box.get_center()))
        
        final_res = Text("ELIGIBLE: YES", color=GREEN, font_size=32, weight=BOLD).next_to(req_box, DOWN)
        self.play(Write(final_res))
        
        summary = Text("Pharmacy gives medicine,\nbut never learns WHICH disease.", font_size=20).move_to(DOWN*3)
        self.play(Write(summary))
        self.wait(3)
        
        self.play(FadeOut(Group(*self.mobjects)))

    def part_3_conclusion(self):
        title = Text("Why This Changes Everything", font_size=40).to_edge(UP)
        self.play(Write(title))

        # 1. Privacy
        p1_box = Rectangle(height=1.5, width=4, color=BLUE).shift(UP*0.5)
        p1_title = Text("Selective Disclosure", font_size=24).move_to(p1_box.get_top() + DOWN*0.4)
        p1_desc = Text("Prove facts without\nrevealing data.", font_size=20, color=GREY).next_to(p1_title, DOWN, buff=0.1)
        p1_group = VGroup(p1_box, p1_title, p1_desc)

        self.play(Create(p1_group))
        self.wait(1)

        # 2. Security
        p2_box = Rectangle(height=1.5, width=4, color=GREEN).next_to(p1_box, DOWN, buff=0.5)
        p2_title = Text("Hack-Proof Auth", font_size=24).move_to(p2_box.get_top() + DOWN*0.4)
        p2_desc = Text("Passwords never leave\nyour device.", font_size=20, color=GREY).next_to(p2_title, DOWN, buff=0.1)
        p2_group = VGroup(p2_box, p2_title, p2_desc)

        self.play(Create(p2_group))
        self.wait(2)

        # Final Statement
        final_text = Text("The Future of Digital Trust", font_size=36, color=YELLOW).to_edge(DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))
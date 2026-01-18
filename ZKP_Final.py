from manim import *
import numpy as np
import random

class ZKP_Final(Scene):
    def construct(self):
        # ==========================================
        # SECTION 1: ZKP PRESENTATION (The "Why")
        # ==========================================
        self.part_0_intro()
        self.part_1_id_card()
        self.part_2_medical_simple()
        self.part_3_core_value()

        # ==========================================
        # SECTION 2: SCENE DEMOS (The "How")
        # ==========================================
        # Note: There is a second definition section here from Scene.py. 
        # You may wish to remove 'self.intro_definition()' if it feels redundant,
        # but I have included it to ensure "all content" is present as requested.
        self.intro_definition() 
        
        self.intro_sequence_1()
        self.scene_colorblind_loop()
        
        self.intro_sequence_waldo()
        self.scene_wheres_waldo()
        
        self.intro_sequence_alibaba()
        self.scene_alibaba_final()
        
        self.outro_contact_slide()

    # ==========================================
    # METHODS FROM ZKP_PRESENTATION.PY
    # ==========================================

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

    # ==========================================
    # METHODS FROM SCENE.PY
    # ==========================================

    # --- PART 0: WHAT IS A ZKP? ---
    def intro_definition(self):
        title = Title("What is a Zero-Knowledge Proof?").to_edge(UP)
        
        t1 = Text("Peggy wants to prove to Victor that she knows a secret,", font_size=28).shift(UP*1.5)
        t2 = Text("without revealing the secret itself.", font_size=28, color=YELLOW).next_to(t1, DOWN)
        
        context_t = Text("Example: Victor is Colorblind. Peggy is not.", font_size=24, color=BLUE).next_to(t2, DOWN, buff=0.5)
        goal_t = Text("Goal: Prove the balls are different colors without saying which is Red.", font_size=24).next_to(context_t, DOWN)
        
        definition_group = VGroup(t1, t2, context_t, goal_t)
        
        self.play(Write(title))
        self.play(FadeIn(definition_group))
        self.wait(3)
        
        self.play(definition_group.animate.scale(0.7).to_edge(UP).shift(DOWN*1.0))
        
        p1 = Text("1. Completeness", color=GREEN, font_size=28).shift(LEFT*4 + DOWN*0.5)
        p1_desc = Text("If true, honest Victor\nis convinced.", font_size=20, color=GRAY).next_to(p1, DOWN)
        
        p2 = Text("2. Soundness", color=RED, font_size=28).shift(RIGHT*4 + DOWN*0.5)
        p2_desc = Text("If false, cheating Peggy\ncannot fool him.", font_size=20, color=GRAY).next_to(p2, DOWN)
        
        p3 = Text("3. Zero-Knowledge", color=BLUE, font_size=28).move_to(DOWN*2.5)
        p3_desc = Text("Victor learns nothing else.", font_size=20, color=GRAY).next_to(p3, DOWN)
        
        self.play(Write(p1), Write(p1_desc))
        self.play(Write(p2), Write(p2_desc))
        self.play(Write(p3), Write(p3_desc))
        
        self.wait(4)
        self.clear()

    # --- PART 1: COLORBLIND ---
    def intro_sequence_1(self):
        self.clear()
        title = Title("Part 1: The Intuition").to_edge(UP)
        
        q1 = Text("The Core Problem:", color=BLUE, font_size=36).shift(UP)
        q2 = Text("How can I prove that I know something...", font_size=28).next_to(q1, DOWN)
        q3 = Text("(e.g., the difference between colors)", font_size=24, color=YELLOW).next_to(q2, DOWN)
        q4 = Text("...without disclosing the information itself?", font_size=28).next_to(q3, DOWN)
        
        self.play(Write(title), FadeIn(q1))
        self.play(Write(q2))
        self.play(Write(q3))
        self.play(Write(q4))
        self.wait(4)
        self.clear()

    def scene_colorblind_loop(self):
        title = Title("Part 1: Interactive Proof").to_edge(UP)
        self.add(title)

        cert_text = Text("Certainty:", font_size=24).to_corner(DL)
        cert_num = DecimalNumber(0, unit="\%", num_decimal_places=1, font_size=24, color=YELLOW).next_to(cert_text, RIGHT)
        self.play(Write(cert_text), Write(cert_num))

        ball_left = Dot(radius=0.6, color=RED).move_to(LEFT * 1.5 + DOWN * 0.2)
        ball_right = Dot(radius=0.6, color=GREEN).move_to(RIGHT * 1.5 + DOWN * 0.2)
        self.play(FadeIn(ball_left, ball_right))

        certainties = [50.0, 75.0, 87.5]
        
        for i in range(3):
            n = i + 1
            round_lbl = Text(f"Round {n}", font_size=24, color=YELLOW).to_corner(UL)
            self.play(FadeIn(round_lbl))
            
            self.play(
                ball_left.animate.set_color(GRAY),
                ball_right.animate.set_color(GRAY),
                run_time=0.3
            )
            
            blindfold = Text("[Peggy Looks Away]", font_size=20, color=RED).to_corner(UR)
            self.play(FadeIn(blindfold))
            
            do_switch = (i % 2 == 0) 
            decision_text = "SWITCHING" if do_switch else "NOT SWITCHING"
            secret_lbl = Text(f"[Victor secretly chooses: {decision_text}]", font_size=24, color=GRAY_B).to_edge(DOWN).shift(UP * 1.5)
            self.play(FadeIn(secret_lbl))

            self.play(Rotate(VGroup(ball_left, ball_right), angle=PI, about_point=DOWN*0.2), run_time=0.5)
            if do_switch:
                self.play(Swap(ball_left, ball_right), run_time=0.3)
            else:
                self.wait(0.3)
            self.play(Rotate(VGroup(ball_left, ball_right), angle=PI, about_point=DOWN*0.2), run_time=0.5)
            
            self.play(FadeOut(secret_lbl), FadeOut(blindfold))
            
            left_col = GREEN if do_switch else RED
            right_col = RED if do_switch else GREEN
            
            peggy_msg = "Peggy: 'Switched!'" if do_switch else "Peggy: 'Stayed!'"
            msg_obj = Text(peggy_msg, color=PINK, font_size=24).next_to(ball_left, UP, buff=0.8)
            
            self.play(
                ball_left.animate.set_color(left_col),
                ball_right.animate.set_color(right_col),
                Write(msg_obj)
            )
            
            self.play(cert_num.animate.set_value(certainties[i]), run_time=0.5)
            self.wait(1)
            
            if do_switch:
                 ball_left.set_color(RED)
                 ball_right.set_color(GREEN)
            
            self.play(FadeOut(round_lbl), FadeOut(msg_obj))

        final_stat = Text("Repeat 10 times -> Chance of luck is < 0.1%", font_size=24, color=YELLOW).to_edge(DOWN)
        self.play(Write(final_stat))
        self.wait(3)
        self.clear()

    # --- PART 2: WHERE'S WALDO ---
    def intro_sequence_waldo(self):
        self.clear()
        title = Title("Part 2: Where's Waldo?").to_edge(UP)
        
        q1 = Text("The Problem:", color=BLUE, font_size=36).shift(UP)
        q2 = Text("How do you prove you found Waldo...", font_size=28).next_to(q1, DOWN)
        q3 = Text("...without showing WHERE he is on the map?", font_size=28, color=YELLOW).next_to(q2, DOWN)
        
        self.play(Write(title), FadeIn(q1))
        self.play(Write(q2))
        self.play(Write(q3))
        self.wait(4)
        self.clear()

    def scene_wheres_waldo(self):
        title = Title("Part 2: Zero-Knowledge Map").to_edge(UP)
        self.add(title)

        # 1. THE MAP
        map_group = VGroup()
        map_bg = Rectangle(height=6, width=10, color=BLUE_E, fill_opacity=0.3)
        map_group.add(map_bg)
        
        waldo_pos = np.array([2.5, 1.5, 0])
        
        for _ in range(80):
            pos = [random.uniform(-4.5, 4.5), random.uniform(-2.5, 2.5), 0]
            if np.linalg.norm(np.array(pos) - waldo_pos) > 0.8:
                d = Dot(color=random.choice([BLUE, YELLOW, GREEN, PINK, GRAY]), radius=0.06)
                d.move_to(pos)
                map_group.add(d)
            
        waldo = Dot(color=RED, radius=0.15).move_to(waldo_pos)
        waldo_ring = Circle(color=WHITE, radius=0.15).move_to(waldo_pos)
        map_group.add(waldo, waldo_ring)
        
        # Shift entire map DOWN further to avoid title clash
        full_map = VGroup(map_group).shift(DOWN * 1.0)

        # Just fade in the map (no text)
        self.play(FadeIn(full_map))
        self.wait(2)

        # 2. THE GIANT SHIELD (Appears BEFORE text)
        hole_center = DOWN * 1.0
        hole_size = 0.4 

        # HUGE rectangles
        r_top = Rectangle(width=25, height=12, color=BLACK, fill_opacity=1).move_to(hole_center + UP * (6 + hole_size))
        r_bot = Rectangle(width=25, height=12, color=BLACK, fill_opacity=1).move_to(hole_center + DOWN * (6 + hole_size))
        r_left = Rectangle(width=12, height=25, color=BLACK, fill_opacity=1).move_to(hole_center + LEFT * (6 + hole_size))
        r_right = Rectangle(width=12, height=25, color=BLACK, fill_opacity=1).move_to(hole_center + RIGHT * (6 + hole_size))
        
        hole_ring = Circle(radius=hole_size, color=WHITE).move_to(hole_center)
        shield_visual = VGroup(r_top, r_bot, r_left, r_right, hole_ring)
        
        # Fade in Shield first
        self.play(FadeIn(shield_visual))
        
        # 3. SOLUTION TEXT (On top of shield)
        t2 = Text("The Solution: Use a giant shield with a tiny hole.", font_size=24, color=YELLOW).to_edge(UP).shift(DOWN*1.5)
        self.play(Write(t2))
        
        # 4. PROVING IT
        t3 = Text("Move the Map behind the shield...", font_size=24).next_to(t2, DOWN)
        self.play(Write(t3))
        
        # Move map behind shield
        current_waldo = waldo.get_center()
        shift_vector = hole_center - current_waldo
        
        # Re-layering
        self.remove(full_map)
        self.add(full_map)
        self.add(shield_visual)
        self.add(t2, t3)
        
        self.play(full_map.animate.shift(shift_vector), run_time=3.0)
        
        arrow = Arrow(start=RIGHT*2 + DOWN*1.0, end=hole_center + RIGHT*0.2, color=RED)
        lbl = Text("There he is!", font_size=24, color=RED).next_to(arrow, RIGHT)
        self.play(GrowArrow(arrow), Write(lbl))
        
        t4 = Text("You see him, but have ZERO context of where he is.", font_size=24, color=GREEN).to_edge(DOWN)
        self.play(Write(t4))
        self.wait(3)
        self.clear()

    # --- PART 3: ALI BABA ---
    def intro_sequence_alibaba(self):
        title = Title("Part 3: The Classic Analogy").to_edge(UP)
        q1 = Text("Ali Baba's Cave", color=BLUE, font_size=36).move_to(UP)
        q2 = Text("A physical demonstration of Zero Knowledge.", font_size=24).next_to(q1, DOWN)
        
        q3 = Text("This shows I can prove I possess a secret key", font_size=24, color=YELLOW).next_to(q2, DOWN, buff=0.5)
        q4 = Text("without ever showing myself using the key.", font_size=24, color=YELLOW).next_to(q3, DOWN)
        
        # Sequential Animation
        self.play(Write(title))
        self.play(FadeIn(q1))
        self.wait(0.5)
        self.play(Write(q2))
        self.wait(1)
        self.play(Write(q3))
        self.play(Write(q4))
        self.wait(3)
        self.clear()

    def scene_alibaba_final(self):
        title = Title("Part 3: Ali Baba's Cave").to_edge(UP)
        self.add(title)

        cave_center = DOWN * 0.5
        cave = Annulus(inner_radius=1.5, outer_radius=2.5, color=GRAY).rotate(PI).move_to(cave_center)
        mask = Rectangle(width=2, height=2, color=BLACK, fill_opacity=1).move_to(cave_center + DOWN * 2)
        cave_visual = Difference(cave, mask, color=GRAY, fill_opacity=0.5)
        
        door = Line(cave_center + UP*1.5, cave_center + UP*2.5, color=ORANGE, stroke_width=8)
        
        lbl_door = Text("Magic Door", font_size=16, color=ORANGE).next_to(door, UP, buff=0.1)

        lbl_A = Text("Path A", font_size=20).move_to(cave_center + LEFT * 3.5)
        lbl_B = Text("Path B", font_size=20).move_to(cave_center + RIGHT * 3.5)
        
        self.play(FadeIn(cave_visual), Create(door), Write(lbl_door), Write(lbl_A), Write(lbl_B))

        peggy = Dot(color=PINK, radius=0.2).move_to(cave_center + DOWN * 2)
        victor = Dot(color=BLUE, radius=0.2).move_to(cave_center + DOWN * 2.5)
        
        # 1. Enters
        self.play(peggy.animate.move_to(cave_center + LEFT * 2))
        self.play(peggy.animate.set_opacity(0.4).move_to(cave_center + UP * 2 + LEFT * 0.5))
        
        # 2. Challenge
        self.play(victor.animate.move_to(cave_center + DOWN * 2))
        
        cmd = Text("Come out Path B!", color=BLUE, font_size=24).next_to(victor, DOWN)
        self.play(Write(cmd))
        
        # 3. Cross
        self.play(peggy.animate.move_to(cave_center + UP * 2 + RIGHT * 0.5), run_time=1.2)
        self.play(Indicate(door, color=YELLOW, scale_factor=1.5))
        
        # 4. Exit
        self.play(peggy.animate.move_to(cave_center + RIGHT * 2))
        self.play(peggy.animate.set_opacity(1).move_to(cave_center + DOWN * 1.8))
        
        valid = Text("Verified!", color=GREEN).to_corner(DR)
        self.play(Write(valid))
        self.wait(3)
        self.clear()

    # --- OUTRO: CONTACT SLIDE ---
    def outro_contact_slide(self):
        name = Text("Jack Merritt", font_size=48, color=BLUE)
        
        info_group = VGroup(
            Text("LinkedIn: linkedin.com/in/jack-merritt42", font_size=24),
            Text("Email: jackmerritt42@proton.me", font_size=24),
            Text("GitHub: https://github.com/Jackmerritt42/ZKP-Demo-Manim", font_size=24)
        ).arrange(DOWN, center=True, buff=0.5).next_to(name, DOWN, buff=1.0)
        
        self.play(Write(name))
        self.play(FadeIn(info_group, shift=UP))
        self.wait(5)
from manim import *

class ZKPIntro(Scene):
    def construct(self):
        # --- SECTION 1: THE TITLE ---
        title = Text("Zero-Knowledge Proofs", font_size=48, color=BLUE)
        subtitle = Text("Proving a secret without revealing it", font_size=24, color=GREY).next_to(title, DOWN)
        
        self.play(Write(title), FadeIn(subtitle))
        self.wait(2)
        
        # Move title up to clear stage
        self.play(FadeOut(subtitle), title.animate.to_edge(UP))

        # --- SECTION 2: THE ACTORS ---
        # Alice (Prover) on Left, Bob (Verifier) on Right
        prover = Text("Prover (Alice)", color=GREEN, font_size=36).to_edge(LEFT).shift(RIGHT)
        verifier = Text("Verifier (Bob)", color=RED, font_size=36).to_edge(RIGHT).shift(LEFT)
        
        self.play(Write(prover), Write(verifier))

        # --- SECTION 3: THE SECRET ---
        # A glowing yellow box representing the secret data
        secret_box = Square(color=YELLOW, fill_opacity=0.5, side_length=1.5).next_to(prover, DOWN)
        secret_text = Text("Secret", font_size=24, color=WHITE).move_to(secret_box)
        secret_group = VGroup(secret_box, secret_text)

        self.play(GrowFromCenter(secret_group))
        self.wait(1)

        # --- SECTION 4: THE PROBLEM ---
        # Alice tries to send the secret to Bob -> STOPPED
        self.play(secret_group.animate.move_to(ORIGIN), run_time=1)
        
        stop_sign = Cross(stroke_width=10, color=RED).scale(0.8).move_to(ORIGIN)
        warning_text = Text("UNSECURE", color=RED, font_size=24).next_to(stop_sign, DOWN)
        
        self.play(Create(stop_sign), Write(warning_text))
        self.wait(1)
        
        # Return secret to Alice
        self.play(FadeOut(stop_sign), FadeOut(warning_text), secret_group.animate.next_to(prover, DOWN))

        # --- SECTION 5: THE SOLUTION ---
        # Alice generates a specific "Proof" object (distinct from secret)
        proof_doc = RoundedRectangle(height=1.2, width=1, corner_radius=0.2, color=BLUE, fill_opacity=0.2).next_to(secret_group, RIGHT)
        proof_text = Text("Proof", font_size=20).move_to(proof_doc)
        proof_obj = VGroup(proof_doc, proof_text)

        self.play(FadeIn(proof_obj))
        self.wait(0.5)
        
        # The Proof travels to Bob
        self.play(proof_obj.animate.move_to(verifier.get_center() + DOWN*1.5))
        
        # Bob verifies it
        check = Text("✔ Valid", color=GREEN, font_size=36).next_to(proof_obj, DOWN)
        self.play(Write(check))
        self.wait(2)
        
        self.play(FadeOut(Group(*self.mobjects)))


class ZKPBarExample(Scene):
    def construct(self):
        # --- SECTION 1: THE ID CARD ---
        title = Text("Why do we need this?", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Create a visual ID card
        id_card = RoundedRectangle(corner_radius=0.3, height=4.5, width=7, fill_color=GREY_E, fill_opacity=1, stroke_color=WHITE)
        photo = Square(side_length=1.8, color=WHITE, fill_opacity=0.5).move_to(id_card.get_left() + RIGHT * 1.5)
        photo_text = Text("PHOTO", font_size=16).move_to(photo)
        
        # Data fields
        name = Text("Name: John Doe", font_size=28).next_to(photo, RIGHT, buff=0.5).shift(UP*0.8)
        addr = Text("Address: 123 Main St", font_size=28).next_to(name, DOWN, align_edge=LEFT)
        dob = Text("DOB: 01/01/1990", font_size=28).next_to(addr, DOWN, align_edge=LEFT)
        id_num = Text("ID#: A123456789", font_size=28).next_to(dob, DOWN, align_edge=LEFT)
        
        full_id = VGroup(id_card, photo, photo_text, name, addr, dob, id_num).move_to(ORIGIN)

        self.play(Create(id_card), FadeIn(photo), FadeIn(photo_text))
        self.play(Write(name), Write(addr), Write(dob), Write(id_num))
        self.wait(1)

        # --- SECTION 2: THE LEAK ---
        # Highlight the unnecessary data
        danger_rect = Rectangle(width=4.5, height=2.5, color=RED).move_to(full_id.get_right() + LEFT*1.8)
        warning = Text("Unnecessary Data Leak!", color=RED, font_size=36).next_to(id_card, DOWN)
        
        self.play(Create(danger_rect), Write(warning))
        self.wait(2)
        self.play(FadeOut(danger_rect), FadeOut(warning))

        # --- SECTION 3: THE ZKP MASK ---
        # A mask slides over, hiding everything but the validity
        mask = RoundedRectangle(corner_radius=0.3, height=4.6, width=7.1, fill_color=BLACK, fill_opacity=0.9, stroke_color=GREEN, stroke_width=4).move_to(id_card)
        zkp_label = Text("Zero Knowledge Proof", color=GREEN, font_size=36).next_to(mask, UP)
        
        result_text = Text("AGE > 21: TRUE", color=GREEN, font_size=48).move_to(mask)

        self.play(FadeIn(mask), Write(zkp_label))
        self.play(Write(result_text))
        self.wait(3)


class ZKPRealWorld(Scene):
    def construct(self):
        title = Text("Real World Applications", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Position 3 main categories
        # 1. Crypto
        crypto_group = VGroup()
        c_icon = Circle(radius=0.8, color=ORANGE, fill_opacity=0.2)
        c_text = Text("Privacy Coins", font_size=24).next_to(c_icon, DOWN)
        c_sub = Text("Zcash / Monero", font_size=18, color=GREY).next_to(c_text, DOWN)
        crypto_group.add(c_icon, c_text, c_sub).shift(LEFT * 4)
        
        # 2. Identity
        id_group = VGroup()
        i_icon = Square(side_length=1.6, color=BLUE, fill_opacity=0.2)
        i_text = Text("Secure Login", font_size=24).next_to(i_icon, DOWN)
        i_sub = Text("No Passwords Sent", font_size=18, color=GREY).next_to(i_text, DOWN)
        id_group.add(i_icon, i_text, i_sub)

        # 3. Scaling/Voting
        vote_group = VGroup()
        v_icon = Triangle(color=GREEN, fill_opacity=0.2).scale(1.2)
        v_text = Text("Voting & Scaling", font_size=24).next_to(v_icon, DOWN).shift(DOWN*0.1) # shift slightly for triangle alignment
        v_sub = Text("Verify without revealing", font_size=18, color=GREY).next_to(v_text, DOWN)
        vote_group.add(v_icon, v_text, v_sub).shift(RIGHT * 4)

        # Animate them appearing one by one with a small "pop" effect
        self.play(DrawBorderThenFill(c_icon), Write(c_text))
        self.play(FadeIn(c_sub))
        self.wait(0.5)

        self.play(DrawBorderThenFill(i_icon), Write(i_text))
        self.play(FadeIn(i_sub))
        self.wait(0.5)

        self.play(DrawBorderThenFill(v_icon), Write(v_text))
        self.play(FadeIn(v_sub))
        
        self.wait(3)
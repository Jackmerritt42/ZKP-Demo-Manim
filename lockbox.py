from manim import *

class FullPresentation(Scene):
    def construct(self):
        # ==========================================
        # PART 1: THE MATH INTRO
        # ==========================================
        
        # --- 1. THE OPENING QUESTION ---
        question = Text("So how does our current model work?", font_size=36)
        self.play(Write(question))
        self.wait(1.5)
        self.play(question.animate.to_edge(UP))

        # --- 2. THE INGREDIENTS (Private) ---
        p_q_group = VGroup(
            MathTex("p", font_size=80, color=RED),
            MathTex("\\times", font_size=60),
            MathTex("q", font_size=80, color=RED)
        ).arrange(RIGHT, buff=0.5).shift(LEFT * 3)
        
        label_private = Text("Private Primes", font_size=20, color=RED).next_to(p_q_group, DOWN)
        
        self.play(FadeIn(p_q_group), FadeIn(label_private))
        self.wait(1)

        # --- 3. THE PRODUCT (Public) ---
        n_val = MathTex("N", font_size=80, color=GREEN).shift(RIGHT * 3)
        label_public = Text("Public Key", font_size=20, color=GREEN).next_to(n_val, DOWN)

        self.play(FadeIn(n_val), FadeIn(label_public))
        self.wait(0.5)

        # --- 4. THE ARROWS ---
        arrow_easy = Arrow(start=p_q_group.get_right() + UP*0.5, end=n_val.get_left() + UP*0.5, color=YELLOW, buff=0.2)
        text_easy = Text("Multiply (Easy)", font_size=20, color=YELLOW).next_to(arrow_easy, UP)
        self.play(GrowArrow(arrow_easy), Write(text_easy))
        
        arrow_hard = Arrow(start=n_val.get_left() + DOWN*0.5, end=p_q_group.get_right() + DOWN*0.5, color=RED, buff=0.2)
        text_hard = Text("Factor (Impossible*)", font_size=20, color=RED).next_to(arrow_hard, DOWN)
        self.play(GrowArrow(arrow_hard), Write(text_hard))
        self.wait(2)

        # --- TRANSITION 1: CLEANUP ---
        math_group = VGroup(p_q_group, label_private, n_val, label_public, arrow_easy, text_easy, arrow_hard, text_hard, question)
        self.play(FadeOut(math_group))
        self.wait(0.5)


        # ==========================================
        # PART 2: THE LOCKBOX ANALOGY
        # ==========================================
        
        # --- SETUP ---
        title_lock = Text("Public Key Encryption: The Lockbox", font_size=36).to_edge(UP)
        self.play(Write(title_lock))

        alice = Text("Alice", color=BLUE).to_edge(LEFT, buff=1.0)
        bob = Text("Bob", color=GREEN).to_edge(RIGHT, buff=1.0)
        self.play(FadeIn(alice), FadeIn(bob))

        # --- ASSETS ---
        message = VGroup(
            Rectangle(height=0.6, width=0.8, fill_color=WHITE, fill_opacity=1, stroke_color=GREY),
            Text("DATA", font_size=14, color=BLACK)
        ).next_to(alice, RIGHT, buff=1.0)

        box = Square(side_length=1.5, color=GREY, fill_opacity=0.1)

        # Public Key
        lock_body = RoundedRectangle(height=0.5, width=0.6, corner_radius=0.1, fill_color=GREEN, fill_opacity=1)
        shackle_open = Arc(radius=0.2, start_angle=0, angle=PI, color=GREY, stroke_width=6).next_to(lock_body, UP, buff=-0.1).shift(RIGHT*0.15)
        public_key = VGroup(lock_body, shackle_open)
        pk_label = Text("Public Key", font_size=16, color=GREEN).next_to(public_key, DOWN)
        public_key_group = VGroup(public_key, pk_label).move_to(UP*1.5)

        # Private Key
        key_handle = Circle(radius=0.15, color=RED, fill_opacity=1)
        key_shaft = Rectangle(height=0.1, width=0.4, color=RED, fill_opacity=1).next_to(key_handle, RIGHT, buff=-0.05)
        key_teeth = Rectangle(height=0.15, width=0.1, color=RED, fill_opacity=1).next_to(key_shaft, RIGHT, buff=-0.05).shift(DOWN*0.05)
        private_key = VGroup(key_handle, key_shaft, key_teeth)
        prk_label = Text("Private Key", font_size=16, color=RED).next_to(private_key, DOWN)
        private_key_group = VGroup(private_key, prk_label).next_to(bob, DOWN, buff=0.5)

        # --- ANIMATION ---
        self.play(FadeIn(public_key_group), FadeIn(private_key_group))
        self.wait(0.5)

        # Send Key
        target_pk_pos = message.get_top() + UP * 1.0
        self.play(public_key_group.animate.move_to(target_pk_pos), run_time=1.5)
        self.wait(0.5)

        # Put Message in Box
        box.move_to(message.get_center())
        self.play(FadeIn(message), FadeIn(box))
        self.play(message.animate.scale(0.8), run_time=0.5) 

        # Lock it
        shackle_closed = Arc(radius=0.2, start_angle=0, angle=PI, color=GREY, stroke_width=6).next_to(lock_body, UP, buff=-0.1)
        closed_lock = VGroup(lock_body.copy(), shackle_closed).move_to(box.get_top())

        self.play(public_key.animate.move_to(box.get_top()), FadeOut(pk_label))
        self.play(Transform(public_key, closed_lock), box.animate.set_fill(color=GREEN, opacity=0.3), run_time=0.5)
        
        # Send to Bob
        locked_package = VGroup(box, message, public_key)
        self.play(locked_package.animate.next_to(bob, LEFT, buff=1.0), run_time=2)

        # Unlock
        self.play(private_key.animate.next_to(public_key, RIGHT), run_time=1)
        open_lock_final = VGroup(lock_body.copy(), shackle_open.copy()).move_to(public_key.get_center())
        self.play(Transform(public_key, open_lock_final), box.animate.set_fill(color=GREY, opacity=0.1), run_time=0.5)

        # Reveal
        self.play(message.animate.next_to(box, DOWN), FadeOut(private_key), run_time=1)
        self.wait(2)

        # --- TRANSITION 2: CLEANUP ---
        # We need to fade out everything from Scene 2 before starting Scene 3
        lockbox_objects = VGroup(title_lock, alice, bob, locked_package, message, public_key, private_key_group, open_lock_final)
        self.play(FadeOut(lockbox_objects))
        self.wait(0.5)


        # ==========================================
        # PART 3: THE VOTING BOOTH ANALOGY
        # ==========================================

        # --- SETUP ---
        title_vote = Text("The Voting Booth Analogy", font_size=36).to_edge(UP)
        sub_title_vote = Text("Public action (encrypt), Private action (decrypt)", font_size=24).next_to(title_vote, DOWN)
        self.play(Write(title_vote), Write(sub_title_vote))

        # Box
        box_body = Square(side_length=2, color=WHITE, fill_opacity=0.5, fill_color=GREY)
        slot = Rectangle(height=0.1, width=0.8, color=BLACK, fill_opacity=1).move_to(box_body.get_top())
        ballot_box = VGroup(box_body, slot)
        box_label = Text("Public Ballot Box", font_size=20).next_to(ballot_box, DOWN)
        self.play(FadeIn(ballot_box), Write(box_label))

        # Voters
        voters = VGroup()
        votes = VGroup()
        for i in range(3):
            voter = Circle(radius=0.3, color=BLUE, fill_opacity=0.5).shift(LEFT * 4 + UP * (1.0 - i*1.0))
            voter_label = Text("Public", font_size=12).next_to(voter, DOWN)
            paper = Rectangle(height=0.3, width=0.5, color=WHITE, fill_opacity=1, stroke_color=GREY)
            paper.move_to(voter.get_center())
            voters.add(VGroup(voter, voter_label))
            votes.add(paper)

        self.play(FadeIn(voters), FadeIn(votes))
        self.wait(1)

        # Voting
        for i in range(3):
            self.play(votes[i].animate.move_to(slot.get_center()), run_time=0.6)
            self.play(FadeOut(votes[i], target_position=box_body.get_center()), run_time=0.3)
        self.wait(1)

        # Private Key
        official = Text("Official", color=RED).to_edge(RIGHT, buff=1.5)
        key_final = VGroup(
            Circle(radius=0.15, color=RED, fill_opacity=1),
            Rectangle(height=0.1, width=0.4, color=RED, fill_opacity=1).shift(RIGHT*0.25),
             Text("Private Key", font_size=14, color=RED).shift(DOWN*0.4)
        ).next_to(official, LEFT)
        
        self.play(FadeIn(official), FadeIn(key_final))
        self.wait(1)

        # Unlock
        self.play(key_final.animate.move_to(box_body.get_right()), run_time=1)
        final_papers = VGroup()
        for i in range(3):
            p = Rectangle(height=0.3, width=0.5, color=WHITE, fill_opacity=1, stroke_color=GREY)
            p.move_to(box_body.get_center() + UP*(0.4 - i*0.4))
            final_papers.add(p)

        self.play(box_body.animate.set_fill(opacity=0), FadeIn(final_papers), run_time=1)
        final_text = Text("Only the key holder can see the results.", font_size=24, color=RED).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(3)
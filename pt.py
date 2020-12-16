from manimlib.imports import *

class DashedMarker(DashedLine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_tip(tip_length=0.2, at_start=False)
        self.add_tip(tip_length=0.2, at_start=True)


class First_Proof(Scene):
    CONFIG = {
        "camera_config" : {"background_color" : "#edf2f4"}
    }
    def construct(self):
        asq = Square(side_length=1.8, fill_opacity=0.5, color=BLACK)
        a_side_label = TexMobject("a").set_color(BLACK)
        a_side_marker = DashedMarker(asq.get_corner(DL), asq.get_corner(DR)).next_to(asq, DOWN).set_color(BLACK)
        a_side_label.next_to(a_side_marker, DOWN)

        self.play(
            DrawBorderThenFill(asq)
        )
        self.play(
            GrowFromCenter(a_side_marker),
            Write(a_side_label)
        )

        self.play(
            ApplyMethod(asq.shift, RIGHT*4),
            ApplyMethod(a_side_label.shift, RIGHT*4),
            ApplyMethod(a_side_marker.shift, RIGHT*4)
        )

        bsq = Square(side_length=2.4, fill_opacity=0.5, color=BLACK)
        b_side_label = TexMobject("b").set_color(BLACK)
        b_side_marker = DashedMarker(bsq.get_corner(DL), bsq.get_corner(DR)).next_to(bsq, DOWN).set_color(BLACK)
        b_side_label.next_to(b_side_marker, DOWN)

        self.play(
            DrawBorderThenFill(bsq)
        )
        self.play(
            GrowFromCenter(b_side_marker),
            Write(b_side_label)
        )

        self.wait()

        a_side_marker.add_updater(lambda mob: mob.next_to(asq, DOWN))
        a_side_label.add_updater(lambda mob: mob.next_to(a_side_marker, DOWN))
        self.play(
            ApplyMethod(bsq.shift, DR * 0.8 + RIGHT),
            ApplyMethod(b_side_label.shift, DR*0.8 + RIGHT),
            ApplyMethod(b_side_marker.shift, DR*0.8 + RIGHT)
        )
        self.play(
            ApplyMethod(asq.move_to, bsq.get_corner(DR) + (UR) * asq.get_width()/2.0)  
        )
        a_side_marker.clear_updaters()
        b_side_label.add_updater(lambda mob: mob.next_to(b_side_marker, DOWN))

        a2 = TexMobject("a^2").set_color(BLACK).move_to(asq.get_center())
        b2 = TexMobject("b^2").set_color(BLACK).move_to(bsq.get_center())

        self.wait()
        self.play(
            TransformFromCopy(a_side_label, a2)
        )
        self.play(
            TransformFromCopy(b_side_label, b2)
        )

        self.wait()
        
        area = VGroup(asq, bsq).copy().scale(0.3)

        eqn = TexMobject("a^2", "+", "b^2", "=").set_color(BLACK).to_edge(LEFT)
        area.next_to(eqn, RIGHT)

        self.play(
            ReplacementTransform(VGroup(a2, b2), eqn)
        )
        self.play(
            TransformFromCopy(VGroup(asq, bsq), area)
        )

        la = a_side_marker.get_width()
        lb = b_side_marker.get_width()
        self.wait()
        self.play(
            ApplyMethod(b_side_marker.shift, RIGHT*la),
            ApplyMethod(a_side_marker.shift, LEFT*lb, path_arc=-PI/4)
        )

        t1 = Polygon(asq.get_corner(UR), asq.get_corner(DR), asq.get_corner(DR) + LEFT * lb, color="#d90429")
        t2 = Polygon(bsq.get_corner(UL), bsq.get_corner(DL), bsq.get_corner(DL) + RIGHT * la, color="#d90429")

        self.wait()
        self.play(
            DrawBorderThenFill(t1),
            DrawBorderThenFill(t2)
        )

        t1_marker = DashedMarker(asq.get_corner(UR) + UL*0.3, asq.get_corner(DR) + LEFT * lb + UL*0.3).set_color("#8d0801")
        t1_label = TexMobject("c").move_to(t1_marker.get_center() + UL*0.3).set_color("#8d0801")

        t2_marker = DashedMarker(bsq.get_corner(UL) + UR*0.3, bsq.get_corner(DL) + RIGHT * la + UR*0.3).set_color("#8d0801")
        t2_label = TexMobject("c").move_to(t2_marker.get_center() + UR*0.3).set_color("#8d0801")

        self.wait()
        self.play(
            GrowFromCenter(t1_marker),
            Write(t1_label)
        )
        self.wait(0.5)
        self.play(
            TransformFromCopy(t1_marker, t2_marker),
            TransformFromCopy(t1_label, t2_label)
        )

        def rot1(mob, alpha):
           mob.restore()
           mob.rotate(3 * PI*alpha*0.5, about_point=asq.get_corner(UR))
           mob.set_fill(color=BLACK, opacity=0.5*alpha)
        def rot2(mob, alpha):
           mob.restore()
           mob.rotate(-3 * PI*alpha*0.5, about_point=bsq.get_corner(UL))
           mob.set_fill(color=BLACK, opacity=0.5*alpha)

        t1.save_state()
        t2.save_state()
        t1_c = t1.copy().set_stroke(color="#edf2f4").set_fill(color="#edf2f4", opacity=1.0)
        t2_c = t2.copy().set_stroke(color="#edf2f4").set_fill(color="#edf2f4", opacity=1.0)

        self.wait()
        self.play(
            *[FadeOut(x) for x in [t1_marker, t1_label, t2_marker, t2_label]]
        )
        self.wait()
        self.play(
            UpdateFromAlphaFunc(t1, rot1),
            #UpdateFromAlphaFunc(t2, rot2),
            FadeIn(t1_c),
            #FadeIn(t2_c)
        )
        self.wait(0.5)

        self.play(
            #UpdateFromAlphaFunc(t1, rot1),
            UpdateFromAlphaFunc(t2, rot2),
            #FadeIn(t1_c),
            FadeIn(t2_c)
        )

        csq = Square(side_length=3.0, fill_opacity=0.5, color=BLACK)
        csq.rotate(np.arctan2(1.8, 2.4))
        center = (asq.get_corner(UR) + bsq.get_corner(UL)) * 0.5
        csq.move_to(center)
        csq_c = csq.copy().set_opacity(1.0).set_color("#edf2f4")
        self.play(
            FadeIn(csq_c),
            FadeIn(csq)
        )

        new_a_marker = DashedMarker(asq.get_corner(UR), asq.get_corner(DR)).set_color("#ef233c")
        new_a_label = TexMobject("a").next_to(new_a_marker, RIGHT).set_color("#ef233c")
        new_b_marker = DashedMarker(asq.get_corner(DR) + LEFT*lb, asq.get_corner(DR)).set_color("#ef233c")
        new_b_label = TexMobject("b").next_to(new_b_marker, DOWN).set_color("#ef233c")
        new_c_marker = DashedMarker(asq.get_corner(UR), asq.get_corner(DR) + LEFT*lb).set_color("#ef233c")
        new_c_label = TexMobject("c").move_to(new_c_marker.get_center() + DR*0.15).set_color("#ef233c")

        self.wait()
        self.play(
            ReplacementTransform(VGroup(a_side_marker, a_side_label), VGroup(new_a_marker, new_a_label))
        )
        self.play(
            ReplacementTransform(VGroup(b_side_marker, b_side_label), VGroup(new_b_marker, new_b_label))
        )
        self.play(
            GrowFromCenter(VGroup(new_c_marker, new_c_label))
        )

        c2 = TexMobject("c^2").set_color(BLACK).move_to(csq.get_center())
        
        eq = TexMobject("=").next_to(area, RIGHT).set_color(BLACK)
        area_new = csq.copy().scale(0.3).next_to(eq, RIGHT)
        self.play(Write(eq))
        self.play(
            TransformFromCopy(csq, area_new)
        )

        eq2 = TexMobject("=").next_to(area_new, RIGHT).set_color(BLACK)
        self.play(
            TransformFromCopy(new_c_label, c2)
        )
        self.play(
            Write(eq2),
            ApplyMethod(c2.next_to, eq2, RIGHT)
        )

        ptheorem = TexMobject("a^2", "+", "b^2", "=", "c^2").to_edge(LEFT).set_color(BLACK)

        self.play(
            ReplacementTransform(VGroup(eqn, area, area_new, eq, eq2, c2), ptheorem)
        )
        self.play(
            ApplyMethod(ptheorem.shift, RIGHT*2)
        )
        self.wait()

class Intro(Scene):
    CONFIG = {
        "camera_config" : {"background_color" : "#edf2f4"}
    }

    def construct(self):
        sciencesort = Text('science.sort', font='Lucida Console').set_color(BLACK)
        # dot = TexMobject("\\cdot")
        # sort = Text('sort', font='Lucida Console')
        langle = TexMobject("\\langle").set_color(RED)
        rangle = TexMobject("\\rangle").set_color(RED)
        
        sciencesort.next_to(langle, RIGHT, buff=0.1)
        # dot.next_to(science, RIGHT, buff=0.0)
        # sort.next_to(dot, RIGHT, buff=0.0)
        rangle.next_to(sciencesort, RIGHT, buff=0.1)

        logo = VGroup(langle, sciencesort, rangle).move_to(ORIGIN)
        self.play(
            FadeInFromDown(logo)
        )
        self.wait(0.5)
        langle1 = TexMobject("\\langle").set_color(RED)
        rangle1 = TexMobject("\\rangle").set_color(RED)
        scienceshort = Text('science.short', font='Lucida Console').next_to(langle1, RIGHT, buff=0.1).set_color(BLACK)
        rangle1.next_to(scienceshort, RIGHT, buff=0.1)
        logo1 = VGroup(langle1, scienceshort, rangle1).move_to(ORIGIN)
        
        self.play(
            ReplacementTransform(logo, logo1)
        )

        self.wait()
        self.play(
            ApplyMethod(logo1.shift, UP)
        )

        pday = TextMobject("Pythagoras' Theorem Day Special!").shift(DOWN).set_color(BLACK)
        self.play(Write(pday))

        self.wait()

class Outro(Scene):
    CONFIG = {
        "camera_config" : {"background_color" : "#edf2f4"}
    }

    def construct(self):
        ptheorem = TexMobject("a^2", "+", "b^2", "=", "c^2").set_color(BLACK).scale(1.5)
        ptriple = TexMobject("16^2", "+", "12^2", "=", "20^2").set_color(BLACK).scale(1.5)
        pdate = TexMobject("16/12/20").scale(1.5).set_color(BLACK)
        pday = TextMobject("Pythagoras' Theorem Day!!").shift(DOWN).set_color(BLACK).scale(1.5)
        self.add(ptheorem)
        self.wait()
        self.play(
            ReplacementTransform(ptheorem, ptriple)
        )
        self.wait()
        self.play(
            ReplacementTransform(ptriple, pdate)
        )
        self.play(Write(pday))

rot90 = np.array(
    [
        [0.0, -1.0, 0.0], 
        [1.0,  0.0, 0.0],
        [0.0,  0.0, 1.0]
    ]
)
class Spiral(Scene):
    CONFIG = {
        "camera_config" : {"background_color" : "#edf2f4"}
    }

    def construct(self):
        endpt = UR
        t1 = Polygon(ORIGIN, RIGHT, UR, color=BLACK)
        self.play(DrawBorderThenFill(t1))
        side_1 = TexMobject("1").set_color(BLACK).next_to(t1, DOWN).scale(0.5)
        side_2 = TexMobject("1").set_color(BLACK).next_to(t1, RIGHT).scale(0.5)
        self.play(
            Write(side_1), Write(side_2)
        )
        side_3 = TexMobject("\\sqrt{2}").set_color(BLACK).move_to(UR/2.0 + np.dot(rot90, endpt) / np.linalg.norm(np.dot(rot90, endpt))*0.25).scale(0.5)
        self.play(Write(side_3), FadeOut(side_1))
        self.wait()

        for i in range(14):
            direction = np.dot(rot90, endpt) / np.linalg.norm(np.dot(rot90, endpt))
            label = TexMobject("\\sqrt{" + str(i+3) + "}").scale(0.5).set_color(BLACK)
            l1 = Line(ORIGIN, endpt+direction, stroke_color=BLACK)
            l2 = Line(endpt, endpt+direction, stroke_color=BLACK)
            self.play(GrowArrow(l1), GrowArrow(l2), run_time=1./(i+1))
            
            one = TexMobject("1").scale(0.5).set_color(BLACK).move_to(l2.get_center() + endpt*0.25/np.linalg.norm(endpt))
            endpt += direction
            label.move_to(l1.get_center() + direction*0.25)
            self.play(
                Write(label), 
                Write(one),
                run_time=1./(i+1))

        
        

        langle1 = TexMobject("\\langle").set_color(RED)
        rangle1 = TexMobject("\\rangle").set_color(RED)
        scienceshort = Text('science.short', font='Lucida Console').next_to(langle1, RIGHT, buff=0.1).set_color(BLACK)
        rangle1.next_to(scienceshort, RIGHT, buff=0.1)
        logo = VGroup(langle1, scienceshort, rangle1).move_to(ORIGIN)
        self.clear()
        self.add(logo)
        self.wait(0.5)
        self.play(
            ApplyMethod(logo.shift, UP*2), run_time=0.2
        )
        ptriple = TexMobject("16^2", "+", "12^2", "=", "20^2").set_color(BLACK).scale(1.5)
        pdate = TexMobject("16/12/20").scale(1.5).set_color(BLACK)
        pday = TextMobject("Pythagoras' Theorem Day!!").shift(DOWN).set_color(BLACK).scale(1.5)
        self.wait(0.2)
        self.play(
            Write(ptriple), run_time=0.2
        )
        self.wait()
        self.play(
            ReplacementTransform(ptriple, pdate), run_time=0.3
        )
        self.play(Write(pday), run_time=0.3)

        self.wait()





